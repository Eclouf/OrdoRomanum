# -*- encoding:utf-8 -*-
import os
from typing import Optional, List
from .AbstractFileDAO import AbstractFileDAO


class ColorRow:
    def __init__(self, id: int, label: str) -> None:
        self.id = id
        self.label = label


class ColorsFileDAO(AbstractFileDAO):
    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        # historical filename was 'Color' without extension
        self.color_path_candidates = [
            os.path.join(self.locale_root, 'Color'),
            os.path.join(self.locale_root, 'Color.txt'),
        ]
        self._all_cache: Optional[List[ColorRow]] = None

    def _resolve_path(self) -> Optional[str]:
        for p in self.color_path_candidates:
            if os.path.isfile(p):
                return p
        return None

    def _load_all(self) -> List[ColorRow]:
        if self._all_cache is not None:
            return self._all_cache
        rows: List[ColorRow] = []
        path = self._resolve_path()
        if not path:
            self._all_cache = rows
            return rows
        text = self._read_text(path)
        for line in text.splitlines():
            if not line.strip():
                continue
            if line.strip().startswith('#'):
                continue
            # split by tab or multiple spaces
            parts = line.split('\t', 1)
            if len(parts) != 2:
                # try spaces
                parts = [p for p in line.split(' ') if p]
                if len(parts) >= 2:
                    id_part = parts[0]
                    label = ' '.join(parts[1:])
                else:
                    continue
            else:
                id_part = parts[0]
                label = parts[1]
            try:
                id_ = int(id_part.strip())
            except ValueError:
                continue
            rows.append(ColorRow(id_, label.strip()))
        self._all_cache = rows
        return rows

    def get_by_id(self, id: int) -> Optional[ColorRow]:
        for r in self._load_all():
            if r.id == id:
                return r
        return None

    def get_all(self) -> List[ColorRow]:
        return list(self._load_all())
