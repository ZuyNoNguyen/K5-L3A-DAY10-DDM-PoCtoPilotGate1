# Kế Hoạch Chia Việc Song Song · Nhóm 3 Người (LAB 10: From PoC to Pilot · Gate 1)

> **Mục tiêu:** Tối đa hóa tốc độ làm việc song song để từng thành viên **không bị chờ tiến độ của nhau** và **không gây xung đột (conflict) Git** khi cùng làm trên repo `K5-L3A-DAY10-DDM-PoCtoPilotGate1`.

---

## 1. Bốn luật sống còn (vi phạm là mất điểm / không qua)

1. **Ký tiêu chí trước khi đo:** `config/acceptance_criteria.json` phải điền xong, ký (`python3 -m lab10.criteria sign`), commit và push **trước** lần chạy `eval` / `grade` đầu tiên. **Tuyệt đối không sửa file này sau khi ký.**
2. **Giữ nguyên file khóa & bản chốt vòng 1:** Không sửa các file hệ thống bị khóa hash, và sau khi chạy `python3 -m lab10.checkpoint` ở phút 105–115, không sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
3. **Không phá ca đang đúng & không hardcode:** Phải đạt `regression ✅` (ca trước đúng thì sau vẫn phải đúng). Không chặn hết, không thu hẹp pilot về `0%`, không xử lý riêng theo mã ticket hay câu chữ cụ thể (vì có bộ test ẩn chấm sau buổi).
4. **Quyết định v2 khớp bằng chứng:** Chọn `Tiếp tục` khi report còn dòng vượt trần hoặc chưa đạt ngưỡng đã ký là **không qua**. Cuối buổi `python3 -m lab10.check_submission --collect` phải in `ĐỦ THÀNH PHẦN`, và **mỗi thành viên** phải tự nộp link repo lên LMS.

---

## 2. Phân vai & Quyền sở hữu file (File Ownership)

| Vai trò | Thành viên | File sở hữu chính | Quyền sửa |
|---|---|---|---|
| **1. Kỹ sư cổng** *(Gate Engineer)* | *(Điền tên)* | `lab10/guards.py`, `lab10/monitors.py` | Độc quyền sửa code & chạy các lệnh CLI (`eval`, `trace`, `gate`, `checkpoint`, `grade`) |
| **2. Sản phẩm & Kinh doanh** *(PM / Biz)* | *(Điền tên)* | `config/acceptance_criteria.json`, khối `business` trong `config/operating_gates.json` | Độc quyền `acceptance_criteria.json`; gửi 4 số `business` cho Ops dán vào `operating_gates.json` |
| **3. Vận hành & Pháp lý** *(Ops / Legal)* | *(Điền tên)* | Khối `operations` & `legal` trong `config/operating_gates.json`, `submission/submission.json` | Giữ file `operating_gates.json` (dán cả phần `business` từ PM), quản lý checklist, runbook, `check_submission` |

### Quy tắc chống conflict khi sửa file dùng chung
- **`config/operating_gates.json`:** Chỉ **Ops/Legal** sửa trực tiếp trên Git. **PM/Biz** tính xong 4 thông số `business` thì gửi JSON/con số qua chat để Ops/Legal dán vào cùng một commit.
- **3 phiếu (`templates/form-a-criteria.md`, `form-b-evaluation-gates.md`, `form-c-incident.md`):** Mỗi người chỉ điền đúng các mục/câu được phân công dưới đây; không sửa chéo sang ô của người khác.
- **`TEAM.md`:** Đầu buổi điền chung bảng thành viên; cuối buổi mỗi người tự điền mục `## HoVaTen-MSSV` của mình (hoặc gửi text cho 1 người ghép vào để tránh conflict).

---

## 3. Lịch làm việc song song theo từng chặng (Phút 0–240)

