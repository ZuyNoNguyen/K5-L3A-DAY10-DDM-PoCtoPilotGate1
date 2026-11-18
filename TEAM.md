# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): DDM
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-DDM-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Khánh Duy | 2A202603575 | Kỹ sư cổng (Gate Engineer) | Có |
|   2 |           |      |     |             |
|   3 | Nguyễn Văn Minh | 2A202603551 | Vận hành và pháp lý (Ops/Legal) | Không |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenVanMinh-2A202603551

### Phần việc phụ trách

Ops/Legal: CP1 thiết lập và thông tin nhóm; CP2 câu 1.2 (A1), 1.4 (A2), hỗ trợ 1.5 (A3); CP3 câu 2.4 (B4 HAZOP, B5 checklist) và câu 2.10 (B7.5 runbook, B7.6 giờ cao điểm), cấu hình operations/legal. Tiếp theo: các mục Ops/Legal trong Phiếu C và kiểm tra submission.

### Đóng góp cụ thể

- CP1: cập nhật tên nhóm và lớp; cấu hình upstream; kiểm tra 13 public tests.
- CP2: mục tiêu của chị Oanh/chị Hạnh; telemetry rò rỉ PII tới hãng; giải thích khoảng tin cậy.
- CP3: câu 2.4 (Phiếu B B4 HAZOP và B5 checklist 9 nhóm có PIC), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm); thiết lập operations/legal trong config dựa trên ops_limits, ops_facts và tiêu chí đã ký, không sửa khối business.
- Dùng ChatGPT hỗ trợ đọc tài liệu, code và biên soạn phần Ops/Legal; đã đối chiếu dữ liệu mock.

### Bằng chứng

- Phiếu A: A1 câu 1.2, A2 cột telemetry câu 1.4, A3 câu 1.5.
- Phiếu B: B4, B5, B7.5, B7.6; `config/operating_gates.json` mục operations/legal. Mốc checkpoint/grade do Gate Engineer chạy sau đồng bộ.
- Git commit cá nhân: CP1–CP2 `cd8f031`; CP3 `4b284b8`. Main đã ghép nội dung tại `033c104` và chốt vòng 1 tại `c9fd022`.
- Public tests: 13/13 OK; prepared run `R-base-prepared-20261118-153046-d0beba` có pass_rate = 1, pass^k = 1, 0 hoàn sai, 0 lỗi hãng oan, 0 PII leak, 0 ca ùn. Bản round1 được khóa hash `34a3f1e5`.
- Kết quả vận hành: 1 người duyệt, 6 ca/giờ, chờ tối đa 60 phút, kiểm mẫu 10%, chặn PII khi gửi hãng và yêu cầu nguyên nhân tracking trước khi ghi lỗi hãng. Trên bộ nền, chi phí trung bình 4.456đ/ticket, ROI 1,24.

### Exit ticket

- Học được: cổng vận hành và telemetry bảo vệ bên thứ ba phải độc lập với model.
- Chưa chắc: năng lực nhân sự và rò rỉ dữ liệu trong pilot thực tế cần đo tiếp.

### Bổ sung nhận diện rủi ro sau checkpoint (không thay đổi Phiếu B đã chốt)

B6 trên `main` được chốt khi mới có lăng kính Kinh doanh. Hai nguy cơ dưới đây là **ghi chú hậu kiểm của Ops/Legal**, không phải bằng chứng cho rằng nhóm đã thảo luận chúng trước checkpoint; cần mang sang Phiếu C mục C1 để so với thẻ sự cố sau khi nhận thẻ:

- **Con người và vận hành – INCAPABLE:** Khi có hơn 6 ca cần người duyệt trong một giờ mà chỉ có một người trực, hàng chờ có thể vượt SLA 60 phút. Nguồn kiểm: `ops_facts`, `operations.reviewers_on_shift`, `queue.wait_max_min`, `queue.stuck`. Biện pháp: ngưỡng vàng khi chờ >30 phút, NV-HANH gọi hỗ trợ; NV-TUNG dừng mở rộng/chuyển ca mới sang xử lý tay khi chờ >60 phút hoặc có ca ùn.
- **Pháp lý – PERTURBED/INCOMPLETE:** Ticket tự do hoặc đơn quà tặng có thể đưa `customer_note` và `recipient_contact` đến đối tác; tracking thiếu nguyên nhân còn có thể làm hãng bị ghi lỗi oan. Nguồn kiểm: `agent.py` tại `notify_carrier`, HAZOP B4, `wrongful_carrier_faults`, `pii_leaks`. Biện pháp: lọc trường PII, chỉ ghi lỗi hãng khi nguyên nhân được tracking xác nhận; dừng tool tương ứng khi có vi phạm.
- **Kỹ thuật – INVALID/WRONG (đề xuất cả bàn kiểm tra ở C1):** Chính sách có thể hết hiệu lực hoặc lời kể của khách khác dữ liệu tracking, gây hoàn sai/ghi lỗi oan. Nguồn: `effective_policy`, `db_delay_days`, trace `T-002@55`; cổng vòng 1 đối chiếu trước khi ghi.

