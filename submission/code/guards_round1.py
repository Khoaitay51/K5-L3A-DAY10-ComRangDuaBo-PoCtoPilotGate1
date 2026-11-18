"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _load_order_context(ctx, action):
    """Lấy (order, parcel, policy, db_delay) từ nguồn sự thật."""
    order_id = action.get("order_id") or (ctx.ticket or {}).get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not policy:
        return order, None, policy, None
    parcel = H.ticket_parcel(order, ctx.ticket or {}, ctx.as_of)
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    return order, parcel, policy, db_delay


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    order, parcel, policy, db_delay = _load_order_context(ctx, action)

    if tool == "issue_refund":
        if order and parcel and policy and db_delay is not None:
            entitled = H.entitlement_vnd(policy, order, db_delay, parcel.get("delay_cause"))
            if action.get("amount_vnd", 0) > entitled and not action.get("approval_id"):
                ctx.log("guard_refund_mismatch", entitled=entitled, requested=action.get("amount_vnd", 0))
                return Verdict.escalate("số tiền hoàn vượt quyền lợi theo tracking DB, chuyển người duyệt")

        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        if cap is not None and not action.get("approval_id"):
            spent = ctx.tools.auto_refund_today_vnd()
            if spent + action.get("amount_vnd", 0) > cap:
                return Verdict.escalate("vượt trần hoàn tự động trong ngày, chuyển người duyệt")

    elif tool == "file_carrier_fault":
        if order and parcel and policy and db_delay is not None:
            if not H.carrier_at_fault(policy, parcel, db_delay) or action.get("delay_days") != db_delay:
                ctx.log("guard_fault_blocked", db_delay=db_delay, action_delay=action.get("delay_days"))
                return Verdict.deny("không đủ điều kiện ghi lỗi hãng hoặc lệch số ngày trễ so với tracking DB")

    elif tool == "notify_carrier":
        payload = dict(action.get("payload") or {})
        if db_delay is not None and payload.get("delay_days") is not None and payload.get("delay_days") != db_delay:
            return Verdict.deny("chặn gửi thông báo sai số ngày trễ cho hãng")
        blocked = set((ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
        removed = [k for k in blocked if k in payload]
        if removed:
            for k in removed:
                payload.pop(k, None)
            return Verdict.modify("lọc trường PII trước khi gửi hãng", payload=payload)

    return Verdict.allow()
