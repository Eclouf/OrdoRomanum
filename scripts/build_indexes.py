# -*- encoding:utf-8 -*-
"""
Build JSON indexes for TXT backends:
- models/index/sanctoral_index.json
- models/index/temporal_index.json

Usage:
  python scripts/build_indexes.py
"""
from pathlib import Path
from models.utils.indexer import build_sanctoral_index, build_temporal_index


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    models_root = base / 'models'
    locale_root = models_root / 'fr'
    index_root = models_root / 'index'
    index_root.mkdir(parents=True, exist_ok=True)

    sanctoral_path = build_sanctoral_index(str(locale_root), str(index_root))
    temporal_path = build_temporal_index(str(locale_root), str(index_root))

    print(f"Sanctoral index: {sanctoral_path}")
    print(f"Temporal index:  {temporal_path}")


if __name__ == '__main__':
    main()
