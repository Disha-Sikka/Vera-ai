from app.domain.decision_models import DecisionPlan
from app.domain.enums import Priority, Sender, Strategy
from app.services.scoring import ScoringEngine


class DecisionEngine:

    def __init__(self):
        self.scorer = ScoringEngine()

    def decide(self, context):

        results = self.scorer.calculate(context)

        best = max(results, key=lambda x: x.score)

        return DecisionPlan(
            strategy=best.strategy,
            priority=Priority.MEDIUM,
            sender=Sender.VERA,
            cta="Open Dashboard",
            score=best.score,
            confidence=0.80,
            reasoning=best.reasons,)
