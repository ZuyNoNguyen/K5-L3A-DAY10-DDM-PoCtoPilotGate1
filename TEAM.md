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
|   2 | Tạ Tiến Dũng    | 2A202603526     | Sản phẩm kinh doanh    | Không            |
|   3 | Nguyễn Văn Minh | 2A202603551 | Vận hành và pháp lý (Ops/Legal) | Không |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenVanMinh-2A202603551

### Phần việc phụ trách

Ops/Legal: CP1 thiết lập và thông tin nhóm; CP2 câu 1.2 (A1), 1.4 (A2), hỗ trợ 1.5 (A3); CP3 B4 HAZOP, B5 checklist, B7.5–B7.6 runbook và config operations/legal; CP4 thẻ S5: phân tích rủi ro chi phí/đối soát theo kho và sổ cái, HAZOP vòng 2, cập nhật checklist/runbook, rà soát báo cáo S5 và submission.

### Đóng góp cụ thể

- CP1: cập nhật tên nhóm và lớp; cấu hình upstream; kiểm tra 13 public tests.
- CP2: mục tiêu của chị Oanh/chị Hạnh; telemetry rò rỉ PII tới hãng; giải thích khoảng tin cậy.
- CP3: câu 2.4 (Phiếu B B4 HAZOP và B5 checklist 9 nhóm có PIC), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm); thiết lập operations/legal trong config dựa trên ops_limits, ops_facts và tiêu chí đã ký, không sửa khối business.
- CP4 (Ops/Legal, S5): đọc thẻ từ repo phát đề và đối chiếu `ledger_seed`, `warehouse_id`, ticket dài với báo cáo; xác định chi phí kép HCM-B2B khi qua LLM rồi chuyển người, và nguy cơ hoàn trùng/hoàn thiếu tại `S5-21`; rà HAZOP C4, giả định môi trường C5, risk register C10 và checklist/runbook 4–5 C11. Đề xuất ngưỡng cảnh báo theo kho, phân quyền NV-TUNG/NV-HANH/NV-OANH. Việc sửa guard/monitor và quyết định phạm vi v2 do Engineer/PM chốt trên main.
- Dùng ChatGPT hỗ trợ đọc tài liệu, code và biên soạn phần Ops/Legal; đã đối chiếu dữ liệu mock.

### Bằng chứng

- Phiếu A: A1 câu 1.2, A2 cột telemetry câu 1.4, A3 câu 1.5.
- Phiếu B: B4, B5, B7.5, B7.6; `config/operating_gates.json` mục operations/legal. Mốc checkpoint/grade do Gate Engineer chạy sau đồng bộ.
- Git commit cá nhân: CP1–CP2 `cd8f031`; CP3 `4b284b8`. Main đã ghép nội dung tại `033c104` và chốt vòng 1 tại `c9fd022`.
- Public tests: 13/13 OK; prepared run `R-base-prepared-20261118-153046-d0beba` có pass_rate = 1, pass^k = 1, 0 hoàn sai, 0 lỗi hãng oan, 0 PII leak, 0 ca ùn. Bản round1 được khóa hash `34a3f1e5`.
- Kết quả vận hành: 1 người duyệt, 6 ca/giờ, chờ tối đa 60 phút, kiểm mẫu 10%, chặn PII khi gửi hãng và yêu cầu nguyên nhân tracking trước khi ghi lỗi hãng. Trên bộ nền, chi phí trung bình 4.456đ/ticket, ROI 1,24.
- S5: thẻ `incidents/S5/card.md`, ticket `S5-21`, `S5-50`–`S5-61`, `world_patch.ledger_seed`; report vòng 2 từ nhóm tại `submission/runs/grade-report.md` và Phiếu C C3.5, C4, C5, C9–C11. Bản chính thức ghi quyết định v2 `Thu hẹp` tại commit `20c00b8`.

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

## TaTienDung-2A202603526

### Phần việc phụ trách

- **Vai trong bàn:** Sản phẩm và kinh doanh[cite: 1, 6].
- **Câu của đề & mục phiếu phụ trách:**
  - **Vòng 1 · Khối 1 (Phiếu A — `templates/form-a-criteria.md`):** Câu 1.1 (mục tiêu cấp hệ thống, mục A1), Câu 1.5 (đọc khoảng tin cậy 95%, mục A3), Câu 1.6 (xây dựng Bản tiêu chí chấp nhận, ranh giới đầu ra, soát 4 câu hỏi và chốt ngưỡng, mục A4)[cite: 6, 9].
  - **Vòng 1 · Khối 2 (Phiếu B — `templates/form-b-evaluation-gates.md`):** Câu 2.3 (bản đồ dữ liệu và phân tích concept drift khi chuyển sang `REFUND-v4`, mục B3), Câu 2.5 (Pre-mortem lăng kính Kinh doanh, mục B6), Câu 2.9 (đặt cổng kinh doanh, mục B7.4)[cite: 6, 11, 12].
  - **Vòng 2 · Khối 3 (Phiếu C — `templates/form-c-incident.md`):** Đọc chỉ số chi phí, ROI, ngân sách hoàn tự động và phối hợp chốt quyết định Gate 1 v2 (mục C12)[cite: 6].
