from typing import Any


class RecommendationBuilder:
    """
    Converts raw evidence into a business recommendation.
    """

    def build(self, evidence: dict[str, Any]) -> dict[str, Any]:

        recommendation = {
            "problem": "",
            "goal": "",
            "recommended_action": "",
            "facts": [],
        }

        trigger = evidence.get("trigger_type", "")

        if trigger == "research_digest":
            recommendation["problem"] = "Merchant may be missing an important business opportunity."
            recommendation["goal"] = "Help the merchant act on recent industry research."
            recommendation["recommended_action"] = "Share a concise recommendation based on the research."

        elif trigger == "low_repeat_customers":
            recommendation["problem"] = "Customer retention is low."
            recommendation["goal"] = "Increase repeat visits."
            recommendation["recommended_action"] = "Launch a repeat customer campaign."

        elif trigger == "inactive_offer":
            recommendation["problem"] = "No attractive offer is currently running."
            recommendation["goal"] = "Increase footfall."
            recommendation["recommended_action"] = "Create a limited-time promotional offer."

        else:
            recommendation["problem"] = "Business growth opportunity detected."
            recommendation["goal"] = "Increase merchant performance."
            recommendation["recommended_action"] = "Provide a personalized recommendation."

        recommendation["facts"].append(
            f"Merchant: {evidence.get('business_name','')}"
        )

        recommendation["facts"].append(
            f"Category: {evidence.get('category','')}"
        )

        recommendation["facts"].append(
            f"City: {evidence.get('city','')}"
        )

        signals = evidence.get("signals", [])

        if signals:
            recommendation["facts"].append(
                "Signals: " + ", ".join(signals)
            )

        return recommendation