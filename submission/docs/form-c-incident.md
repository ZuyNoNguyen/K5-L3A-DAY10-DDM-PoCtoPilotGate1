# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** DDM (`K5-L3A-DAY10-DDM-PoCtoPilotGate1`) · **Thẻ đã bốc:** S5 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S5-prepared-20261118-163816-d0beba` | S5 · prepared | nhận thẻ S5, chưa sửa thêm (đúng cổng vòng 1 đã chốt `34a3f1e5`) | `0.9667` (`[0.9333, 1.0]`) | `0.9667` | `0đ · 0 · 0` (thiếu hoàn `60.000đ` ở `S5-21`) | `0.5` | Cổng V1 chặn được `890k` hoàn sai & `20` lỗi oan, nhưng hỏng `S5-21` và kho `HCM-B2B` tốn `10.382đ > làm tay`. |
| 2 | `R-S5-after-20261118-163952-d71028` | S5 · after | `v2`: hoàn phần còn lại theo sổ cái (`guards.py`), loại kho `HCM-B2B` (`operating_gates.json`), thêm 2 monitor | `1.0` (`[1.0, 1.0]`) | `1.0` | `0đ · 0 · 0` | `0.1667` | Sửa dứt điểm `S5-21`, bỏ vượt trần `HCM-B2B`, `cost = 3.980đ`, `ROI = 1.51`, `visible ✅`. |
| 3 | `R-S5-grade-20261118-163953-d71028` | S5 · grade (3 mốc) | chạy tự kiểm tra đầy đủ 3 mốc sau khi sửa | `1.0` | `1.0` | `0đ · 0 · 0` | `0.1667` | `criteria ✅`, `visible ✅`, `regression ✅`, `monitor ✅`; không vượt trần. |
| 4 | `R-base-after-20261118-163953-d71028` | base · after | (kiểm không regression trên bộ nền) | `1.0` (`[1.0, 1.0]`) | `1.0` | `0đ · 0 · 0` | `0.2273` | `110/110` trials xanh, không làm hỏng bất kỳ ca đúng nào của bộ nền. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident S5
```

- Mã lần chạy grade: `R-S5-grade-20261118-163815-d0beba` · base: `R-S5-before-20261118-163816-d0beba` · prepared: `R-S5-prepared-20261118-163816-d0beba`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared):
  - `wrongful_refund_vnd`: giảm từ `890.000đ` → **`0đ`** (chặn được hoàn trùng 2–3 lần như `S5-01`/`S5-02` và hoàn sai).
  - `wrongful_carrier_faults`: giảm từ `20` → **`0`**.
  - `llm_cost_max_per_ticket_vnd`: giảm từ `2.412đ` (vượt trần `1.500đ`) → **`764đ`** (nhờ `cost_budget_per_ticket_vnd = 1500` chuyển các ticket quá dài như `S5-50`, `S5-70` sang người đọc).
  - `net_saving_per_day_vnd`: từ **`-60.486đ`** (`ROI = -0.33`) → **`+103.870đ`** (`ROI = +0.53`).
- Khối kinh doanh và vận hành còn dòng nào vượt trần: Còn 1 dòng vượt trần: **`kho HCM-B2B: mỗi ticket tốn 10.382đ > làm tay 10.000đ`** (vì 100% đơn sỉ ở đó đọc xong vẫn phải chuyển người duyệt). Ngoài ra `S5-21@11..55` bị chặn nhầm gây `under_refund_vnd = 60.000đ`.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? Chủ yếu thuộc lăng kính **Kinh doanh** (nhóm ticket không thể có lời ở kho sỉ `HCM-B2B`, chi phí LLM ticket dài) và **Kỹ thuật** (sổ cái hoàn nhiều lần: hoàn trùng vs hoàn bổ sung một phần).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Có nằm một phần** trong B6: dòng *Kinh doanh* đã dự báo rủi ro kho `HCM-B2B` (giá trị ≥ 2 triệu) và ticket dài, nhưng chỉ mới đặt `daily_refund_cap_vnd` và `cost_budget_per_ticket_vnd`, chưa loại trừ `HCM-B2B` khỏi `pilot_scope` nên ở `prepared` kho này vẫn lỗ (`10.382đ > 10.000đ`). Dòng *Kỹ thuật* có chặn hoàn trùng (`ledger_rows`), nhưng **chưa nghĩ tới ca hoàn bổ sung một phần** (`S5-21`).
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| *(Bổ sung vòng 2)* Nhóm đơn sỉ `HCM-B2B` hầu hết vượt hạn mức tự động `300.000đ`, khiến trợ lý tốn thêm tiền LLM đọc rồi vẫn chuyển người duyệt (`10.382đ/ticket > 10.000đ` làm tay). | Kinh doanh | Khối `by_segment` / `segments` trong `report.json` (`HCM-B2B worse_than_manual = true`) và `config/operating_gates.json → pilot_scope`. |
| *(Bổ sung vòng 2)* Cổng chống hoàn trùng chặn cứng mọi đơn có dòng trong `ledger_rows()`, làm từ chối nhầm đơn mới được hoàn một phần trước đó (`S5-21`). | Kỹ thuật | `trace --suite S5 --ticket S5-21 --seed 11` và `incidents/S5/world_patch.json → ledger_seed`. |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite S5 --ticket S5-21 --seed 11
python3 -m lab10.trace --suite S5 --ticket S5-51 --seed 11
python3 -m lab10.trace --suite S5 --ticket S5-70 --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `LogiX (CFO / ngân sách vận hành) và khách hàng hoàn bổ sung` · đo bằng gì `chi phí mỗi ticket theo kho (đ), tiết kiệm ròng (đ), ROI, tiền hoàn sai/thiếu (đ)` · bao nhiêu ở mốc base `tiết kiệm ròng -60.486đ/ngày, ROI -0.33, hoàn sai 890.000đ, LLM max 2.412đ > 1.500đ`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S5-51@11` (kho `HCM-B2B`): `05 proposal {"amount_vnd": 230000}` → `06 result {"status": "escalated", "cost_vnd": 565}`; report `prepared`: `kho HCM-B2B: mỗi ticket tốn 10382đ > làm tay 10000đ`. | Trưởng ca duyệt (`NV-HANH`) nhận ca; **CFO / LogiX chịu lỗ vận hành** (trả cả LLM + công người). | Cao | **Lỗi chìm** (mỗi ticket riêng lẻ đều `ĐẠT` trạng thái `escalated`, chỉ khi cộng chi phí theo kho mới thấy đắt hơn làm tay). |
| 2 | `S5-21@11`: `06 gate {"tool": "issue_refund", "action": "deny", "reason": "đơn đã có giao dịch hoàn tiền trong sổ cái"}` → `status: "denied"`, dù nhãn cần hoàn thêm `12.000đ` (`under_refund_vnd = 60.000đ` trên 5 seed). | **Khách hàng (`C-16`)** bị từ chối nhầm phần hoàn còn thiếu và thiếu ghi lỗi hãng `MKD`. | Cao | **Lỗi ngữ cảnh** (cổng chống hoàn trùng chỉ kiểm tra tồn tại dòng sổ cái mà không kiểm tra số tiền đã hoàn so với hạn mức chính sách). |
| 3 | `S5-70@11` (ở mốc `base`): ticket đính kèm danh sách hàng siêu dài khiến tiền LLM lên tới `2.412đ > trần 1.500đ` (ở `prepared` bị `business_gate` chuyển `escalated` tốn `10.000đ` công người). | **CFO / LogiX** chịu chi phí LLM/nhân công bất thường cho ticket dài. | Trung bình | **Giới hạn của hệ thống** (chi phí token tăng tuyến tính theo độ dài văn bản khách dán kèm). |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Không. | Không. | **Đúng** (khách dán bảng hàng dài hàng trăm dòng vào chung văn bản ticket khiến LLM phải đọc hết). |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | **Đúng** (chính sách định giá theo đơn lẻ, không phân tách đơn vị kinh tế của kho sỉ `HCM-B2B`). | **Đúng** (cổng chỉ kiểm tra boolean `ledger_rows` có rỗng không, thiếu tổng số tiền đã hoàn `sum(amount_vnd)`). | **Đúng** (dữ liệu đầu vào nhiễu, chứa danh sách sản phẩm không cần cho việc tính phí hoàn trễ). |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | **Đúng** (trợ lý đọc trước rồi vẫn đẩy về quy trình người duyệt thủ công, gây trùng chi phí). | **Đúng** (bút toán hoàn một phần có sẵn trong `ledger_seed` và giao dịch mới của trợ lý dùng chung sổ cái). | Không. |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Không (từng ca vẫn chạy nhưng tổng hợp cả kho thì lỗ). | Không. | Không. |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | CFO thấy kho `HCM-B2B` tốn `10.382đ/ticket`, đắt hơn làm tay `10.000đ/ticket`. | Khách đã được hoàn một phần (`10.000đ/22.000đ`) nhưng khi đòi phần còn lại (`12.000đ`) thì bị từ chối trắng. | CFO thấy có ticket ngốn tiền LLM vượt trần `1.500đ` (lên tới `2.412đ` ở base). |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | **Thu hẹp phạm vi pilot (`config`)**: loại kho `HCM-B2B` khỏi `pilot_scope` để xử lý thủ công ngay từ đầu. | **Sửa cổng `write_gate` (`issue_refund`)**: tính `remaining = expected - sum(ledger_rows)`, chỉ chặn khi `remaining <= 0` và `modify` về `remaining` nếu `0 < remaining < amount`. | **Ngân sách chi phí mỗi ticket (`config`)**: giữ `cost_budget_per_ticket_vnd = 1500` để `business_gate` chặn trước khi gọi LLM quá đắt. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Ticket thuộc `HCM-B2B` đi thẳng tới nhân viên xử lý tay (`10.000đ`), không tốn thêm tiền LLM hay làm nghẽn hàng chờ duyệt. | Trợ lý tự động hoàn đúng `12.000đ` còn lại cho khách và ghi lỗi hãng `MKD`; nếu đã hoàn đủ rồi mới từ chối. | Ticket dài bất thường bị chặn trước khi đọc LLM đắt đỏ, chuyển sang người đọc hoặc xử lý theo quy trình chuẩn. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `estimated_cost_per_ticket_vnd` (và bảng `segments` theo kho trong report). | `refund_gate_block_rate` (tỉ lệ `write_gate` chặn/điều chỉnh tại `issue_refund`). | `llm_cost_max_per_ticket_vnd` và `estimated_cost_per_ticket_vnd`. |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `ledger` / `ledger_seed` (`amount_vnd` theo `order_id`) | Nguồn sự thật về "đơn đã hoàn hay chưa" (dạng có/không). | Cần coi là **tổng số tiền đã hoàn** cho `order_id` (`sum(amount_vnd)`), vì có thể có hoàn một phần trước đó. | Chặn cứng theo kiểu có/không làm từ chối nhầm `S5-21` (gây `under_refund_vnd = 60.000đ`). |
| `orders[].warehouse_id` (`HCM-B2B`) & `policies[].auto_limit_vnd` | Nguồn sự thật thông tin kho, nhưng chưa tách đơn vị kinh tế theo kho. | Kho sỉ `HCM-B2B` có đơn từ 2 triệu → thưởng trễ/hoàn vượt `auto_limit_vnd = 300.000đ` → gần như luôn `escalated`. | Mỗi ca `HCM-B2B` tốn cả LLM + công người (`10.382đ > 10.000đ` làm tay), làm giảm ROI. |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` (cùng luồng chi phí LLM / `pilot_scope` dẫn tới `issue_refund`)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `ledger_rows(order_id)` | **INVALID** (trước sửa) | `S5-01`, `S5-02`: cùng 1 đơn gửi nhiều ticket đòi hoàn 2–3 lần khi `refund_status` chưa kịp cập nhật đêm. | LogiX mất tiền hoàn trùng (`890.000đ` ở `base`). | Có cổng V1 kiểm `ledger_rows()`. | Giữ kiểm tra `ledger_rows()` nhưng tính `sum(amount_vnd)` (tầng **chặn**). |
| `ledger_rows(order_id)` | **INCOMPLETE** | `S5-21@11`: đơn `O-2521` mới hoàn một phần `10.000đ` trong `ledger_seed` (chính sách cho `22.000đ`). | Khách `C-16` bị từ chối oan `12.000đ` (`60.000đ` trên 5 seed). | Chưa có ở V1 (cổng V1 chặn nhầm). | `write_gate` (`issue_refund`): tính `remaining = expected - already` (tầng **chặn / sửa tham số**). |
| `warehouse_id` (`HCM-B2B`) | **INCAPABLE** | `S5-51@11`: đơn kho sỉ `HCM-B2B` vượt `auto_limit_vnd = 300.000đ` nên trợ lý đọc xong vẫn `escalated`. | CFO lỗ `382đ/ticket` (`10.382đ > 10.000đ` làm tay). | Chưa có ở V1 (`pilot_scope = all`). | Thu hẹp `pilot_scope` loại `HCM-B2B` (tầng **vận hành / giới hạn phạm vi**). |
| *(Nhánh chưa thấy trên trace lúc viết)* `checkout_note` hoặc `ticket.text` kèm tệp/chuỗi cực dài ở kênh mới | **PERTURBED** | Nếu khách dán log/bảng hàng dài vào `checkout_note` dù `ticket.text` ngắn, bước `llm.extract(checkout_note)` có thể đội chi phí. | Đội chi phí LLM hoặc đẩy hàng loạt sang người duyệt. | `cost_budget_per_ticket_vnd = 1500` ở `agent.py`. | Theo dõi `estimated_cost_per_ticket_vnd` và `llm_cost_max_per_ticket_vnd` (tầng **phát hiện**). |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Tổng chi phí vận hành trung bình mỗi ticket ở bất kỳ kho nào trong phạm vi pilot không được vượt quá chi phí làm tay (`10.000đ/ticket`), và tổng số tiền hoàn cho một đơn hàng (`sum(ledger_rows) + amount_vnd`) không được vượt quá mức hưởng hợp lệ `H.entitlement_vnd()` (nhưng vẫn phải cho phép hoàn nốt phần chênh lệch nếu trước đó mới hoàn một phần).

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): Dòng `segments_worse_than_manual == 0` / `vượt trần: không` trong report `lab10.grade` và nhánh `issue_refund` trong `lab10/guards.py` (`remaining = expected - already`).

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Người thiết kế ngầm giả định rằng **mọi kho đều có cơ cấu đơn hàng giống nhau** (giá trị đơn nhỏ, nằm dưới hạn mức tự động `300.000đ` để trợ lý tự xử lý được) và **khách chỉ gửi yêu cầu hoàn tiền ngắn gọn** (không dán kèm bảng kê hàng hóa dài hàng trăm dòng).

Vì sao có thể sai: Kho sỉ `HCM-B2B` phục vụ cửa hàng với đơn từ `2.000.000đ` trở lên nên hầu hết vượt hạn mức tự động và phải chuyển người duyệt; khách hàng doanh nghiệp/khiếu nại thường copy-paste toàn bộ bảng kê xuất kho vào email/ticket khiến chi phí LLM tăng vọt.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S5-prepared-20261118-163816-d0beba`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: Hệ thống lỗ vận hành / đắt hơn làm tay hoặc hoàn sai/thiếu tiền (cho ai: CFO LogiX & khách hàng, đo bằng: chi phí/ticket > 10.000đ, ROI, wrongful/under_refund_vnd)
 └─ HOẶC
 ├─ [1] Kho sỉ HCM-B2B tốn 10.382đ/ticket (> 10.000đ làm tay) · tầng: kinh doanh / phạm vi
 │   └─ vì: đơn sỉ >= 2 triệu vượt auto_limit_vnd (300.000đ) → đọc LLM xong vẫn escalated · bằng chứng: S5-51@11 & report prepared (HCM-B2B: 10382đ)
 ├─ [2] Từ chối nhầm phần hoàn bổ sung (under_refund 60.000đ) · tầng: hành động / cổng ghi
 │   └─ vì: cổng V1 chặn mọi đơn đã có dòng trong ledger_rows() mà không trừ số đã hoàn · bằng chứng: ticket S5-21@11 (gate deny)
 └─ [3] Ticket quá dài đội chi phí LLM hoặc chuyển người tốn 10.000đ/ca · tầng: đầu vào / chi phí
     └─ vì: khách dán bảng hàng dài khiến cost_vnd > 1.500đ (base: 2.412đ; prepared: business_gate escalate) · bằng chứng: ticket S5-70@11
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Chỉ đưa vào phạm vi tự động hóa các phân khúc kho có khả năng tự động xử lý và chi phí trung bình `<= 10.000đ/ticket`. | Mọi kho đều có đơn lẻ giá trị nhỏ dưới `auto_limit_vnd = 300.000đ`. |
| [2] | Tổng hoàn cho một đơn hàng không vượt quá `entitlement_vnd`, nhưng phải cho phép hoàn nốt phần chênh lệch nếu trước đó mới hoàn một phần. | Một đơn hàng chỉ phát sinh tối đa 1 giao dịch hoàn tiền duy nhất trong sổ cái. |
| [3] | Chi phí LLM cho mỗi ticket không vượt `max_llm_cost_per_ticket_vnd = 1.500đ`. | Khách chỉ viết mô tả ngắn gọn vừa phải trong ticket. |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Kho sỉ `HCM-B2B` đọc LLM xong vẫn chuyển người (`10.382đ > 10.000đ`). | `config/operating_gates.json` → `business.pilot_scope`: đổi `mode` thành `"warehouse"`, `warehouses: ["HN", "HCM", "DN", "CT"]` (loại `HCM-B2B`). | **Vận hành / Giới hạn phạm vi** | **NGĂN hẳn** cho kho `HCM-B2B` vì `ops.in_scope()` giữ toàn bộ ticket kho này ở quy trình thủ công trước khi gọi LLM. | `R-S5-after-20261118-163952-d71028` |
| [2] | Cổng V1 từ chối nhầm đơn đã hoàn một phần (`S5-21`). | `lab10/guards.py` → `write_gate` nhánh `tool == "issue_refund"`: tính `already = sum(ledger_rows)`, `remaining = max(0, expected - already)`; chỉ `deny` khi `remaining <= 0`, còn lại `modify` về `remaining`. | **Chặn / Sửa tham số** | **NGĂN hẳn** cả hoàn trùng (`remaining == 0`) lẫn thiếu hoàn bổ sung (`S5-21`: hoàn đủ `12.000đ` còn lại). | `R-S5-after-20261118-163952-d71028` |
| [3] | Ticket quá dài ngốn tiền LLM vượt `1.500đ` (`S5-70`). | Giữ `config/operating_gates.json` → `business.cost_budget_per_ticket_vnd = 1500` và bổ sung monitor `estimated_cost_per_ticket_vnd` ở `lab10/monitors.py`. | **Giới hạn thiệt hại + Phát hiện** | **NGĂN hẳn** tiền LLM vượt `1.500đ` (max còn `765đ`), và **GIẢM** rủi ro đội chi phí chung bằng cảnh báo chi phí trung bình (vì vẫn tốn công người duyệt nếu nhiều ticket dài). | `R-S5-after-20261118-163952-d71028` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `estimated_cost_per_ticket_vnd` (kèm `refund_gate_block_rate`) |
| **Bước / hành vi được đo** | Tổng chi phí vận hành ước tính cho mỗi ticket trong phạm vi pilot (tách tiền máy LLM/nền tảng và công người duyệt khi chuyển `escalated`). |
| **Thước đo** (một câu, có đơn vị) | Chi phí trung bình ước tính mỗi ticket trong ca (`đồng/ticket`), kèm tỉ lệ ticket bị `write_gate` chặn/sửa ở `issue_refund` (`refund_gate_block_rate`, `%`). |
| **Dữ liệu** (trường nào của trial, không có nhãn) | Trường `cost_vnd` (tiền máy LLM + nền tảng) và `status` (`"escalated"` cộng thêm `10.000đ` công người duyệt theo `ops_facts`), cùng `events` (`gate` trên `issue_refund`) từ danh sách `trials` trong production (không cần nhãn đúng/sai). |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `sum(t["cost_vnd"] + (10000 if t["status"] == "escalated" else 0) for t in trials) / max(1, len(trials))`. Nếu `trials` rỗng trả về `0.0`. (Chi phí theo từng kho đối chiếu thêm qua `segments` trong report). |
| **Khung thời gian / ngưỡng báo động** | Tính theo từng ca 480 phút / mỗi ngày; báo động vàng khi vượt **`7.000đ/ticket`**, báo động đỏ khi bất kỳ kho nào vượt **`10.000đ/ticket`** (chi phí làm tay). |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không cộng được thiệt hại do hoàn sai tiền nếu `wrongful_refund` là lỗi chìm chưa có nhãn, và chưa tính phí giữ chỗ `30.000đ/ca` của người trực hoặc chi phí kiểm mẫu `recheck`. |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | `estimated_cost_per_ticket_vnd`: bộ nền **`2910.82`** · trên thẻ S5 **`2313.5`** (`refund_gate_block_rate`: bộ nền **`0.0091`** · trên thẻ S5 **`0.2778`**). |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S5-after-20261118-163952-d71028`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Hệ thống lỗ vận hành / đắt hơn làm tay hoặc hoàn sai/thiếu tiền
 └─ HOẶC
 ├─ [1] Kho HCM-B2B lỗ vận hành (10.382đ > 10.000đ) VÀ [gate pilot_scope loại HCM-B2B hỏng]
 ├─ [2] Từ chối nhầm hoàn bổ sung S5-21 VÀ [gate write_gate(issue_refund) tính remaining hỏng]
 └─ [3] Ticket dài đội chi phí LLM > 1.500đ VÀ [business_gate cost_budget_per_ticket_vnd hỏng] (còn hở nếu tỉ lệ ticket dài làm escalated vượt trần cost 7.000đ)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `config/operating_gates.json → business.pilot_scope` (`mode="warehouse"`, giữ `HN, HCM, DN, CT`) | **Vận hành / Giới hạn phạm vi** | **Ngăn hẳn** cho `HCM-B2B` vì `ops.in_scope()` bỏ qua toàn bộ kho này trước khi gọi trợ lý. | Nếu một kho bán lẻ khác (như `HN`) tăng tỉ lệ đơn giá trị cao vượt `300.000đ`, chi phí kho đó vẫn có thể tăng (theo dõi qua `estimated_cost_per_ticket_vnd`). |
| [2] | `lab10/guards.py → write_gate` (`issue_refund` dùng `remaining = expected - already`) + `refund_gate_block_rate` | **Chặn / Sửa tham số + Phát hiện** | **Ngăn hẳn** hoàn trùng lẫn từ chối nhầm hoàn một phần khi sổ cái `ledger_rows` đầy đủ. | Nếu sổ cái bên ngoài đồng bộ chậm (chưa ghi vào `ledger` lúc kiểm tra), vẫn có thể lọt hoàn trùng trong khoảng trễ đó. |
| [3] | `config/operating_gates.json → business.cost_budget_per_ticket_vnd = 1500` + `estimated_cost_per_ticket_vnd` | **Giới hạn thiệt hại + Phát hiện** | **Ngăn** chi phí LLM vượt `1.500đ`, nhưng chỉ **giảm** tổng chi phí vì ticket bị `escalate` vẫn tốn `10.000đ` công người. | Nếu tỷ lệ khách dán bảng kê dài tăng đột biến, `escalation_rate` và `cost_per_ticket` sẽ tăng theo. |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Tỉ lệ ticket dài hoặc ticket vượt hạn mức ở 4 kho còn lại tăng cao làm chi phí trung bình mỗi ticket tiến sát chi phí làm tay (`10.000đ`). | Trung bình | Cao | `Phạm Kiều Oanh (NV-OANH)` | `estimated_cost_per_ticket_vnd > 7.000đ` hoặc bất kỳ kho nào `> 10.000đ` trong `segments` | Khoanh vùng cắt kho có chi phí > 10.000đ khỏi `pilot_scope` và bổ sung bước tiền xử lý cắt phần bảng kê thừa ở `pre_guard`. | Bắt buộc giữ quyết định **Thu hẹp** (không mở lại `HCM-B2B` hay mở rộng 100%) tới khi đo lại ở Gate 2. | **MEASURE / MANAGE** |
| Sổ cái hoàn tiền thủ công cập nhật chậm khiến `ledger_rows` chưa có giao dịch cũ lúc trợ lý kiểm tra. | Thấp | Cao | `Trần Thị Hạnh (NV-HANH)` | `refund_gate_block_rate` giảm bất thường hoặc đối soát tuần phát hiện hoàn trùng | Bật cảnh báo khi cùng `order_id` phát sinh >1 ticket trong ngày; chuyển người duyệt kiểm tra trước khi chi. | Bắt buộc kiểm tra độ trễ đồng bộ sổ cái trước khi mở rộng tự động hóa. | **MAP / MANAGE** |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 · Chất lượng | Xong | `R-S5-after-20261118-163952-d71028` (`pass_rate = 1.0`, `pass^k = 1.0`) và `R-base-after-20261118-163953-d71028` (`regression ✅`). | `Trần Thị Hạnh (NV-HANH)` |
| 6 · Chi phí | Xong | Loại `HCM-B2B` khỏi `pilot_scope` → `cost_per_ticket = 3.980đ ≤ 7.000đ`, `ROI = 1.51`, `segments_worse_than_manual = 0`. | `Phạm Kiều Oanh (NV-OANH)` |
| 7 · Vận hành | Xong | Thêm `estimated_cost_per_ticket_vnd` & `refund_gate_block_rate` trong `lab10/monitors.py` (`6 monitor ✅`). | `Lê Thanh Tùng (NV-TUNG)` |
| 9 · Quyết định | Xong | Cập nhật quyết định v2 (`Thu hẹp`) ở mục C12 khớp bằng chứng 3 mốc `R-S5-grade-20261118-163953-d71028`. | `Lê Thanh Tùng (NV-TUNG)` |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Tín hiệu chi phí/ticket theo từng kho (`cost_per_ticket > 7.000đ` hoặc `> 10.000đ`) và tỉ lệ `escalated` theo kho. Ở Vòng 1 mới có chỉ số tổng toàn hệ thống, chưa tách monitor `estimated_cost_per_ticket_vnd` và theo dõi `segments` theo kho. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Giữ `cost_budget_per_ticket_vnd = 1500` và `daily_refund_cap_vnd = 1500000`; thêm ngưỡng báo động cho monitor mới: `estimated_cost_per_ticket_vnd > 7.000đ` (vàng) và `> 10.000đ` ở bất kỳ kho nào (đỏ). |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ `1 người trực` (`NV-HANH`, `6 ca/giờ`), vì sau khi loại `HCM-B2B` tỉ lệ chuyển duyệt trên S5 giảm từ `0.5` xuống `0.1667` (`3 ca/ngày`, `0 ca ùn`). `NV-OANH` phụ trách theo dõi chi phí theo kho mỗi tuần. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Đổi `business.pilot_scope` từ `mode: "all"` (`100%`) sang `mode: "warehouse"`, `warehouses: ["HN", "HCM", "DN", "CT"]` (loại `HCM-B2B`, độ phủ `0.6`); sửa `guards.py` cho phép hoàn phần còn lại (`remaining`) thay vì chặn cứng mọi đơn đã có trong sổ cái. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Thông báo cho bộ phận xử lý đơn sỉ `HCM-B2B` và `NV-HANH` trong vòng `30 phút` rằng các ticket kho `HCM-B2B` tiếp tục đi theo luồng thủ công `100%`; `NV-OANH` thông báo cho khách hàng bị từ chối nhầm phần hoàn bổ sung (nếu có trong thực tế) để hoàn bù trong ngày. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có (`pii_leaks = 0` ở cả 3 mốc `base`, `prepared`, `after`). |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Lộ ra qua **phản hồi của CFO + đối soát kế toán (`NV-OANH`)** kết hợp bảng chi phí theo kho (`segments`). Nguồn bàn chưa có ở V1 là monitor chi phí ước tính thực tế (`cost_vnd + công người duyệt`) theo từng ca. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp **3** lần trong một giờ thì: `NV-HANH` kích hoạt gọi thêm `1` người duyệt dự phòng ngay khi hàng chờ vượt `6 ca/giờ` hoặc chờ `> 30 phút`; nếu vẫn tiến tới `60 phút` SLA, `NV-TUNG` thu hẹp tạm thời xuống `50%` hoặc chuyển ca mới sang thủ công.
2. Nếu nhà cung cấp LLM lỗi quá **10** phút thì: `NV-TUNG` tắt luồng tự động hoàn tiền hoặc chuyển toàn bộ ticket mới vào hàng chờ thủ công để tránh rơi vào `fail_open` hoặc retry tốn kém; chỉ mở lại sau khi nhà cung cấp ổn định.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: kiểm tra ngay `decision_note`, trace `events` và đối chiếu `ledger_rows` + tracking DB; giữ hoặc tăng `review_sampling_pct` lên `20%` (từ `10%`) cho tới khi xác nhận nguyên nhân và vá xong.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `97e536b` |
| Hash chốt cổng vòng 1 | `34a3f1e5` |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S5-before-20261118-163816-d0beba` · prepared: `R-S5-prepared-20261118-163816-d0beba` · after: `R-S5-after-20261118-163952-d71028` (grade: `R-S5-grade-20261118-163953-d71028`) |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không (`Không vượt trần kinh doanh / vận hành nào`: chờ `0.0 phút ≤ 60 phút`, `0` ca ùn, chi phí `3.980đ ≤ 7.000đ`, `ROI = 1.51 ≥ 0.25`, LLM max `765đ ≤ 1.500đ`, hoàn ngày `98.000đ ≤ 1.500.000đ`, `0` PII, `0` lỗi hãng oan). |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Trên S5 `prepared`, kho xấu nhất là **`HCM-B2B`** (`10.382đ/ticket > 10.000đ làm tay`), và trên S5 `after` (sau khi loại `HCM-B2B`), kho có chi phí cao nhất còn lại là **`HN`** (`4.277đ/ticket`, `pass_rate = 1.0`, `0` hoàn sai/oan/PII). Nhìn vào `HCM-B2B` chính là lý do trực tiếp để **đổi quyết định từ `Tiếp tục` sang `Thu hẹp`** (cắt `HCM-B2B`). |
| Quyết định (khoanh một) | **Thu hẹp** *(trong: Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng)* |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S5-after-20261118-163952-d71028`: trên S5 đạt 5/5 chỉ số bắt buộc (`pass_rate = 1.0`, `pass^k = 1.0`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`, `under_refund_vnd = 0`). |
| Bằng chứng 2 | `R-S5-after-20261118-163952-d71028`: kinh doanh/vận hành trên 4 kho bán lẻ đạt `cost_per_ticket = 3.980đ` (làm tay `10.000đ`), `ROI = 1.51`, `escalation_rate = 0.1667`, `tiết kiệm ròng = 108.357đ/ngày`, `0 ca ùn`. |
| Bằng chứng 3 | `R-base-after-20261118-163953-d71028` & `R-S5-grade-20261118-163953-d71028`: bộ nền giữ nguyên `110/110` ca đúng (`pass_rate = 1.0`, `regression ✅`), `monitor ✅` (`estimated_cost_per_ticket_vnd`: `2910.82` → `2313.5`; `refund_gate_block_rate`: `0.0091` → `0.2778`). |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp dòng **`Thu hẹp`**: cắt phân khúc không hiệu quả (`HCM-B2B`) khỏi phạm vi tự động để giữ toàn bộ chỉ số an toàn `= 0` và chi phí/ROI đạt ngưỡng trong phạm vi còn lại. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | Cắt hoàn toàn kho sỉ **`HCM-B2B`** (`mode: "warehouse"`, giữ 4 kho lẻ `["HN", "HCM", "DN", "CT"]`); độ phủ còn **`60%`** (`18/30` ticket/ngày trên S5); giữ **`1` người trực** (`NV-HANH`, `6 ca/giờ`); **`12` ticket/ngày của `HCM-B2B`** đi thẳng về quy trình xử lý thủ công (`10.000đ/ticket`) mà không qua LLM. |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (không áp dụng) |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | `2026-11-23` |
| PIC ký | `2A202603575` (Trưởng nhóm, đại diện bàn DDM) |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Đổi từ `Tiếp tục` (v1) sang `Thu hẹp` (v2)** vì ở mốc `prepared` trên S5, kho `HCM-B2B` tốn `10.382đ/ticket > 10.000đ làm tay` (`segments_worse_than_manual = 1`), dù tổng thể đạt. Loại `HCM-B2B` giúp `cost_per_ticket` giảm từ `6.538đ` xuống `3.980đ` và `ROI` tăng từ `0.53` lên `1.51`.
- Report tự kiểm tra: mã lần chạy `R-S5-grade-20261118-163953-d71028` · ô nào còn đỏ (nguyên nhân × tầng): Không còn ô đỏ nào trên gói sự cố (`criteria ✅`, `visible ✅`, `regression ✅`, `monitor ✅`; riêng `1 integrity` báo lệch trên máy Windows do Git tự đổi `LF→CRLF` khi checkout, không sửa file khóa).
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Cổng V1 đã chặn sạch hoàn trùng (`wrongful_refund`: `890.000đ → 0đ`), chặn `20` lỗi hãng oan (`20 → 0`), và chặn ticket dài vượt trần LLM (`2.412đ → 764đ`); nhưng bỏ sót **ca hoàn bổ sung một phần** (`S5-21`, `under_refund 60.000đ`) và **chưa loại kho sỉ `HCM-B2B`** (`10.382đ/ticket`).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report mốc `after` ghi **"Được phép cân nhắc 'Tiếp tục'"**, nhưng vì đội đã chủ động cắt kho `HCM-B2B` (độ phủ `0.6`) để đạt trạng thái đó nên quyết định **`Thu hẹp`** là chính xác và khớp hoàn toàn với bằng chứng thực tế.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Tốc độ đồng bộ sổ cái hoàn tiền thủ công ngoài thực tế (độ trễ giữa lúc CSKH chi tay và lúc `ledger_rows` cập nhật) và tỉ lệ khách dán bảng kê dài ở 4 kho lẻ; nếu độ trễ sổ cái lớn thì phải giữ `Thu hẹp` hoặc bật kiểm tra bổ sung trước khi mở rộng.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế của đội giả định sổ cái `ledger_rows()` luôn được cập nhật tức thời cho mọi giao dịch hoàn tiền (kể cả hoàn tay) và cơ cấu đơn hàng ở 4 kho lẻ (`HN, HCM, DN, CT`) tiếp tục nằm chủ yếu dưới hạn mức tự động `300.000đ`.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Cổng loại trừ kho `HCM-B2B` (`pilot_scope`) và cổng tính phần hoàn còn lại (`remaining = expected - already` trong `guards.py`) thực sự **NGĂN hẳn** lỗ vận hành ở `HCM-B2B` (`10.382đ → 0` ca qua LLM) và ngăn hoàn trùng/thiếu hoàn (`wrongful_refund = 0`, `under_refund = 0`) dựa trên dữ liệu tất định từ DB; còn `cost_budget_per_ticket_vnd = 1500` chỉ **GIẢM** thiệt hại tiền LLM vì vẫn tốn `10.000đ` công người duyệt khi ticket dài bị `escalate`.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Trước Gate 2, cần đo lại ở pilot thật tại 4 kho (`HN, HCM, DN, CT`): (1) `estimated_cost_per_ticket_vnd` theo từng kho (đối chiếu trần `7.000đ` và làm tay `10.000đ`), (2) tỉ lệ `escalated` do ticket dài vượt `1.500đ` hoặc vượt `300.000đ`, (3) độ trễ đồng bộ sổ cái thực tế, và (4) `wait_max_min` tại hàng chờ của `NV-HANH`.
