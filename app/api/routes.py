from datetime import datetime

from fastapi import APIRouter

from app.api.schemas import ContextRequest, ContextResponse
from app.domain.context_models import ContextRecord
from app.services.context_store import ContextStore
from app.services.store_instance import store

router = APIRouter()

store = ContextStore()


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