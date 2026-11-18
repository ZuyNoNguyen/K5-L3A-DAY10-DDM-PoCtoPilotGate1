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

Ops/Legal: CP1 thông tin nhóm và thiết lập; CP2 câu 1.2 (Phiếu A A1), 1.4 (A2), hỗ trợ 1.5 (A3). Các bước sau: câu 2.4, 2.10, các mục Ops/Legal của Phiếu C và submission.

### Đóng góp cụ thể

- CP1: cập nhật tên nhóm và lớp; cấu hình upstream; kiểm tra 13 public tests.
- CP2: mục tiêu của chị Oanh/chị Hạnh; telemetry rò rỉ PII tới hãng; giải thích khoảng tin cậy.
- CP3: câu 2.4 (Phiếu B B4 HAZOP và B5 checklist 9 nhóm có PIC), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm); thiết lập operations/legal trong config dựa trên ops_limits, ops_facts và tiêu chí đã ký, không sửa khối business.
- Dùng ChatGPT hỗ trợ đọc tài liệu, code và biên soạn phần Ops/Legal; đã đối chiếu dữ liệu mock.

### Bằng chứng

- Phiếu A: A1 câu 1.2, A2 cột telemetry câu 1.4, A3 câu 1.5.
- Phiếu B: B4, B5, B7.5, B7.6; `config/operating_gates.json` mục operations/legal. Mốc checkpoint/grade do Gate Engineer chạy sau đồng bộ.
- 13 public tests OK; commit và run ID cập nhật sau khi đồng bộ.

### Exit ticket

- Học được: cổng vận hành và telemetry bảo vệ bên thứ ba phải độc lập với model.
- Chưa chắc: năng lực nhân sự và rò rỉ dữ liệu trong pilot thực tế cần đo tiếp.
