from datetime import datetime

from pydantic import BaseModel


class ReplyRequest(BaseModel):
    conversation_id: str
    merchant_id: str
    customer_id: str | None = None
    from_role: str
    message: str
    received_at: datetime
    turn_number: int


class ReplyResponse(BaseModel):
    action: str
    body: str | None = None
    cta: str | None = None
    rationale: str
    wait_seconds: int | None = None