Đây là rủi ro cần đối chiếu và kiểm chứng ở CP4, không được dùng để sửa lịch sử checkpoint CP3.

## NguyenKhanhDuy-2A202603575

### Phần việc phụ trách

Trưởng nhóm & Kỹ sư cổng: CP1 (tạo nhánh, gắn `upstream`, danh tính Git, 13 public tests); CP2 (ký tiêu chí `config/acceptance_criteria.json`, Phiếu A câu 1.1, 1.3, 1.5, 1.6, A5); CP3 (chạy `base`, trace `T-002@55`, code 3 cổng vòng 1 trong `lab10/guards.py`, 2 ticket `--adhoc`, merge 3 nhánh, chạy `checkpoint`, chốt v1 ở Phiếu B B0–B2, B7.1–B7.3, B8); CP4–CP5 (kéo thẻ `S5`, phân tích `S5-21`/`S5-51`/`S5-70`, sửa `lab10/guards.py`, thu hẹp `pilot_scope` ở `config/operating_gates.json`, thêm 2 monitor trong `lab10/monitors.py`, hoàn thiện Phiếu C C0–C12 và `submission/`).

### Đóng góp cụ thể

- CP1–CP2: thiết lập Git/remote `upstream`, kiểm tra `13/13` unit tests; điền và ký `config/acceptance_criteria.json` (hash `05ef76c7`, commit `97e536b`) trước khi chạy đánh giá lần đầu; hoàn thiện Phiếu A.
- CP3: chạy baseline (`R-base-before-20261118-151428-bde05c`), phân tích lỗi chìm `T-002@55`, code 3 cổng hệ thống trong `lab10/guards.py` (`pre_guard` ghim policy, `write_gate` kiểm tra `issue_refund`, `file_carrier_fault`, lọc PII `notify_carrier`), kiểm thử `--adhoc`, hợp nhất bài từ 3 nhánh (`033c104`), chốt vòng 1 (`34a3f1e5`, commit `c9fd022`).
- CP4–CP5: kéo thẻ `S5`, phát hiện và sửa 2 vấn đề cốt lõi (hoàn bổ sung phần còn lại `remaining` cho `S5-21` và loại kho sỉ `HCM-B2B` khỏi `pilot_scope`), thêm `estimated_cost_per_ticket_vnd` và `refund_gate_block_rate` vào `lab10/monitors.py`, chạy `grade --incident S5` (`criteria ✅`, `visible ✅`, `regression ✅`, `monitor ✅`), chốt quyết định v2 (`Thu hẹp`) và gom `submission/` (`ĐỦ THÀNH PHẦN`).
- Sử dụng trợ lý AI (Antigravity / Gemini) để hỗ trợ đọc codebase, thiết kế và kiểm thử cổng, đối chiếu trace/report và biên soạn phiếu; toàn bộ con số và quyết định đã được kiểm chứng lại trên các lần chạy thực tế.

### Bằng chứng

- Ký tiêu chí: commit `97e536b` (`2026-11-18T14:56:36`), hash `05ef76c7`.
- Nhánh cá nhân & hợp nhất vòng 1: `NguyenKhanhDuy` (`e05482c`), merge `033c104`, chốt vòng 1 `c9fd022` (`34a3f1e5`).
- Các lần chạy: `R-base-before-20261118-151428-bde05c` (base), `R-base-prepared-20261118-153046-d0beba` (prepared), `R-S5-grade-20261118-163815-d0beba` (S5 trước sửa), `R-S5-after-20261118-163952-d71028` (S5 sau sửa: `pass_rate = 1.0`, `ROI = 1.51`), `R-base-after-20261118-163953-d71028` (`110/110`), `R-S5-grade-20261118-163953-d71028` (grade cuối).
- Phiếu: Phiếu A (`A1–A5`), Phiếu B (`B0–B2`, `B6`, `B7.1–B7.3`, `B8`), Phiếu C (`C0–C12`).

### Exit ticket

- Học được: Cổng phòng ngừa hiệu quả nhất là cổng đặt ngoài model dựa trên nguồn sự thật (`ledger_rows`, `tracking DB`, `pilot_scope`), và phải đo tách biệt theo từng phân khúc kho để không bị số tổng che mất phân khúc lỗ (`HCM-B2B`).
- Chưa chắc: Độ trễ đồng bộ sổ cái hoàn tay và tỉ lệ ticket dài thực tế ngoài production tại 4 kho bán lẻ cần được theo dõi sát trước Gate 2.
