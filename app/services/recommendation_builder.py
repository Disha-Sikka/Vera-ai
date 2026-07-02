from typing import Any


class RecommendationBuilder:
    """
    Converts raw evidence into a business recommendation.
    """

    def build(self, evidence: dict[str, Any]) -> dict[str, Any]:

        category = str(evidence.get("category", "")).lower()

        recommendation = {
            "problem": "",
            "goal": "",
            "recommended_action": "",
            "facts": [],
            "tone": "",
        }

        if "restaurant" in category:
            recommendation["goal"] = "Increase table bookings and repeat customers."
            recommendation["tone"] = "friendly, energetic, food-focused"

        elif "salon" in category:
            recommendation["goal"] = "Increase repeat appointments."
            recommendation["tone"] = "premium, beauty-focused"

        elif "dent" in category:
            recommendation["goal"] = "Increase patient visits and trust."
            recommendation["tone"] = "professional, trustworthy"

        elif "gym" in category:
            recommendation["goal"] = "Increase memberships and retention."
            recommendation["tone"] = "motivational"

        elif "pharmacy" in category:
            recommendation["goal"] = "Increase customer trust and repeat purchases."
            recommendation["tone"] = "professional"

        else:
            recommendation["goal"] = "Help merchant grow."

        trigger = str(evidence.get("trigger_type", "")).lower()

        if "research" in trigger:
            recommendation["problem"] = "A new research insight may help this business."
            recommendation["recommended_action"] = "Share the research and explain how to use it."

        elif "repeat" in trigger:
            recommendation["problem"] = "Repeat customer rate is low."
            recommendation["recommended_action"] = "Recommend a loyalty campaign."

        elif "offer" in trigger:
            recommendation["problem"] = "Merchant is missing an attractive offer."
            recommendation["recommended_action"] = "Recommend launching a limited-time offer."

        else:
            recommendation["problem"] = "Business growth opportunity detected."
            recommendation["recommended_action"] = "Provide practical next steps."

        recommendation["facts"] = [
            f"Business: {evidence.get('business_name','')}",
            f"Category: {evidence.get('category','')}",
            f"City: {evidence.get('city','')}",
        ]

        for signal in evidence.get("signals", []):
            recommendation["facts"].append(signal)

        return recommendation