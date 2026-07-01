from app.domain.models import Decision
from app.domain.enums import Priority, Strategy


class DecisionEngine:

    def decide(self, context):
        """
        Placeholder implementation.
        """

        return Decision(
            strategy=Strategy.INCREASE_FOOTFALL,
            priority=Priority.MEDIUM,
            score=50,
            confidence=0.80,
            reasoning=[
                "Initial placeholder strategy."
            ]
        )