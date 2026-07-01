from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class ContextRequest(BaseModel):
    scope: Literal[
        "category",
        "merchant",
        "customer",
        "trigger",
    ]

    context_id: str

    version: int = Field(ge=1)

    delivered_at: datetime

    payload: dict[str, Any]


class ContextResponse(BaseModel):
    accepted: bool

    ack_id: str | None = None

    stored_at: datetime | None = None

    reason: str | None = None

    current_version: int | None = None