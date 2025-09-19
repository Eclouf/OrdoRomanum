# -*- encoding:utf-8 -*-
from typing import Any, Optional
from .AbstractFileDAO import AbstractFileDAO


class OfficeFileDAO(AbstractFileDAO):
    """
    File-based office accessor.
    For now, it acts as a passthrough: if an "id" is a string (embedded content), return it.
    If it's an int, you can later map it to files or templates; we return None for unknown ids.
    """

    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)

    def _resolve(self, value: Any) -> Optional[str]:
        if value is None:
            return None
        if isinstance(value, str):
            return value
        # Future: lookup by integer id from a fileset if defined
        return None

    def get_by_id(self, id: int):
        # Not used by controllers directly in current code; implement if needed
        return None

    def get_office(self, id: Any):
        return self._resolve(id)

    def get_matins(self, id: Any):
        return self._resolve(id)

    def get_lauds(self, id: Any):
        return self._resolve(id)

    def get_prime(self, id: Any):
        return self._resolve(id)

    def get_little_hours(self, id: Any):
        return self._resolve(id)

    def get_vespers(self, id: Any):
        return self._resolve(id)

    def get_compline(self, id: Any):
        return self._resolve(id)

    def get_all(self):
        return []
