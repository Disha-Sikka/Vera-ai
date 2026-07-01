from app.domain.enums import Strategy
from app.domain.signals import ContextSignals
from pydantic import BaseModel


class ScoreResult(BaseModel):
    strategy: Strategy
    score: float
    reasons: list[str]


class ScoringEngine:

    def calculate(self, context: ContextSignals):

        results = []

        # Strategy 1
        score = 50
        reasons = []

        if context.merchant.sales_health == "declining":
            score += 30
            reasons.append("Sales are declining.")

        if context.merchant.offer_quality == "poor":
            score += 20
            reasons.append("Merchant has weak offers.")

        if context.trigger.seasonal:
            score += 10
            reasons.append("Seasonal opportunity.")

        results.append(
            ScoreResult(
                strategy=Strategy.INCREASE_FOOTFALL,
                score=score,
                reasons=reasons,
            )
        )

        # Strategy 2
        score = 40
        reasons = []

        if context.customer.is_repeat:
            score += 30
            reasons.append("Repeat customer.")

        if context.customer.days_since_last_visit > 30:
            score += 20
            reasons.append("Customer inactive.")

        results.append(
            ScoreResult(
                strategy=Strategy.RECALL_CUSTOMERS,
                score=score,
                reasons=reasons,
            )
        )

        return results