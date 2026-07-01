from app.domain.context_models import ContextRecord
from app.services.context_store import ContextStore

store = ContextStore()

record = ContextRecord(
    id="merchant-1",
    version=1,
    payload={
        "name": "ABC Restaurant"
    }
)

print(store.upsert_merchant(record))

record2 = ContextRecord(
    id="merchant-1",
    version=0,
    payload={
        "name": "Old Data"
    }
)

print(store.upsert_merchant(record2))

print(store.merchants["merchant-1"])