### Chặng 0 · Phút 0–15: Cài đặt & chia vai
- [ ] **Kỹ sư cổng:** Chạy `git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git` (hiện tại repo chưa có `upstream`), chạy `python3 -m unittest discover -s tests` (đảm bảo `Ran 13 tests ... OK`), đọc trước `lab10/helpers.py`, `lab10/tools.py`, `docs/guide.md`.
- [ ] **PM / Kinh doanh:** Mở eval card & PRD v1.1 từ Lab 9, đọc `data/world.json` mục `ops_facts` và `ops_limits`.
- [ ] **Vận hành & Pháp lý:** Điền bảng thành viên trong `TEAM.md`, cấu hình `git config user.name/email` theo đúng hướng dẫn, điền sẵn khung `submission/submission.json` (`team`, `members` dạng `"HoVaTen-MSSV"`), kiểm tra đã mời tài khoản team chấm quyền Read trên GitHub.

---

### Chặng 1 · Phút 15–65: Khối 1 – Tiêu chí & Ký (Phiếu A)
> Chặng này **chưa được chạy `eval`**. Kỹ sư cổng làm độc lập câu 1.3 và đọc code chuẩn bị cổng, không ngồi đợi PM/Biz.

| Thành viên | Việc làm song song (Phút 15–60) |
|---|---|
| **Kỹ sư cổng** | - Điền **Câu 1.3** (Phiếu A, mục A2 cột *Offline*): chọn 1 bước của agent, thiết kế Thước đo → Dữ liệu → Cách tính.<br>- Đọc `data/world.json`, `data/tickets.jsonl`, `lab10/helpers.py` và phác sẵn logic các cổng dự kiến trong nháp để sang phút 85 code ngay. |
| **PM / Kinh doanh** | - Điền **Câu 1.1** (mục A1) và **Câu 1.6** (mục A4: câu *"Nếu… thì chúng tôi sẽ…"*, 4 câu soát, 2 câu ranh giới đầu ra).<br>- Điền đầy đủ `config/acceptance_criteria.json` (`team = "K5-L3A-DAY10-DDM-PoCtoPilotGate1"`, `signed_by`, `required`, `nice_to_have`, `business_ops`, `stop_condition`, `decision_rule`). |
| **Vận hành & Pháp lý** | - Điền **Câu 1.2** (mục A1: góc nhìn chị Oanh & chị Hạnh từ `world.json → staff`) và **Câu 1.4** (mục A2 cột *Telemetry production*).<br>- Soát **Câu 1.5** (mục A3) trước để bàn chốt nhanh. |

- **SYNC 1 (Phút 60–65):** Cả bàn chốt Câu 1.5 + rà `config/acceptance_criteria.json` lần cuối → chạy:
  ```bash
  python3 -m lab10.criteria sign
  git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m "Sign acceptance criteria" && git push -u origin main
  ```
  → Điền mục **A5** (giờ ký, mã commit) vào Phiếu A.

---

### Chặng 2A · Phút 65–85: Đo base & Tìm rủi ro (Phiếu B · B0–B6)
> 10 phút đầu (65–75) **3 người làm hoàn toàn độc lập**, không cần chờ số liệu của nhau.

| Thành viên | Việc làm song song (Phút 65–75) |
|---|---|
| **Kỹ sư cổng** | Chạy `eval --suite base --stage base --note "baseline"`, `gate`, và `trace --suite base --ticket T-002 --seed 55`. Điền **Câu 2.1** (B0, B1) và **Câu 2.2** (B2 bảng soát lỗi). |
| **PM / Kinh doanh** | Mở `data/world.json` điền **Câu 2.3** (Phiếu B, mục B3: bản đồ dữ liệu + 1 ví dụ drift cụ thể trong 3 tháng tới). |
| **Vận hành & Pháp lý** | Điền **Câu 2.4**: Phiếu B mục B4 (HAZOP vòng 1: ≥ 3 dòng + ≥ 2 dòng ngoài kỹ thuật) và mục B5 (Checklist 9 nhóm việc lần 1, mỗi dòng có PIC gắn tên cụ thể). |

