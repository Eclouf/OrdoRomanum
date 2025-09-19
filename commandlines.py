# -*- encoding:utf-8 -*-
"""
CLI utilitaire pour OrdoRomanum (backend fichiers TXT).

Exemples:
  - Construire les index JSON:
      python commandlines.py build-indexes

  - Obtenir la fête sanctorale d'une date (YYYY-MM-DD):
      python commandlines.py sanctoral --date 2025-01-13

  - Obtenir la fiche temporelle d'une date (YYYY-MM-DD):
      python commandlines.py temporal --date 2025-04-20

  - Consulter une couleur par id:
      python commandlines.py colors --id 3

  - Consulter une catégorie par id:
      python commandlines.py category --id 14

Note: main.py sera dédié au GUI, ce fichier sert aux usages en ligne de commande/tests.
"""
from __future__ import annotations
import argparse
import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Ensure relative imports work when run from project root
BASE_DIR = Path(__file__).resolve().parent

# App imports
from models.ModelManager import ModelManager
from models.utils.indexer import build_sanctoral_index, build_temporal_index
from controllers.SanctoralCtrl import SanctoralCtrl


def to_serializable(obj: Any) -> Any:
    """Convert objects from DAOs or dataclasses to a JSON-serializable structure."""
    if obj is None:
        return None
    if is_dataclass(obj):
        return asdict(obj)
    # ORM-like rows or simple containers
    if hasattr(obj, "__dict__"):
        # Strip private attrs
        return {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    # Fallback for strings, ints, dicts
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_serializable(x) for x in obj]
    return str(obj)


def cmd_build_indexes(_: argparse.Namespace) -> None:
    models_root = BASE_DIR / 'models'
    locale_root = models_root / 'fr'
    index_root = models_root / 'index'
    index_root.mkdir(parents=True, exist_ok=True)
    san_path = build_sanctoral_index(str(locale_root), str(index_root))
    tmp_path = build_temporal_index(str(locale_root), str(index_root))
    print(json.dumps({"sanctoral_index": san_path, "temporal_index": tmp_path}, ensure_ascii=False, indent=2))


def cmd_sanctoral(args: argparse.Namespace) -> None:
    date = datetime.strptime(args.date, "%Y-%m-%d")
    model = ModelManager()
    ctrl = SanctoralCtrl(model)
    fest = ctrl.get_fest(date)
    print(json.dumps(to_serializable(fest), ensure_ascii=False, indent=2))


def cmd_temporal(args: argparse.Namespace) -> None:
    date = datetime.strptime(args.date, "%Y-%m-%d")
    model = ModelManager()
    dao = model.get_temporal_dao()
    fiche = dao.get_by_date(date) if dao else None
    print(json.dumps(to_serializable(fiche), ensure_ascii=False, indent=2))


def cmd_colors(args: argparse.Namespace) -> None:
    model = ModelManager()
    dao = model.get_colors_dao()
    row = dao.get_by_id(int(args.id))
    out = {"id": getattr(row, "id", None), "label": getattr(row, "label", None)} if row else None
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_category(args: argparse.Namespace) -> None:
    model = ModelManager()
    dao = model.get_category_dao()
    row = dao.get_by_id(int(args.id))
    out = {"id": getattr(row, "id", None), "label": getattr(row, "label", None)} if row else None
    print(json.dumps(out, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="OrdoRomanum CLI (TXT backend)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_bi = sub.add_parser("build-indexes", help="Construire les index JSON (sanctoral/temporal)")
    p_bi.set_defaults(func=cmd_build_indexes)

    p_san = sub.add_parser("sanctoral", help="Afficher la fête sanctorale pour une date (YYYY-MM-DD)")
    p_san.add_argument("--date", required=True, help="Date au format YYYY-MM-DD")
    p_san.set_defaults(func=cmd_sanctoral)

    p_tmp = sub.add_parser("temporal", help="Afficher la fiche temporelle pour une date (YYYY-MM-DD)")
    p_tmp.add_argument("--date", required=True, help="Date au format YYYY-MM-DD")
    p_tmp.set_defaults(func=cmd_temporal)

    p_col = sub.add_parser("colors", help="Afficher une couleur par id")
    p_col.add_argument("--id", required=True, help="Identifiant de couleur")
    p_col.set_defaults(func=cmd_colors)

    p_cat = sub.add_parser("category", help="Afficher une catégorie par id")
    p_cat.add_argument("--id", required=True, help="Identifiant de catégorie")
    p_cat.set_defaults(func=cmd_category)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
