from pydantic import BaseModel

from app.domain.enums import Strategy


class ScoreResult(BaseModel):
    strategy: Strategy
    score: float
    reasons: list[str]


class ScoringEngine:

    def calculate(self, context):

        return [
            ScoreResult(
                strategy=Strategy.INCREASE_FOOTFALL,
                score=50,
                reasons=[
                    "Default strategy."
                ],
            )
        ]