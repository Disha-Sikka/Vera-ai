from typing import Any

from pydantic import BaseModel, Field

from app.domain.enums import (
    Category,
    Priority,
    Sender,
    Strategy,
)


class Merchant(BaseModel):
    """
    Represents a merchant in the business domain.
    """

    id: str = Field(..., description="Unique merchant identifier")
    name: str
    category: Category

    # Raw merchant information received from the challenge.
    raw_data: dict[str, Any] = Field(default_factory=dict)


class Customer(BaseModel):
    """
    Represents a customer in the business domain.
    """

    id: str

    # Raw customer information.
    raw_data: dict[str, Any] = Field(default_factory=dict)


class Trigger(BaseModel):
    """
    Represents an event that may require action.
    """

    id: str

    # Keep this as string because new trigger types may appear.
    type: str

    # Raw trigger payload.
    raw_data: dict[str, Any] = Field(default_factory=dict)


class ComposeResponse(BaseModel):
    """
    Final response returned to the challenge evaluator.
    """

    sender: Sender

    message: str

    cta: str

    suppression_key: str

    rationale: str