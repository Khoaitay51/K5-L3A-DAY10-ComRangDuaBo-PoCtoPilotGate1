# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): ComRangDuaBo
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ComRangDuaBo-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      | Kỹ sư cổng (Code & Monitor) |             |
|   2 |           |      | Kỹ sư cổng (Eval, Trace & Kiểm thử) |             |
|   3 |           |      | Sản phẩm và kinh doanh (Vận hành kinh doanh) |             |
|   4 |           |      | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công chi tiết

- **Kỹ sư cổng 1 (Code & Monitor):** `lab10/guards.py` (`pre_guard`, `write_gate`), `lab10/monitors.py` (`MONITORS`); câu 2.6–2.7 (B7.1, B7.2), câu 3.5–3.6 (C7, C8).
- **Kỹ sư cổng 2 (Eval, Trace & Kiểm thử):** Chạy `unittest`, `lab10.eval`, `lab10.gate`, `lab10.trace`, `lab10.grade`; câu 2.1–2.2 (B0–B2), câu 2.8 (B7.3, `--adhoc`), câu 3.1 (C2, C3), kiểm thử hồi quy & demo 3 mốc.
- **Sản phẩm và kinh doanh (Vận hành kinh doanh):** `config/acceptance_criteria.json` (điền ngưỡng & ký), `config/operating_gates.json` (mục `business`); Phiếu A (A1–A5: câu 1.1–1.6), câu 2.3 (B3), câu 2.9 (B7.4), quyết định v1 (B8) & v2 (C12).
- **Vận hành và pháp lý:** `config/operating_gates.json` (mục `operations`, `legal`), Runbook; câu 2.4 (B4, B5), câu 2.10 (B7.5, B7.6), câu 3.7 (C10, C11), gom bài (`submission/submission.json`, `lab10.check_submission --collect`).
- **Cả bàn làm chung:** Chọn eval card & PRD v1.1 (Lab 9), thống nhất ngưỡng trước khi ký tiêu chí, pre-mortem 4 lăng kính (câu 2.5 → B6), đọc thẻ sự cố & đối chiếu (C1, C4–C6, C9).

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
