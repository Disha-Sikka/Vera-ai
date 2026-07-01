from enum import Enum


class Category(str, Enum):
    """Supported merchant categories."""

    RESTAURANT = "restaurant"
    SALON = "salon"
    CLINIC = "clinic"
    RETAIL = "retail"
    OTHER = "other"


class Strategy(str, Enum):
    """Business strategies selected by the decision engine."""

    INCREASE_FOOTFALL = "increase_footfall"
    RECALL_CUSTOMERS = "recall_customers"
    PROMOTE_EXISTING_OFFER = "promote_existing_offer"
    CREATE_NEW_OFFER = "create_new_offer"
    PROMOTE_BESTSELLER = "promote_bestseller"
    FESTIVAL_CAMPAIGN = "festival_campaign"
    IMPROVE_PROFILE = "improve_profile"
    CELEBRATE_SUCCESS = "celebrate_success"


class Priority(str, Enum):
    """Decision priority."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Sender(str, Enum):
    """Identity that sends the message."""

    VERA = "vera"
    MAGICPIN = "magicpin"
    SYSTEM = "system"


class ConversationStatus(str, Enum):
    """Conversation lifecycle."""

    ACTIVE = "active"
    PAUSED = "paused"
    CLOSED = "closed"