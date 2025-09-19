# -*- encoding:utf-8 -*-
import os
import json
from functools import lru_cache
from typing import Optional
from models.utils import indexer


class AbstractFileDAO:
    def __init__(self, model_manager) -> None:
        # ModelManager is kept only for symmetry; not required for file access
        self.model_manager = model_manager
        # default data root inferred from project structure
        app_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        self.repo_root = app_path
        self.models_root = os.path.join(self.repo_root, 'models')
        self.locale_root = os.path.join(self.models_root, 'fr')  # default locale
        self.index_root = os.path.join(self.models_root, 'index')
        os.makedirs(self.index_root, exist_ok=True)

    @staticmethod
    @lru_cache(maxsize=512)
    def _read_text(path: str) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def _list_files(dir_path: str, prefix: Optional[str] = None, suffix: Optional[str] = None):
        if not os.path.isdir(dir_path):
            return []
        items = []
        for name in os.listdir(dir_path):
            if prefix and not name.startswith(prefix):
                continue
            if suffix and not name.endswith(suffix):
                continue
            items.append(os.path.join(dir_path, name))
        return items

    def _read_json(self, path: str) -> dict:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def _load_or_build_sanctoral_index(self) -> dict:
        idx_path = os.path.join(self.index_root, 'sanctoral_index.json')
        if not os.path.isfile(idx_path):
            indexer.build_sanctoral_index(self.locale_root, self.index_root)
        return self._read_json(idx_path)

    def _load_or_build_temporal_index(self) -> dict:
        idx_path = os.path.join(self.index_root, 'temporal_index.json')
        if not os.path.isfile(idx_path):
            indexer.build_temporal_index(self.locale_root, self.index_root)
        return self._read_json(idx_path)
