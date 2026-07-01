from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ContextRecord(BaseModel):
    context_id: str

    version: int

    delivered_at: datetime

    payload: dict[str, Any] = Field(default_factory=dict)

    stored_at: datetime = Field(default_factory=datetime.utcnow)