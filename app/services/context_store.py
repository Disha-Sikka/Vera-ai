from app.domain.context_models import ContextRecord


class ContextStore:
    """
    In-memory version-aware context storage.
    """

    def __init__(self):
        self.categories: dict[str, ContextRecord] = {}
        self.merchants: dict[str, ContextRecord] = {}
        self.customers: dict[str, ContextRecord] = {}
        self.triggers: dict[str, ContextRecord] = {}

    def _upsert(
        self,
        store: dict[str, ContextRecord],
        record: ContextRecord,
    ) -> bool:
        """
        Insert or update only if the incoming version is newer.
        """

        existing = store.get(record.context_id)

        if existing is None:
            store[record.context_id] = record
            return True

        if record.version > existing.version:
            store[record.context_id] = record
            return True

        return False

    def upsert_category(self, record: ContextRecord) -> bool:
        return self._upsert(self.categories, record)

    def upsert_merchant(self, record: ContextRecord) -> bool:
        return self._upsert(self.merchants, record)

    def upsert_customer(self, record: ContextRecord) -> bool:
        return self._upsert(self.customers, record)

    def upsert_trigger(self, record: ContextRecord) -> bool:
        return self._upsert(self.triggers, record)