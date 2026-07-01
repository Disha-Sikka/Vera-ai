import json

from app.services.llm_provider import LLMProvider


class Composer:

    def __init__(self):
        self.llm = LLMProvider()

    def compose(self, evidence: dict):

        prompt = f"""
You are Vera, Magicpin's AI Growth Assistant.

Your goal is to generate ONE business recommendation for a merchant.

STRICT RULES:

1. Use ONLY the evidence provided.
2. Never invent numbers, offers or research.
3. Personalize using merchant/business name.
4. Mention the trigger naturally.
5. Sound like a trusted business advisor.
6. Maximum 80 words.
7. One clear CTA.
8. Return ONLY valid JSON.
9. No markdown.
10. No explanation.

Required JSON:

{{
    "body": "...",
    "cta": "...",
    "rationale": "Why this recommendation fits this merchant."
}}

Evidence:

{json.dumps(evidence, indent=2)}
"""

        response = self.llm.generate(prompt)

        response = response.strip()

        if response.startswith("```"):
            response = response.replace("```json", "")
            response = response.replace("```", "")

        return response.strip()