from app.services.llm_provider import LLMProvider
from app.services.recommendation_builder import RecommendationBuilder


class Composer:

    def __init__(self):
        self.llm = LLMProvider()
        self.recommender = RecommendationBuilder()

    def compose(self, evidence: dict):

        recommendation = self.recommender.build(evidence)

        prompt = f"""
You are Vera, Magicpin's AI Growth Assistant.

Write ONE short personalized recommendation.

Business:
{evidence.get("business_name","")}

Category:
{evidence.get("category","")}

Problem:
{recommendation["problem"]}

Goal:
{recommendation["goal"]}

Recommended Action:
{recommendation["recommended_action"]}

Facts:
{chr(10).join("- " + x for x in recommendation["facts"])}

Rules:
- Never invent facts.
- Maximum 60 words.
- One CTA.
- Return ONLY valid JSON.

Return:

{{
"body":"",
"cta":"open_ended",
"rationale":""
}}
"""

        response = self.llm.generate(prompt).strip()

        if response.startswith("```"):
            response = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return response