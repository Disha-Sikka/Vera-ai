from datetime import datetime
from fastapi import HTTPException
from fastapi import APIRouter
from app.api.schemas import ContextRequest, ContextResponse
from app.domain.context_models import ContextRecord
from app.services.store_instance import store
from app.api.tick_schema import TickRequest
from app.domain.actions import Action, TickResponse
from app.api.reply_schema import ReplyRequest, ReplyResponse
from app.services.evidence_builder import EvidenceBuilder
from app.services.composer import Composer
import json
import httpx

router = APIRouter()
evidence_builder = EvidenceBuilder()
composer = Composer()


@router.get("/v1/healthz")
def health():
    return {
        "status": "ok",
        "uptime_seconds": 0,
        "contexts_loaded": {
            "category": len(store.categories),
            "merchant": len(store.merchants),
            "customer": len(store.customers),
            "trigger": len(store.triggers),
        },
    }

@router.get("/v1/metadata")
def metadata():
    return {
        "team_name": "Disha Sikka",
        "model": "mistral-large-latest",
        "version": "1.0.0",
    }

@router.post("/v1/context", response_model=ContextResponse)
def push_context(request: ContextRequest):

    record = ContextRecord(
        context_id=request.context_id,
        version=request.version,
        delivered_at=request.delivered_at,
        payload=request.payload,
    )

    mapping = {
        "category": store.upsert_category,
        "merchant": store.upsert_merchant,
        "customer": store.upsert_customer,
        "trigger": store.upsert_trigger,
    }

    accepted = mapping[request.scope](record)

    if not accepted:
        current = getattr(store, f"{request.scope}s")[request.context_id]

        return ContextResponse(
            accepted=False,
            reason="stale_version",
            current_version=current.version,
        )

    return ContextResponse(
        accepted=True,
        ack_id=f"ack_{request.context_id}_v{request.version}",
        stored_at=datetime.utcnow(),
    )

@router.post("/v1/tick", response_model=TickResponse)
def tick(request: TickRequest):

    actions = []

    for trigger_id in request.available_triggers:

        trigger = store.triggers.get(trigger_id)

        if trigger is None:
            continue

        payload = trigger.payload

        merchant_id = payload.get("merchant_id")
        merchant = store.merchants.get(merchant_id)

        if merchant is None:
            continue

        category_slug = merchant.payload.get("category_slug")
        category = store.categories.get(category_slug)

        if category is None:
            continue

        customer = None
        customer_id = payload.get("customer_id")

        if customer_id:
            customer_record = store.customers.get(customer_id)
            if customer_record:
                customer = customer_record.payload

        evidence = evidence_builder.build(
            category=category.payload,
            merchant=merchant.payload,
            trigger=payload,
            customer=customer,
        )

        try:
            response = composer.compose(evidence)
        except httpx.TimeoutException:
            continue
        except httpx.HTTPError:
            continue
        except Exception:
            continue

        try:
            generated = json.loads(response)
            generated.setdefault("body", "")
            generated.setdefault("cta", "open_ended")
            generated.setdefault("rationale", "")

        except Exception:

            start = response.find("{")
            end = response.rfind("}")

            if start != -1 and end != -1:
                try:
                    generated = json.loads(response[start:end + 1])
                except Exception:
                    generated = {
                        "body": response.strip(),
                        "cta": "open_ended",
                        "rationale": "Fallback",
                    }
            else:
                generated = {
                    "body": response.strip(),
                    "cta": "open_ended",
                    "rationale": "Fallback",
                }
        if not generated["body"].strip():
            continue

        action = Action(
            conversation_id=f"conv_{trigger_id}",
            merchant_id=merchant_id,
            customer_id=customer_id,
            send_as="merchant_on_behalf" if customer_id else "vera",
            trigger_id=trigger_id,
            template_name="dynamic_v1",
            template_params=[],
            body=generated.get("body", ""),
            cta=generated.get("cta", "open_ended"),
            suppression_key=payload.get("suppression_key", trigger_id),
            rationale=generated.get("rationale", ""),
        )

        actions.append(action)

    return TickResponse(actions=actions)

@router.post("/v1/reply", response_model=ReplyResponse)
def reply(request: ReplyRequest):

    message = request.message.lower()

    # Hostile / Opt-out
    if any(x in message for x in [
        "stop",
        "spam",
        "not interested",
        "useless",
        "don't message",
        "do not message",
    ]):
        return ReplyResponse(
            action="end",
            rationale="Merchant opted out.",
        )

    # Auto reply
    if (
        "thank you for contacting" in message
        or "respond shortly" in message
        or "auto reply" in message
    ):
        if request.turn_number >= 4:
            return ReplyResponse(
                action="end",
                rationale="Repeated auto replies detected.",
            )

        return ReplyResponse(
            action="wait",
            wait_seconds=14400,
            rationale="Detected auto reply.",
        )

    # Intent transition
    if any(x in message for x in [
        "let's do it",
        "lets do it",
        "what's next",
        "whats next",
        "yes",
        "okay",
        "ok",
    ]):
        return ReplyResponse(
            action="send",
            body=(
                "Great! I'll prepare everything for you. "
                "I'll draft the message and share it for your approval."
            ),
            cta="binary_confirm_cancel",
            rationale="Merchant is ready to proceed.",
        )

    # Default
    return ReplyResponse(
        action="send",
        body="Thanks! Let me help you with that.",
        cta="open_ended",
        rationale="General response.",
    )