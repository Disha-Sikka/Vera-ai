from pydantic import BaseModel


class MerchantSignals(BaseModel):
    sales_health: str = "unknown"
    offer_quality: str = "unknown"
    profile_health: str = "unknown"
    review_health: str = "unknown"
    repeat_customer_rate: float = 0.0
    campaign_health: str = "unknown"


class TriggerSignals(BaseModel):
    urgency: str = "medium"
    seasonal: bool = False
    research_based: bool = False


class CustomerSignals(BaseModel):
    is_repeat: bool = False
    days_since_last_visit: int = 0
    consent: bool = False


class ContextSignals(BaseModel):
    merchant: MerchantSignals
    trigger: TriggerSignals
    customer: CustomerSignals