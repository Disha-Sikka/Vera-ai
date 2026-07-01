from app.domain.decision_models import DecisionPlan
from app.domain.enums import Priority, Sender
from app.services.context_builder import ContextBuilder
from app.services.scoring import ScoringEngine


class DecisionEngine:

    def __init__(self):
        self.builder = ContextBuilder()
        self.scorer = ScoringEngine()

    def decide(self, merchant, trigger, customer):

        context = self.builder.build(
            merchant,
            trigger,
            customer,
        )

        results = self.scorer.calculate(context)

        best = max(results, key=lambda x: x.score)

        confidence = min(best.score / 100, 1.0)

        return DecisionPlan(
            strategy=best.strategy,
            priority=Priority.HIGH if best.score >= 70 else Priority.MEDIUM,
            sender=Sender.VERA,
            cta="View Recommendation",
            score=best.score,
            confidence=confidence,
            reasoning=best.reasons,
        )