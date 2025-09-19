# -*- encoding:utf-8 -*-
import os
from typing import Optional, List
from .AbstractFileDAO import AbstractFileDAO


class CategoryRow:
    def __init__(self, id: int, label: str) -> None:
        self.id = id
        self.label = label


class CategoryFileDAO(AbstractFileDAO):
    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        self.cat_path = os.path.join(self.locale_root, 'Category.txt')
        self._all_cache: Optional[List[CategoryRow]] = None

    def _load_all(self) -> List[CategoryRow]:
        if self._all_cache is not None:
            return self._all_cache
        rows: List[CategoryRow] = []
        if not os.path.isfile(self.cat_path):
            self._all_cache = rows
            return rows
        text = self._read_text(self.cat_path)
        for line in text.splitlines():
            if not line.strip():
                continue
            if line.strip().startswith('#'):
                continue
            parts = line.split('\t', 1)
            if len(parts) != 2:
                continue
            try:
                id_ = int(parts[0].strip())
            except ValueError:
                continue
            label = parts[1].strip()
            rows.append(CategoryRow(id_, label))
        self._all_cache = rows
        return rows

    def get_by_id(self, id: int) -> Optional[CategoryRow]:
        for r in self._load_all():
            if r.id == id:
                return r
        return None

    def get_all(self) -> List[CategoryRow]:
        return list(self._load_all())
