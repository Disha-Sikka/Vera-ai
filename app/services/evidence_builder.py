from typing import Any


class EvidenceBuilder:
    """
    Extracts only the useful information from the four contexts.
    """

    def build(
        self,
        category: dict[str, Any],
        merchant: dict[str, Any],
        trigger: dict[str, Any],
        customer: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        identity = merchant.get("identity", {})
        performance = merchant.get("performance", {})
        aggregate = merchant.get("customer_aggregate", {})
        offers = merchant.get("offers", [])

        evidence = {
            "merchant_name": identity.get("owner_first_name")
            or identity.get("name"),

            "business_name": identity.get("name"),

            "category": merchant.get("category_slug"),

            "city": identity.get("city"),

            "locality": identity.get("locality"),

            "trigger_kind": trigger.get("kind"),

            "trigger_payload": trigger.get("payload", {}),

            "merchant_signals": merchant.get("signals", []),

            "offers": offers,

            "performance": performance,

            "customer_aggregate": aggregate,

            "voice": category.get("voice", {}),

            "offer_catalog": category.get("offer_catalog", []),

            "digest": category.get("digest", []),

            "seasonal_beats": category.get("seasonal_beats", []),

            "trend_signals": category.get("trend_signals", []),

            "customer": customer or {},
        }

        return evidence