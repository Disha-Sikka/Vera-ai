import json

from app.services.llm_provider import LLMProvider


class Composer:

    def __init__(self):
        self.llm = LLMProvider()

    def compose(self, evidence: dict):

        prompt = f"""
You are Vera, Magicpin's AI growth assistant.

Use ONLY the provided evidence.

Write ONE highly personalized message.

Rules:
- Never invent facts.
- Use merchant name.
- Use trigger.
- Use category voice.
- Mention research source if available.
- Keep under 120 words.
- No URLs.
- JSON only.

Evidence:

{json.dumps(evidence, indent=2)}

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
            response = response.split("```")[1]

        response = response.replace("json", "", 1).strip()

        return response