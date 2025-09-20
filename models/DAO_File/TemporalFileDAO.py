# -*- encoding:utf-8 -*-
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any
from .AbstractFileDAO import AbstractFileDAO
from models.utils.file_parsers import parse_kv_document
from controllers.CalendarCtrl import CalendarRom


@dataclass
class TemporalFiche:
    id: str = ''
    title: str = ''
    category: Optional[int] = None
    color: Optional[int] = None
    office: Optional[str] = None
    matins: Optional[str] = None
    lauds: Optional[str] = None
    prime: Optional[str] = None
    little_hours: Optional[str] = None
    vespers: Optional[str] = None
    compline: Optional[str] = None
    mass: str = ''
    com: str = ''
    note: str = ''
    degree: Optional[int] = None
    rank: Optional[int] = None


class TemporalFileDAO(AbstractFileDAO):
    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        self.temporal_root = os.path.join(self.locale_root, 'Temporal')
        self._calendar = CalendarRom()
        self._year_map_cache: dict[int, dict[str, str]] = {}

    def _file_for_id(self, id_: str) -> Optional[str]:
        # Deterministic fast path: Temporal/<id>.txt
        cand = os.path.join(self.temporal_root, f"{id_}.txt")
        if os.path.isfile(cand):
            return cand
        # Optional fallback via index (useful if files are organized differently)
        # idx = self._load_or_build_temporal_index()
        # rel = idx.get(id_)
        # if isinstance(rel, str) and rel:
        #     abs_path = os.path.join(self.locale_root, rel)
        #     if os.path.isfile(abs_path):
        #         return abs_path
        return None

    def _parse_file(self, id_: str, path: str) -> TemporalFiche:
        text = self._read_text(path)
        data: Dict[str, Any] = parse_kv_document(text)
        f = TemporalFiche()
        f.id = id_
        f.title = str(data.get('title', '')).strip()
        f.mass = str(data.get('messe', '')).strip() or str(data.get('mass', '')).strip()
        f.note = str(data.get('notes', '')).strip() or str(data.get('note', '')).strip()
        # ints
        def to_int(x):
            try:
                return int(str(x).strip())
            except Exception:
                return None
        f.category = to_int(data.get('category'))
        f.color = to_int(data.get('color'))
        f.degree = to_int(data.get('degree'))
        f.rank = to_int(data.get('rank'))
        # office block
        office_block = data.get('office', {}) if isinstance(data.get('office', {}), dict) else {}
        f.office = office_block.get('common') or None
        f.matins = office_block.get('matins') or None
        f.lauds = office_block.get('laudes') or office_block.get('lauds') or None
        f.prime = office_block.get('prime') or None
        f.little_hours = '\n'.join([s for s in [office_block.get('terce'), office_block.get('sext'), office_block.get('none')] if isinstance(s, str) and s]) or None
        f.vespers = office_block.get('vespers') or None
        f.compline = office_block.get('compline') or None
        # mass subfields
        messe_block = data.get('messe', {}) if isinstance(data.get('messe', {}), dict) else {}
        f.com = messe_block.get('commemoration', '') if isinstance(messe_block.get('commemoration', ''), str) else ''
        return f

    def get_by_id(self, id_: str) -> Optional[TemporalFiche]:
        path = self._file_for_id(id_)
        if not path:
            return None
        return self._parse_file(id_, path)

    def get_by_date(self, date: datetime) -> Optional[TemporalFiche]:
        # cache per year to avoid recomputing the full map repeatedly
        ids = self._year_map_cache.get(date.year)
        if ids is None:
            ids = self._calendar.date_to_id_map(date.year)
            self._year_map_cache[date.year] = ids
        id_ = ids.get(date.strftime('%Y-%m-%d'))
        if not id_:
            return None
        return self.get_by_id(id_)

    def get_all(self):
        if not os.path.isdir(self.temporal_root):
            return []
        return [os.path.join(self.temporal_root, n) for n in os.listdir(self.temporal_root) if n.endswith('.txt')]