- **SYNC 2 (Phút 75–85):** Cả bàn họp 8–10 phút hoàn thành **Câu 2.5** (mục B6: Pre-mortem 4 lăng kính) và **chốt 2–3 lý do sẽ biến thành cổng** ở Chặng 2B.

---

### Chặng 2B & Chốt v1 · Phút 85–115: Dựng cổng vòng 1 & Quyết định v1 (Phiếu B · B7–B8)

| Thành viên | Việc làm song song (Phút 85–105) |
|---|---|
| **Kỹ sư cổng** | - Code 2–3 cổng trong `lab10/guards.py` (**Câu 2.6** / B7.1).<br>- Viết **Câu 2.7** (B7.2: 2 bước tránh rò rỉ dữ liệu).<br>- Chạy `eval --suite base --stage after`, `unittest`, và thử 2 ticket hiểm bằng `--adhoc` (**Câu 2.8** / B7.3). |
| **PM / Kinh doanh** | - Tính 4 con số `business` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`) từ `world.json → ops_limits, ops_facts`.<br>- Điền **Câu 2.9** (B7.4: lý do từng số) và gửi 4 con số này cho Ops/Legal.<br>- Soạn sẵn khung lập luận cho **Quyết định v1** (B8). |
| **Vận hành & Pháp lý** | - Dán khối `business` (từ PM) và điền khối `operations`, `legal` vào `config/operating_gates.json`.<br>- Viết **Câu 2.10**: Runbook phần 1–3 (B7.5) và mục **Giờ cao điểm** (B7.6) khớp đúng con số trong config. |

- **SYNC 3 (Phút 105–115):**
  1. Pull bản mới nhất từ mọi người → Kỹ sư cổng chạy:
     ```bash
     python3 -m lab10.checkpoint
     python3 -m lab10.eval --suite base --stage prepared
     python3 -m lab10.gate --run runs/<mã_lần_chạy>/report.json
     ```
  2. PM/Biz điền cột **v1** ở mục **B8** (kèm 3 dòng bằng chứng có mã chạy từ Kỹ sư cổng) → commit & push toàn bộ vòng 1.

---

### Chặng 3 · Phút 125–200: Khối 3 – Sự cố, Sửa & Quyết định v2 (Phiếu C)

#### Phút 125–135 · Nhận thẻ & đo `prepared`
- **Kỹ sư cổng:** Chờ Lab Coach báo phát thẻ → kéo thẻ về:
  ```bash
  git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main
  python3 -m lab10.grade --incident Sx
  ```
- **Ops / Legal:** Ghi số thẻ vào dòng `Thẻ đã bốc:` ở đầu Phiếu C và trường `incident` trong `submission/submission.json`.
- **Cả bàn:** Nhìn bảng `prepared` vừa in ra, điền nhanh **Câu 3.0** (C0, C1).

#### Phút 135–155 · Phân tích song song (Câu 3.1–3.4)
| Thành viên | Việc làm song song (Phút 135–149) |
|---|---|
| **Kỹ sư cổng** | Chạy `trace --suite Sx --ticket ... --seed 11` dò ≥ 2 ticket hỏng theo hai kiểu khác nhau → điền **C2** (bảng soát lỗi & tác hại). |
| **PM / Kinh doanh** | Đọc `incidents/Sx/card.md` + report `prepared` → viết **Câu 3.2** (C5: 1 specification kiểm được bằng code hoặc con số). |
| **Vận hành & Pháp lý** | Điền **C3** (phần riêng theo thẻ, bỏ qua nếu bốc S4), **C4** (HAZOP của thẻ ≥ 3 dòng), và **Câu 3.3** (C5: 1 giả định môi trường). |

- *Phút 149–155:* Cả bàn ghép nhanh bằng chứng từ 3 người vào **Câu 3.4** (C6: Fault tree trước khi sửa, ít nhất 2 nhánh ở 2 tầng khác nhau).

#### Phút 155–185 · Sửa song song & cập nhật hồ sơ (Câu 3.5–3.7)
| Thành viên | Việc làm song song (Phút 155–180) |
|---|---|
| **Kỹ sư cổng** | - Sửa nhánh kỹ thuật trong `lab10/guards.py`.<br>- Thêm ít nhất 1 hàm monitor mới vào `lab10/monitors.py` và đăng ký vào `MONITORS`.<br>- Chạy `eval --suite Sx --stage after`, `eval --suite base --stage after`, và `grade --incident Sx`.<br>- Điền **C8** (3 ô của chỉ số theo dõi mới). |
| **PM / Kinh doanh** | - Quyết định điều chỉnh khối `business` (`pilot_scope`, trần…) nếu thẻ có nguyên nhân kinh doanh, gửi cho Ops dán vào `operating_gates.json`.<br>- Điền **C7** (bảng sửa: nêu rõ biện pháp *giảm khả năng* hay *ngăn hẳn*).<br>- Chuẩn bị sẵn **C12** (Quyết định v2 + 3 dòng bắt buộc). |
| **Vận hành & Pháp lý** | - Cập nhật `operations` & `legal` (và `business` nếu có) trong `config/operating_gates.json`.<br>- Điền **C9** (Fault tree sau sửa), **C10** (≥ 1 dòng Risk register), **C11** (cập nhật Checklist PIC + Runbook phần 4–5). |

- **SYNC 4 (Phút 185–200):**
  1. Chạy lại `python3 -m lab10.grade --incident Sx` trên code & config đã ghép xong.
  2. PM/Biz điền **C12** (v2 + 3 dòng bắt buộc).
  3. Ops/Legal chép 3 dòng bắt buộc vào `submission/submission.json`, chạy `python3 -m lab10.check_submission --collect` và sửa các dòng `[THIẾU]` (nếu có) tới khi in `ĐỦ THÀNH PHẦN`.

---

### Chặng 4 · Phút 200–240: Demo & Nộp bài
- **Phút 200–230 (Demo):**
  - Kỹ sư cổng: chiếu 3 cột `base · prepared · after`, chạy demo `--adhoc` hoặc đổi thử số theo yêu cầu bàn phản biện.
  - PM / Kinh doanh: trình bày quyết định v2 và con số kinh doanh đỡ cho quyết định đó.
  - Vận hành & Pháp lý: trình bày cổng con người, số người trực, runbook và tác động lên hàng chờ.
- **Phút 230–240 (Chốt bài nộp):**
  - Nếu lúc demo có đổi thử số trong `config/operating_gates.json`, **bắt buộc trả về bản v2**, rồi Kỹ sư cổng chạy lại `python3 -m lab10.grade --incident Sx` và `python3 -m lab10.check_submission --collect`.
  - **Cả 3 thành viên** hoàn thiện mục cá nhân `## HoVaTen-MSSV` trong `TEAM.md` (gồm cả Exit ticket).
  - Push lần cuối:
    ```bash
    git add -u && git add submission templates TEAM.md
    git commit -m "LAB 10: bài nộp"
    git push -u origin main
    ```
  - **Mỗi thành viên tự nộp link repo** (`https://github.com/ZuyNoNguyen/K5-L3A-DAY10-DDM-PoCtoPilotGate1`) lên LMS trước deadline.

---

## 4. Mẹo Git để không đụng nhau
- **Mỗi người làm trên 1 nhánh riêng** (`feat/gate-eng`, `feat/biz`, `feat/ops`) và chỉ merge vào `main` ở **4 mốc Sync** (phút 60, 80, 105, 185).
- **Hoặc nếu làm chung trực tiếp trên `main`:** Luôn chạy `git pull --rebase` trước khi push, và tuân thủ tuyệt đối bảng **File Ownership** ở mục 2 (không ai sửa file của người khác).
- **Chỉ Kỹ sư cổng chạy `eval` / `grade`** sau khi đã pull đủ config mới nhất, để `runs/journal.jsonl` sạch và phản ánh đúng trạng thái từng mốc.
