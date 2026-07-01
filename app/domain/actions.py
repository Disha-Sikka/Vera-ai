from pydantic import BaseModel


class Action(BaseModel):
    conversation_id: str

    merchant_id: str

    customer_id: str | None = None

    send_as: str

    trigger_id: str

    template_name: str

    template_params: list[str]

    body: str

    cta: str

    suppression_key: str

    rationale: str


class TickResponse(BaseModel):
    actions: list[Action]