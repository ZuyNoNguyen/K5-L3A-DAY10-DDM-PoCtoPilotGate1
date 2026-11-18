"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
"""
from . import helpers as H
from .tools import Verdict


def _worst_parcel(order: dict, as_of: str) -> dict:
    """Trả về kiện có số ngày trễ theo tracking DB lớn nhất."""
    return max(order["parcels"], key=lambda p: H.db_delay_days(p, as_of))


def pre_guard(ctx):
    """Cổng 1: Ghim đúng phiên bản chính sách đang hiệu lực tại ngày as_of."""
    policies = ctx.tools.lookup_policies()
    pol = H.effective_policy(policies, ctx.as_of)
    if pol:
        ctx.log("pin_policy", policy_id=pol["policy_id"])
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    """Cổng 2 & 3: Kiểm soát các lệnh ghi dựa trên nguồn sự thật (DB & chính sách)."""
    tool = action.get("tool")
    policies = ctx.tools.lookup_policies()
    policy = H.effective_policy(policies, ctx.as_of)

    if tool == "issue_refund":
        order_id = action.get("order_id")
        if ctx.tools.ledger_rows(order_id=order_id):
            return Verdict.deny("đơn đã có giao dịch hoàn tiền trong sổ cái")

        order = ctx.tools.lookup_order(order_id)
        if order and policy:
            parcel = _worst_parcel(order, ctx.as_of)
            delay = H.db_delay_days(parcel, ctx.as_of)
            cause = parcel.get("delay_cause")
            expected = H.entitlement_vnd(policy, order, delay, cause)
            if expected <= 0:
                return Verdict.deny("không đủ điều kiện hoàn tiền theo tracking DB và chính sách")

            amount = action.get("amount_vnd", 0)
            payer = action.get("payer", "LOGIX")
            if amount > expected or payer != "LOGIX":
                return Verdict.modify(
                    "điều chỉnh mức hoàn và người trả đúng theo chính sách",
                    amount_vnd=expected,
                    payer="LOGIX",
                )

            cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
            if cap is not None and not action.get("approval_id"):
                spent = ctx.tools.auto_refund_today_vnd()
                if spent + amount > cap:
                    return Verdict.escalate("vượt trần hoàn tự động trong ngày, chuyển người duyệt")

    elif tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order and policy:
            parcel = _worst_parcel(order, ctx.as_of)
            delay = H.db_delay_days(parcel, ctx.as_of)
            if not H.carrier_at_fault(policy, parcel, delay):
                return Verdict.deny("không đủ điều kiện ghi lỗi hãng theo tracking DB và chính sách")
            if (
                action.get("delay_days") != delay
                or action.get("parcel_id") != parcel["parcel_id"]
                or action.get("carrier_id") != parcel["carrier_id"]
            ):
                return Verdict.modify(
                    "chuẩn hóa kiện và số ngày trễ theo tracking DB",
                    parcel_id=parcel["parcel_id"],
                    carrier_id=parcel["carrier_id"],
                    driver_id=parcel.get("driver_id"),
                    delay_days=delay,
                )

    elif tool == "notify_carrier":
        blocked = set((ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
        payload = dict(action.get("payload") or {})
        removed = [k for k in list(payload.keys()) if k in blocked or k == "recipient_contact"]
        if removed:
            for k in removed:
                payload.pop(k, None)
            return Verdict.modify("loại bỏ trường PII trước khi gửi hãng", payload=payload)

    return Verdict.allow()
