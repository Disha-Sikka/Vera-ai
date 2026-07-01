from typing import Any


class EvidenceBuilder:

    def build(
        self,
        category: dict[str, Any],
        merchant: dict[str, Any],
        trigger: dict[str, Any],
        customer: dict[str, Any] | None = None,
    ):

        identity = merchant.get("identity", {})
        perf = merchant.get("performance", {})
        agg = merchant.get("customer_aggregate", {})

        return {
            "merchant_name": identity.get("owner_first_name", ""),
            "business_name": identity.get("name", ""),
            "category": merchant.get("category_slug", ""),
            "city": identity.get("city", ""),
            "locality": identity.get("locality", ""),

            "sales": perf,
            "customer_stats": agg,
            "offers": merchant.get("offers", []),
            "signals": merchant.get("signals", []),

            "trigger_type": trigger.get("kind"),
            "trigger_payload": trigger.get("payload", {}),

            "voice": category.get("voice", {}),
            "digest": category.get("digest", []),
            "seasonal_beats": category.get("seasonal_beats", []),
            "trend_signals": category.get("trend_signals", []),

            "customer": customer or {},
        }