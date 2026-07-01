from app.domain.decision_models import DecisionPlan


class PromptBuilder:

    def build(self, decision: DecisionPlan):

        return f"""
You are Vera, Magicpin's AI growth assistant.

Business Strategy:
{decision.strategy.value}

Priority:
{decision.priority.value}

Reasons:
{chr(10).join(decision.reasoning)}

CTA:
{decision.cta}

Generate JSON only.

{{
    "message": "...",
    "cta": "...",
    "sender": "{decision.sender.value}",
    "suppression_key": "...",
    "rationale": "..."
}}
"""