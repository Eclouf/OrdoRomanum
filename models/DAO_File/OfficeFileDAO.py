# -*- encoding:utf-8 -*-
import os
from typing import Any, Optional, Dict
from .AbstractFileDAO import AbstractFileDAO


class OfficeFileDAO(AbstractFileDAO):
    """
    File-based office accessor.
    For now, it acts as a passthrough: if an "id" is a string (embedded content), return it.
    If it's an int, you can later map it to files or templates; we return None for unknown ids.
    """

    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        self._common_map: Optional[Dict[int, str]] = None
        self._common_path_candidates = [
            os.path.join(self.locale_root, 'Common.txt'),
            os.path.join(self.locale_root, 'common.txt'),
        ]

    def _load_common_map(self) -> Dict[int, str]:
        if self._common_map is not None:
            return self._common_map
        path = next((p for p in self._common_path_candidates if os.path.isfile(p)), None)
        mapping: Dict[int, str] = {}
        if path:
            text = self._read_text(path)
            for line in text.splitlines():
                if not line.strip() or line.strip().startswith('#'):
                    continue
                # Split on tab first, then fallback to multi-space
                parts = line.split('\t', 1)
                if len(parts) != 2:
                    raw = [p for p in line.split(' ') if p]
                    if len(raw) >= 2:
                        key_part = raw[0]
                        val = ' '.join(raw[1:])
                    else:
                        continue
                else:
                    key_part, val = parts[0], parts[1]
                try:
                    key = int(key_part.strip())
                except ValueError:
                    continue
                mapping[key] = val.strip()
        self._common_map = mapping
        return mapping

    def _resolve(self, value: Any) -> Optional[str]:
        if value is None:
            return None
        # Try to interpret as numeric ID first (supports str like "7")
        try:
            num = int(str(value).strip())
            label = self._load_common_map().get(num)
            if label:
                return label
        except Exception:
            pass
        # Fallback: passthrough string content
        if isinstance(value, str):
            return value
        # Unknown
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
