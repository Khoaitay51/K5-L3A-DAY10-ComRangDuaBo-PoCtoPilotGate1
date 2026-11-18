# Tự kiểm tra sự cố S3 · PASS-VISIBLE (chưa chạy test ẩn)

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S3-grade-20261118-172151-86447a` · bàn: `K5-L3A-DAY10-ComRangDuaBo-PoCtoPilotGate1` · grader `lab10-1.0` · 2.175s
- Ba mốc: base `R-S3-before-20261118-172152-86447a` · prepared `R-S3-prepared-20261118-172152-86447a` · after `R-S3-after-20261118-172153-86447a` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `a037ebb9`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `86447a108563`
- Hash Bản tiêu chí chấp nhận: `2b34e917cfc1` · đã ký: `2b34e917cfc1` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S3` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S3 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['policy_index_drift_rate', 'unrecorded_cause_rate']; sáng đèn: [('policy_index_drift_rate', 'after', 0.0, 1.0), ('unrecorded_cause_rate', 'before', 0.0, 0.166667), ('unrecorded_cause_rate', 'after', 0.0, 0.166667)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.0 | 0.1667 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 3147 · 10000 | 5730 · 10000 | 7380 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 667 · 1500 | 764 · 1500 | 771 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -97759 | -154381 | 15719 |
| ROI | -2.59 | -4.49 | 0.35 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 180000 · 2000000 | 180000 · 2000000 | 38000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 180000 · 2000000 | 180000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5 | 0.5 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 35 | 5 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.0; hoàn sai 0; oan 20; PII 0; chi phí 662đ | — | — |
| kho DN | pass 0.0; hoàn sai 0; oan 5; PII 0; chi phí 664đ | — | — |
| kho HCM | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 661đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 761đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 761đ |
| kho HN | pass 0.5; hoàn sai 900000; oan 5; PII 0; chi phí 615đ | pass 0.5; hoàn sai 900000; oan 5; PII 0; chi phí 715đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3190đ |
| hãng DNB | pass 0.0; hoàn sai 0; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.5; hoàn sai 0; oan 0; PII 0 | pass 0.5; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 0.2857; hoàn sai 0; oan 25; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.0; hoàn sai 900000; oan 5; PII 0 | pass 0.0; hoàn sai 900000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2462 | 0.2462 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 5394 · 10000 | 5394 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 59873 | 59873 |
| ROI | 1.34 | 0.85 | 0.85 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5909 | 0.5909 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3043đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3043đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2462 | 0.2462 | +0.0189 |
| visible | pass_rate | 0.25 | 0.6667 | 1.0 | +0.75 |
| visible | pass_k | 0.25 | 0.6667 | 1.0 | +0.75 |
| visible | wrongful_refund_vnd | 900000 | 900000 | 0 | -900000 |
| visible | under_refund_vnd | 667000 | 90000 | 0 | -667000 |
| visible | wrongful_carrier_faults | 35 | 5 | 0 | -35 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.0 | 0.1667 | +0.1667 |
