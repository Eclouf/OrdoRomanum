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
        self._common_meta: Optional[Dict[int, Dict[str, str]]] = None
        self._common_path_candidates = [
            os.path.join(self.locale_root, 'Common.txt'),
            os.path.join(self.locale_root, 'common.txt'),
        ]

    def _load_common_map(self) -> Dict[int, str]:
        if self._common_map is not None:
            return self._common_map
        path = next((p for p in self._common_path_candidates if os.path.isfile(p)), None)
        mapping: Dict[int, str] = {}
        meta: Dict[int, Dict[str, str]] = {}
        if path:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            current_id: Optional[int] = None
            for raw in text.splitlines():
                if not raw.strip() or raw.lstrip().startswith('#'):
                    continue
                # ID line starts with a number
                stripped = raw.strip('\n\r')
                if stripped and stripped[0].isdigit():
                    # split on whitespace sequences
                    parts = [p for p in stripped.split(' ') if p]
                    if len(parts) >= 2:
                        key_part = parts[0]
                        label = ' '.join(parts[1:])
                        try:
                            current_id = int(key_part)
                        except ValueError:
                            current_id = None
                            continue
                        mapping[current_id] = label.strip()
                        meta.setdefault(current_id, {})
                        continue
                # Continuation meta line (indented)
                if current_id is not None and raw[:1].isspace():
                    cont = raw.strip()
                    if ':' in cont:
                        k, v = cont.split(':', 1)
                        key_norm = k.strip()
                        # Accept leading '-' or 'tab-' prefixes
                        if key_norm.startswith('-'):
                            key_norm = key_norm[1:].lstrip()
                        if key_norm.lower().startswith('tab-'):
                            key_norm = key_norm[4:]
                        meta[current_id][key_norm.strip().lower()] = v.strip()
                    continue
                # Otherwise, unknown format; ignore
            
        self._common_map = mapping
        self._common_meta = meta
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

    def get_common_inline_details(self, id_val: Any) -> Dict[str, Any]:
        try:
            num = int(str(id_val).strip())
        except Exception:
            return {}
        # Ensure maps are loaded
        self._load_common_map()
        if not self._common_meta:
            return {}
        data = self._common_meta.get(num, {})
        if not data:
            return {}
        # Only support 'messe' key for now (maps to mass.title)
        title = data.get('messe')
        if title:
            return {'mass': {'title': title}}
        return {}
