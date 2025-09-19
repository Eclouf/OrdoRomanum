# -*- encoding:utf-8 -*-
import json
import os
from typing import Dict


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def build_sanctoral_index(locale_root: str, index_root: str) -> str:
    """
    Scan models/fr/Sanctoral/** and build an index mapping 'MM-DD' -> relative path
    Returns the path to the written JSON file.
    """
    sanctoral_root = os.path.join(locale_root, 'Sanctoral')
    index_path = os.path.join(index_root, 'sanctoral_index.json')
    ensure_dir(index_root)
    idx: Dict[str, str] = {}
    if not os.path.isdir(sanctoral_root):
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(idx, f, ensure_ascii=False, indent=2)
        return index_path

    for mm in sorted(os.listdir(sanctoral_root)):
        mdir = os.path.join(sanctoral_root, mm)
        if not os.path.isdir(mdir):
            continue
        for name in sorted(os.listdir(mdir)):
            if not name.endswith('.txt'):
                continue
            # filenames are actually '<MM>-<DD>.txt' (first segment repeats the month)
            # derive day from second segment
            parts = name[:-4].split('-', 1)
            if len(parts) != 2:
                continue
            dd = parts[1]
            if len(dd) != 2 or not dd.isdigit():
                continue
            key = f"{mm}-{dd}"
            rel_path = os.path.join('Sanctoral', mm, name).replace('\\', '/')
            # If multiple entries per day, last one wins; can be extended to list later
            idx[key] = rel_path

    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
    return index_path


def build_temporal_index(locale_root: str, index_root: str) -> str:
    """
    Scan models/fr/Temporal/* and build an index mapping '<id>' -> relative path
    Returns the path to the written JSON file.
    """
    temporal_root = os.path.join(locale_root, 'Temporal')
    index_path = os.path.join(index_root, 'temporal_index.json')
    ensure_dir(index_root)
    idx: Dict[str, str] = {}
    if os.path.isdir(temporal_root):
        for name in sorted(os.listdir(temporal_root)):
            if not name.endswith('.txt'):
                continue
            id_ = name[:-4]
            rel_path = os.path.join('Temporal', name).replace('\\', '/')
            idx[id_] = rel_path
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
    return index_path
