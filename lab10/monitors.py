"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def estimated_cost_per_ticket_vnd(trials):
    """Chi phí ước tính mỗi ticket (tiền LLM/nền tảng + công người duyệt nếu escalated)."""
    if not trials:
        return 0.0
    total = sum(
        t.get("cost_vnd", 0) + (10000 if t.get("status") == "escalated" else 0)
        for t in trials
    )
    return round(total / len(trials), 2)


def refund_gate_block_rate(trials):
    """Tỉ lệ trial phát sinh chặn/điều chỉnh ở cổng issue_refund (phát hiện hoàn trùng hoặc hoàn lố)."""
    if not trials:
        return 0.0
    hits = sum(
        any(
            e.get("type") == "gate"
            and e.get("tool") == "issue_refund"
            and e.get("action") in ("deny", "modify")
            for e in t.get("events", [])
        )
        for t in trials
    )
    return round(hits / len(trials), 4)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "estimated_cost_per_ticket_vnd": estimated_cost_per_ticket_vnd,
    "refund_gate_block_rate": refund_gate_block_rate,
}
STARTER_MONITORS = ("escalation_rate",)
