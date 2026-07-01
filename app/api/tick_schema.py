from datetime import datetime

from pydantic import BaseModel


class TickRequest(BaseModel):
    now: datetime
    available_triggers: list[str]