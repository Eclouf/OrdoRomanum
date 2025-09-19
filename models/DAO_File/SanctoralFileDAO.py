# -*- encoding:utf-8 -*-
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any
from .AbstractFileDAO import AbstractFileDAO
from models.utils.file_parsers import parse_kv_document


@dataclass
class SanctoralFiche:
    title: str = ''
    category: Optional[int] = None
    color: Optional[int] = None
    office: Optional[int] = None
    matins: Optional[int] = None
    lauds: Optional[int] = None
    prime: Optional[int] = None
    little_hours: Optional[int] = None
    vespers: Optional[int] = None
    compline: Optional[int] = None
    mass: str = ''
    com: str = ''
    note: str = ''
    degree: Optional[int] = None
    rank: Optional[int] = None
    occ: Optional[int] = None
    con: Optional[int] = None


class SanctoralFileDAO(AbstractFileDAO):
    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        self.sanctoral_root = os.path.join(self.locale_root, 'Sanctoral')

    def _find_file_for(self, month: int, day: int) -> Optional[str]:
        # Try index first
        idx = self._load_or_build_sanctoral_index()
        key = f"{month:02d}-{day:02d}"
        rel = idx.get(key)
        if isinstance(rel, str) and rel:
            abs_path = os.path.join(self.locale_root, rel)
            if os.path.isfile(abs_path):
                return abs_path
        # Fallback: scan directory
        mdir = os.path.join(self.sanctoral_root, f"{month:02d}")
        if not os.path.isdir(mdir):
            return None
        prefix = f"{day:02d}-"
        for name in os.listdir(mdir):
            if name.startswith(prefix) and name.endswith('.txt'):
                return os.path.join(mdir, name)
        return None

    def _parse_file(self, path: str) -> SanctoralFiche:
        text = self._read_text(path)
        data: Dict[str, Any] = parse_kv_document(text)
        f = SanctoralFiche()
        # direct fields
        f.title = str(data.get('title', '')).strip()
        # Mass title and notes: support both scalar and section with subkeys ('_value')
        messe_val = data.get('messe')
        if isinstance(messe_val, dict):
            f.mass = str(messe_val.get('_value', '')).strip()
        else:
            f.mass = str(messe_val or data.get('mass', '')).strip()

        notes_val = data.get('notes')
        if isinstance(notes_val, dict):
            f.note = str(notes_val.get('_value', '')).strip()
        else:
            f.note = str(notes_val or data.get('note', '')).strip()
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
        f.occ = to_int(data.get('occ'))
        f.con = to_int(data.get('con'))
        # office block
        office_block = data.get('office', {}) if isinstance(data.get('office', {}), dict) else {}
        # We set the attributes to small integers if available, otherwise set to None and let OfficeFileDAO passthrough strings
        # But to keep controller-compatible, we put actual string content into 'office-like' ids and rely on OfficeFileDAO to passthrough
        # Aggregate content
        def _val(key):
            v = office_block.get(key)
            return v if isinstance(v, str) else ''
        # Use negative pseudo-ids encoded as strings so OfficeFileDAO can detect and passthrough
        # Store strings directly; OfficeFileDAO will detect and return as-is
        f.office = office_block.get('common') or None
        f.matins = office_block.get('matins') or None
        f.lauds = office_block.get('laudes') or office_block.get('lauds') or None
        f.prime = office_block.get('prime') or None
        f.little_hours = '\n'.join([s for s in [office_block.get('terce'), office_block.get('sext'), office_block.get('none')] if isinstance(s, str) and s]) or None
        f.vespers = office_block.get('vespers') or None
        f.compline = office_block.get('compline') or None
        # mass subfields
        messe_block = data.get('messe', {}) if isinstance(data.get('messe', {}), dict) else {}
        com_val = messe_block.get('commemoration', '') if isinstance(messe_block.get('commemoration', ''), str) else ''
        f.com = com_val.strip()
        return f

    def get_by_id(self, month: int, day: int) -> Optional[SanctoralFiche]:
        path = self._find_file_for(month, day)
        if not path:
            return None
        return self._parse_file(path)

    def get_all(self):
        # Optional: iterate all sanctoral files; avoid loading content eagerly for memory
        all_entries = []
        for m in range(1, 13):
            mdir = os.path.join(self.sanctoral_root, f"{m:02d}")
            if not os.path.isdir(mdir):
                continue
            for name in os.listdir(mdir):
                if name.endswith('.txt'):
                    all_entries.append(os.path.join(mdir, name))
        return all_entries
