"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def policy_index_drift_rate(trials):
    """S3 · concept drift: tỉ lệ ticket mà cờ index_active của bảng chính sách KHÁC phiên bản có hiệu lực theo ngày.
    Tín hiệu: sự kiện `policy` có "pinned": true (pre_guard phải ghim lại phiên bản theo effective_from/effective_to).
    Không cần nhãn. Bình thường = 0; > 0 nghĩa là Ops chưa chuyển cờ sau khi chính sách mới có hiệu lực."""
    def drifted(t):
        return any(e.get("type") == "policy" and e.get("pinned") for e in t["events"])
    return sum(drifted(t) for t in trials) / max(1, len(trials))


def unrecorded_cause_rate(trials):
    """S3 · dữ liệu thiếu (INCOMPLETE): tỉ lệ ticket mà tracking trễ nhưng CHƯA ghi nguyên nhân (cause_recorded = false).
    Đây là chỗ code gốc tự điền CARRIER, nên tăng là dấu hiệu nguy cơ ghi oan cho hãng."""
    def missing(t):
        return any(e.get("type") == "tracking" and e.get("cause_recorded") is False for e in t["events"])
    return sum(missing(t) for t in trials) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "policy_index_drift_rate": policy_index_drift_rate,
    "unrecorded_cause_rate": unrecorded_cause_rate,
}
STARTER_MONITORS = ("escalation_rate",)
