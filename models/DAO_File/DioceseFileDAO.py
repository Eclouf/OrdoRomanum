# -*- encoding:utf-8 -*-
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from .AbstractFileDAO import AbstractFileDAO
from models.utils.file_parsers import parse_kv_document


@dataclass
class DioceseFiche:
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
    mass: Optional[Dict[str, Any]] = None
    com: str = ''
    note: str = ''
    degree: Optional[int] = None
    rank: Optional[int] = None
    occ: Optional[str] = None
    con: Optional[str] = None
    martyrology: Optional[List[str]] = None


class DioceseFileDAO(AbstractFileDAO):
    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        self.diocese_root = os.path.join(self.locale_root, 'Diocese')

    def _find_file_for(self, month: int, day: int) -> Optional[str]:
        # Deterministic fast path: Diocese/MM/MM-DD.txt
        mdir = os.path.join(self.diocese_root, f"{month:02d}")
        cand = os.path.join(mdir, f"{month:02d}-{day:02d}.txt")
        return cand if os.path.isfile(cand) else None

    def _parse_file(self, path: str) -> DioceseFiche:
        text = self._read_text(path)
        data: Dict[str, Any] = parse_kv_document(text)
        f = DioceseFiche()
        # direct fields
        f.title = str(data.get('title', '')).strip()
        # Mass as structured dict: {'title': ..., 'commemoration': ..., 'gloria': ..., 'credo': ...}
        messe_val = data.get('messe')
        mass_dict: Dict[str, Any] = {}
        if isinstance(messe_val, dict):
            title_val = str(messe_val.get('_value', '')).strip()
            if title_val:
                if title_val.isdigit():
                    try:
                        mass_dict['common_id'] = int(title_val)
                    except Exception:
                        pass
                else:
                    mass_dict['title'] = title_val
            for k, v in messe_val.items():
                if k == '_value':
                    continue
                if isinstance(v, str):
                    mass_dict[k] = v.strip()
        else:
            raw = messe_val or data.get('mass', '')
            s = str(raw).strip()
            # If numeric, treat as reference to Common.txt ID
            if s.isdigit():
                try:
                    mass_dict['common_id'] = int(s)
                except Exception:
                    pass
            elif s:
                mass_dict['title'] = s
        f.mass = mass_dict or None

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
        # occurrence/content codes are symbolic (e.g., F2U, D2): read as strings
        occ_val = data.get('occ')
        con_val = data.get('con')
        f.occ = str(occ_val).strip() if isinstance(occ_val, str) and occ_val.strip() else None
        f.con = str(con_val).strip() if isinstance(con_val, str) and con_val.strip() else None
        # Be resilient to misplaced '##occ'/'##con' stored under another section dict
        if f.occ is None or f.con is None:
            for v in data.values():
                if isinstance(v, dict):
                    if f.occ is None:
                        ov = v.get('occ')
                        if isinstance(ov, str) and ov.strip():
                            f.occ = ov.strip()
                    if f.con is None:
                        cv = v.get('con')
                        if isinstance(cv, str) and cv.strip():
                            f.con = cv.strip()
                if f.occ is not None and f.con is not None:
                    break
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
        messe_block = f.mass if isinstance(f.mass, dict) else {}
        com_val = messe_block.get('commemoration', '') if isinstance(messe_block.get('commemoration', ''), str) else ''
        f.com = com_val.strip()
        # martyrology parsing: split with '|'
        mart_val = data.get('martirologe')
        mart_text = None
        if isinstance(mart_val, dict):
            mart_text = mart_val.get('_value') if isinstance(mart_val.get('_value'), str) else None
        elif isinstance(mart_val, str):
            mart_text = mart_val
        if isinstance(mart_text, str):
            if '|' in mart_text:
                items = [s.strip() for s in mart_text.split('|') if s.strip()]
            else:
                items = [mart_text.strip()] if mart_text.strip() else []
            f.martyrology = items or None
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
