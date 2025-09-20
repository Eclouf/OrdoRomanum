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
from typing import Any, Optional
import sys

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

USE_COLOR = False


def _label_or_none(row: Any) -> Optional[str]:
    return getattr(row, "label", None) if row is not None else None


def _c(code: str, text: str) -> str:
    if not USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def _h(text: str) -> str:
    # header style
    return _c('1', text)  # bold


def _lbl(text: str) -> str:
    # label style
    return _c('36', text)  # cyan


def _format_mass(mass: Any) -> str:
    if not isinstance(mass, dict):
        return str(mass) if mass else ""
    lines = []
    title = mass.get("title")
    if title:
        lines.append(f"{_h('Messe')}: {title}")
    label_map = {
        "commemoration": "Commémoration",
        "gloria": "Gloria",
        "credo": "Credo",
        "preface": "Préface",
    }
    for k in ("commemoration", "gloria", "credo", "preface"):
        v = mass.get(k)
        if v:
            label = label_map.get(k, k)
            lines.append(f"    - {_lbl(label)}: {v}")
    return "\n".join(lines) if lines else ""


def _print_text(obj: Any) -> None:
    print(obj)


def _render_sanctoral(model: ModelManager, fest: dict[str, Any]) -> str:
    if not fest:
        return "Aucune fête trouvée."
    # Resolve labels for category/color if needed
    cat_label = _label_or_none(fest.get("category"))
    col_label = _label_or_none(fest.get("color"))

    parts: list[str] = []
    parts.append(f"{_h('Titre')}: {fest.get('title','')}")
    if cat_label:
        parts.append(f"{_lbl('Catégorie')}: {cat_label}")
    if col_label:
        parts.append(f"{_lbl('Couleur')}: {col_label}")
    deg = fest.get('degree')
    rng = fest.get('rank')
    if deg is not None:
        parts.append(f"{_lbl('Degré')}: {deg}")
    if rng is not None:
        parts.append(f"{_lbl('Rang')}: {rng}")

    # Office
    office_parts = []
    for k in ("office", "matins", "lauds", "prime", "little_hours", "vespers", "compline"):
        v = fest.get(k)
        if v:
            label = {
                "office": "Office",
                "matins": "Matines",
                "lauds": "Laudes",
                "prime": "Prime",
                "little_hours": "Petites Heures",
                "vespers": "Vêpres",
                "compline": "Complies",
            }[k]
            office_parts.append(f"  - {label}: {v}")
    if office_parts:
        parts.append(f"{_h('Office')}:\n" + "\n".join(office_parts))

    # Mass
    mass_text = _format_mass(fest.get("mass"))
    if mass_text:
        parts.append(mass_text)
    # Avoid duplicate commemoration line if mass already includes it
    mass_has_com = isinstance(fest.get("mass"), dict) and bool(fest.get("mass", {}).get("commemoration"))
    if fest.get("com") and not mass_has_com:
        parts.append(f"{_lbl('Commémoration')}: {fest['com']}")
    if fest.get("note"):
        parts.append(f"{_lbl('Notes')}: {fest['note']}")
    return "\n\n".join(parts)


def _render_temporal(model: ModelManager, fiche: Any) -> str:
    if fiche is None:
        return "Aucune fiche temporelle trouvée."
    # fiche est une dataclass TemporalFiche
    d = asdict(fiche) if is_dataclass(fiche) else fiche
    parts: list[str] = []
    if d.get('id'):
        parts.append(f"{_lbl('ID')}: {d['id']}")
    if d.get('title'):
        parts.append(f"{_h('Titre')}: {d['title']}")
    # No category/color resolution here; temporal fiches peuvent aussi référencer category/color
    mass_text = _format_mass(d.get('mass'))
    if mass_text:
        parts.append(mass_text)
    office_parts = []
    for k in ("office", "matins", "lauds", "prime", "little_hours", "vespers", "compline"):
        v = d.get(k)
        if v:
            label = {
                "office": "Office",
                "matins": "Matines",
                "lauds": "Laudes",
                "prime": "Prime",
                "little_hours": "Petites Heures",
                "vespers": "Vêpres",
                "compline": "Complies",
            }[k]
            office_parts.append(f"  - {label}: {v}")
    if office_parts:
        parts.append("Office:\n" + "\n".join(office_parts))
    return "\n\n".join(parts) if parts else "Fiche temporelle."


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
    if args.format == 'json':
        print(json.dumps(to_serializable(fest), ensure_ascii=False, indent=2))
    else:
        text = _render_sanctoral(model, fest)
        _print_text(text)


def cmd_temporal(args: argparse.Namespace) -> None:
    date = datetime.strptime(args.date, "%Y-%m-%d")
    model = ModelManager()
    dao = model.get_temporal_dao()
    fiche = dao.get_by_date(date) if dao else None
    if args.format == 'json':
        print(json.dumps(to_serializable(fiche), ensure_ascii=False, indent=2))
    else:
        text = _render_temporal(model, fiche)
        _print_text(text)


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
    p_san.add_argument("--format", choices=["text", "json"], default="text", help="Format de sortie")
    p_san.add_argument("--color", choices=["auto", "on", "off"], default="auto", help="Couleur en sortie texte")
    p_san.set_defaults(func=cmd_sanctoral)

    p_tmp = sub.add_parser("temporal", help="Afficher la fiche temporelle pour une date (YYYY-MM-DD)")
    p_tmp.add_argument("--date", required=True, help="Date au format YYYY-MM-DD")
    p_tmp.add_argument("--format", choices=["text", "json"], default="text", help="Format de sortie")
    p_tmp.add_argument("--color", choices=["auto", "on", "off"], default="auto", help="Couleur en sortie texte")
    p_tmp.set_defaults(func=cmd_temporal)

    p_col = sub.add_parser("colors", help="Afficher une couleur par id")
    p_col.add_argument("--id", required=True, help="Identifiant de couleur")
    p_col.set_defaults(func=cmd_colors)

    p_cat = sub.add_parser("category", help="Afficher une catégorie par id")
    p_cat.add_argument("--id", required=True, help="Identifiant de catégorie")
    p_cat.set_defaults(func=cmd_category)

    args = parser.parse_args()

    # setup color policy
    global USE_COLOR
    if getattr(args, 'format', 'text') == 'text':
        if getattr(args, 'color', 'auto') == 'on':
            USE_COLOR = True
        elif getattr(args, 'color', 'auto') == 'off':
            USE_COLOR = False
        else:  # auto
            USE_COLOR = sys.stdout.isatty()
    else:
        USE_COLOR = False

    args.func(args)


if __name__ == "__main__":
    main()
