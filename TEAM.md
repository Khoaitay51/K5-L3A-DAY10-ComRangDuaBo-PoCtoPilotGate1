# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): ComRangDuaBo
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ComRangDuaBo-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S3`

## Thành viên

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phạm Trường Chinh | 2A202603426 | Kỹ sư cổng (Code & Monitor) | ✓ |
|   2 | Nguyễn Văn Ba | 2A202603489 | Kỹ sư cổng (Eval, Trace & Kiểm thử) | |
|   3 | Nguyễn Minh Quân | 2A202603510 | Sản phẩm và kinh doanh (Vận hành kinh doanh) | |
|   4 | Trần Quang Nam | 2A202603516 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công chi tiết

- **Kỹ sư cổng 1 (Code & Monitor):** `lab10/guards.py` (`pre_guard`, `write_gate`), `lab10/monitors.py` (`MONITORS`); câu 2.6–2.7 (B7.1, B7.2), câu 3.5–3.6 (C7, C8).
- **Kỹ sư cổng 2 (Eval, Trace & Kiểm thử):** Chạy `unittest`, `lab10.eval`, `lab10.gate`, `lab10.trace`, `lab10.grade`; câu 2.1–2.2 (B0–B2), câu 2.8 (B7.3, `--adhoc`), câu 3.1 (C2, C3), kiểm thử hồi quy & demo 3 mốc.
- **Sản phẩm và kinh doanh (Vận hành kinh doanh):** `config/acceptance_criteria.json` (điền ngưỡng & ký), `config/operating_gates.json` (mục `business`); Phiếu A (A1–A5: câu 1.1–1.6), câu 2.3 (B3), câu 2.9 (B7.4), quyết định v1 (B8) & v2 (C12).
- **Vận hành và pháp lý:** `config/operating_gates.json` (mục `operations`, `legal`), Runbook; câu 2.4 (B4, B5), câu 2.10 (B7.5, B7.6), câu 3.7 (C10, C11), gom bài (`submission/submission.json`, `lab10.check_submission --collect`).
- **Cả bàn làm chung:** Chọn eval card & PRD v1.1 (Lab 9), thống nhất ngưỡng trước khi ký tiêu chí, pre-mortem 4 lăng kính (câu 2.5 → B6), đọc thẻ sự cố & đối chiếu (C1, C4–C6, C9).

## Cá nhân

Các exit ticket dưới đây ghi một điều học được và một điều còn chưa chắc theo phần việc của từng thành viên.

## PhamTruongChinh-2A202603426

### Phần việc phụ trách

Kỹ sư cổng (Code & Monitor), phụ trách `lab10/guards.py`, `lab10/monitors.py`, Phiếu B mục B7.1–B7.2 và Phiếu C mục C7–C8.

### Đóng góp cụ thể

- Viết cổng vòng 1, ký tiêu chí chấp nhận, cấu hình cổng kinh doanh, chốt bản chụp cổng và ghi quyết định v1 ở B8.
- Sau sự cố S3, cập nhật cổng để dùng chính sách theo ngày hiệu lực, kiểm tra hạn mức tự hoàn và áp trần số lỗi ghi tự động theo hãng mỗi ngày. Thêm hai chỉ số theo dõi và thử nghiệm trên cả bốn kho. Phạm vi pilot chốt ở HN và HCM.

### Bằng chứng

- `8fc12a4` (cổng vòng 1), `1ed5aea` (ký tiêu chí), `72d65fd` (cổng kinh doanh), `be8f9e6` và `5c19957` (chốt vòng 1 và quyết định v1), `36e3713` (cổng vòng 2, chỉ số theo dõi và Phiếu C).
- Phiếu C mục C0 ghi lần thử trên bốn kho `R-S3-after-20261118-171202-3167ca`. Báo cáo trong gói nộp ghi lần chấm `R-S3-grade-20261118-172151-86447a` cho phạm vi HN và HCM.

### Exit ticket

- Điều học được: Kiểm ngày hiệu lực của chính sách trước khi xử lý và kiểm hạn mức ngay trước khi ghi giúp chặn hai kiểu lỗi khác nhau trong S3.
- Điều còn chưa chắc: Nếu Ops nhập sai ngày hiệu lực, `policy_index_drift_rate` có phát hiện đủ sớm để dừng tự hoàn không?
- AI hỗ trợ tổng hợp mục cá nhân và soạn exit ticket từ lịch sử commit và Phiếu C.

##  NguyenVanBa-2A202603489

### Phần việc phụ trách

Kỹ sư cổng (Eval, Trace & Kiểm thử), phụ trách đánh giá bộ nền và soát lỗi ở B0–B2, kiểm thử hành vi ở B7.3 và phần đo lường ở Phiếu A.

### Đóng góp cụ thể

- Ghi kết quả bộ nền và dùng trace `T-002@55` để xác định một ca hoàn sai 20.000đ và ghi oan lỗi cho hãng VNX.
- Viết hai ca kiểm thử hành vi ở B7.3, bổ sung thước đo offline cho hành động ghi lỗi hãng ở A2 và dự đoán kết quả ở A3.

### Bằng chứng

- `7257cfa` (B0–B2), `09a44a2` (B7.3), `93e5b81` (A2–A3).
- Lần chạy bộ nền `R-base-before-20261118-160345-bde05c`, ghi tại Phiếu B mục B0–B1.

### Exit ticket

- Điều học được: Bộ nền đạt `pass_rate` 0,9909 nhưng `T-002@55` vẫn vừa hoàn sai 20.000đ vừa ghi oan lỗi hãng. Trace giúp lần theo điểm trợ lý bỏ qua số ngày trễ trong tracking.
- Điều còn chưa chắc: Bộ 22 ticket có bao phủ đủ cách khách diễn đạt số ngày trễ và các trường hợp tracking mâu thuẫn với nội dung ticket thật không?
- AI hỗ trợ tổng hợp mục cá nhân và soạn exit ticket từ lịch sử commit và Phiếu B.

## NguyenMinhQuan-2A202603510

### Phần việc phụ trách

Sản phẩm và kinh doanh, phụ trách tiêu chí chấp nhận, các mục kinh doanh trong Phiếu A và bản đồ dữ liệu ở B3.

### Đóng góp cụ thể

- Đưa `PRD_v1.1.md` từ Lab 9 vào repo, điền A1 câu 1.1, A4 câu 1.6, bản nháp A5 và các ngưỡng trong `config/acceptance_criteria.json`.
- Cập nhật bản đồ dữ liệu ở B3 và đưa tài liệu, dữ liệu thẻ sự cố, trong đó có S3, vào repo.

### Bằng chứng

- `8df46b4` (PRD), `5b46502` (Phiếu A và tiêu chí), `ffd9d0b` (B3), `4a3a28f` (tài liệu và dữ liệu thẻ sự cố).

### Exit ticket

- Điều học được: Nguồn dữ liệu dùng để ra quyết định phải rõ trong bản đồ dữ liệu. Cờ `index_active` có thể cập nhật chậm hơn ngày hiệu lực của chính sách và khiến trợ lý áp dụng sai mức hoàn.
- Điều còn chưa chắc: ROI 0,35 trong phạm vi HN và HCM có còn đạt ngưỡng 0,10 khi tính theo lượng ticket và chi phí duyệt thực tế không?
- AI hỗ trợ tổng hợp mục cá nhân và soạn exit ticket từ lịch sử commit và các phiếu của nhóm.

## TranQuangNam-2A202603516

### Phần việc phụ trách

Vận hành và pháp lý, phụ trách yêu cầu vận hành trong Phiếu A, HAZOP và runbook trong Phiếu B, cùng các mục `operations` và `legal` trong `config/operating_gates.json`.

### Đóng góp cụ thể

- Bổ sung yêu cầu đối soát, chỉ số tranh chấp lỗi hãng và ngưỡng chuyển người duyệt trong Phiếu A.
- Điền HAZOP, cập nhật checklist và runbook ca trực, cấu hình người duyệt, năng lực xử lý, điều kiện dừng, kênh cảnh báo và các trường dữ liệu cá nhân cần chặn khi gửi bên thứ ba.

### Bằng chứng

- `32bc089` (Phiếu A), `dad21fe` (Phiếu B và `config/operating_gates.json`).

### Exit ticket

- Điều học được: Khi phát hiện một lỗi ghi oan cho hãng, runbook cần ghi rõ ai nhận cảnh báo và ai có quyền tắt `file_carrier_fault` tự động để ca trực hành động ngay.
- Điều còn chưa chắc: Với năng lực 6 ca duyệt mỗi giờ mỗi người, ca trực có giữ được thời gian chờ dưới 60 phút khi ticket tăng đột biến sau bão không?
- AI hỗ trợ tổng hợp mục cá nhân và soạn exit ticket từ lịch sử commit và Phiếu B.
