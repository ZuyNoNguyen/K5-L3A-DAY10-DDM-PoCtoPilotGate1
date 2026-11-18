# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): DDM
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-DDM-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
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
