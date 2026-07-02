import json

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

Write ONE highly personalized recommendation.

Business Situation

Problem:
{recommendation["problem"]}

Goal:
{recommendation["goal"]}

Recommended Action:
{recommendation["recommended_action"]}

Tone:
{recommendation["tone"]}

Facts:

{chr(10).join("- " + x for x in recommendation["facts"])}

Evidence:

{json.dumps(evidence, indent=2)}

Rules:

- Never invent facts.
- Mention only evidence provided.
- Sound like an expert business advisor.
- Maximum 80 words.
- One CTA.
- Return ONLY JSON.

Return:

{{
    "body":"",
    "cta":"",
    "rationale":""
}}
"""

        response = self.llm.generate(prompt)

        response = response.strip()

        if response.startswith("```"):
            response = response.replace("```json", "")
            response = response.replace("```", "")

        return response.strip()