- **File cấu hình trực tiếp tham gia:** `config/acceptance_criteria.json` (soạn thảo ngưỡng `required`, `nice_to_have`, `business_ops`, `stop_condition`, `decision_rule`) và `config/operating_gates.json` (mục `business`: `daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`)[cite: 2, 6, 13].

### Đóng góp cụ thể

- Soạn thảo bộ ngưỡng chất lượng và kinh doanh/vận hành trong `config/acceptance_criteria.json` dựa trên dữ liệu thực tế tại `data/world.json` (`ops_facts`, `ops_limits`: đặt trần chi phí 7.500đ/ticket so với 10.000đ làm tay, `roi_min = 0.3`, các ngưỡng an toàn bằng `0`) trước khi nhóm tiến hành ký niêm phong[cite: 6, 11].
- Hoàn thiện phân tích mục tiêu hệ thống, giải thích khoảng tin cậy 95% và câu tiêu chí hành động ("Nếu … thì chúng tôi sẽ …") tại Phiếu A (mục A1, A3, A4)[cite: 6, 9].
- Xây dựng bản đồ dữ liệu nguồn sự thật (`orders[].parcels`, `policies`, `approvals`), chỉ ra rủi ro concept drift vào ngày `2026-12-01` khi chính sách chuyển sang `REFUND-v4` tại Phiếu B (mục B3), và đóng góp phân tích rủi ro ngân sách/kho sỉ `HCM-B2B` vào bảng Pre-mortem (mục B6)[cite: 11, 12].
- Thiết lập các giới hạn kinh doanh trong `config/operating_gates.json` mục `business` (`daily_refund_cap_vnd = 1500000`, `cost_budget_per_ticket_vnd = 1500`, `pilot_scope`, `roi_min = 0.3`) và giải trình cơ sở số liệu tại Phiếu B (mục B7.4)[cite: 11, 12, 13].
- Đối chiếu các chỉ số kinh doanh và vận hành (chi phí/ticket, ROI, tổng tiền hoàn so với trần) ở cả hai vòng để cùng nhóm thống nhất quyết định Gate 1 v2 (`Thu hẹp`) trên thẻ sự cố `S5`[cite: 6].

### Bằng chứng

- **Thẻ sự cố & Quyết định v2:** Thẻ `S5` · Quyết định v2: `Thu hẹp` (theo commit `20c00b8`).
- **Mã commit:**
  - `033c104` (merge phần `operating_gates.json` mục `business` và Phiếu B từ `TaTienDung`)[cite: 13].
  - `c9fd022` (chốt cổng vòng 1, quyết định v1).
  - `c9ddf39` (hoàn thiện 4 lăng kính Pre-mortem mục B6)[cite: 12].
  - `20c00b8` (hoàn thành vòng 2 thẻ `S5`, quyết định v2 `Thu hẹp`, đủ thành phần).
- **Mã lần chạy (`submission/runs/`):**
  - `submission/runs/R-S5-before-20261118-163954-d71028/` (mốc `base`)
  - `submission/runs/R-S5-prepared-20261118-163954-d71028/` (mốc `prepared` - cổng vòng 1)
  - `submission/runs/R-S5-after-20261118-163954-d71028/` (mốc `after` - cổng vòng 2)
  - `submission/runs/grade-report.md` và `submission/runs/journal.jsonl`
- **Dòng trong phiếu:**
  - `templates/form-a-criteria.md`: Mục A1 (câu 1.1), A3 (câu 1.5), A4 (câu 1.6)[cite: 6, 9].
  - `templates/form-b-evaluation-gates.md`: Mục B3 (câu 2.3), B6 (lăng kính Kinh doanh), B7.4 (câu 2.9)[cite: 6, 12].
  - `templates/form-c-incident.md`: Mục C12 (quyết định v2 `Thu hẹp` và đối chiếu chỉ số kinh doanh)[cite: 6].
  - `config/operating_gates.json`: Khối `"business"`[cite: 1, 13].

### Exit ticket

- **Một điều học được:** Hiểu rõ tầm quan trọng của việc khóa cứng tiêu chí chấp nhận (Acceptance Criteria) trước khi chạy đánh giá đầu tiên để tránh thiên lệch hợp lý hóa sau khi thấy số liệu, đồng thời thấy được rằng một cổng kiểm soát kinh doanh bằng con số (như trần hoàn tiền ngày hay giới hạn phạm vi kho pilot) có thể chặn rủi ro tài chính hiệu quả mà không cần phức tạp hóa prompt hay code[cite: 1, 2, 10].
- **Một điều còn chưa chắc:** Cách hiệu chỉnh tối ưu sự đánh đổi (trade-off) giữa tỉ lệ kiểm mẫu (`review_sampling_pct`) và số người trực ca (`reviewers_on_shift`) khi lưu lượng thực tế tăng đột biến gấp 3–4 lần vào mùa sale lớn để vừa giữ hàng chờ dưới SLA 60 phút vừa không đẩy chi phí mỗi ticket vượt mức làm tay 10.000đ[cite: 1, 10, 11].
>>>>>>> origin/TaTienDung
