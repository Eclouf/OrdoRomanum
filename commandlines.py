# -*- encoding:utf-8 -*-
"""
CLI utilitaire pour OrdoRomanum (backend fichiers TXT).

INTERFACE INTERACTIVE:
  python commandlines.py    # Lance le menu interactif

COMMANDES DIRECTES:
  python commandlines.py sanctoral 2025-01-13
  python commandlines.py temporal 2025-04-20
  python commandlines.py calendar 2025
  python commandlines.py search saint
  python commandlines.py stats
  python commandlines.py build-indexes

Exemples avec arguments:
  python commandlines.py sanctoral --date 2025-01-13 --format json
  python commandlines.py temporal --date 2025-04-20 --color on
"""
from __future__ import annotations
import argparse
import json
import sys
import os
from dataclasses import asdict, is_dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional
from collections import Counter

# Ensure relative imports work when run from project root
BASE_DIR = Path(__file__).resolve().parent

# App imports
from models.ModelManager import ModelManager
from models.utils.indexer import build_sanctoral_index, build_temporal_index
from controllers.SanctoralCtrl import SanctoralCtrl
from controllers.TemporalCtrl import TemporalCtrl
from controllers.CalendarCtrl import CalendarRom
from controllers.ColorsCtrl import ColorsCtrl
from controllers.OccurenceCtrl import OccurenceCtrl
from controllers.Ordinarium import Ordination

USE_COLOR = True
DEBUG = False


def clear_screen():
    """Efface l'écran"""
    # Utilise print au lieu de os.system pour éviter les problèmes
    print("\n" * 50)  # Simule un effacement d'écran


def print_header():
    """Affiche l'en-tête"""
    clear_screen()
   
    print("\n" + "="*60)
    print(" ORDOROMANUM - Interface Liturgique")
    print("="*60)
    print("Interface interactive - Utilisez les numéros ou tapez 'help'")
    print("-"*60)


def print_menu():
    """Affiche le menu principal"""
    print("\n COMMANDES DISPONIBLES:")
    print("  1. Fête Sanctorale (par date)")
    print("  2. Fiche Temporelle (par date)")
    print("  3. Calendrier Annuel")
    print("  4. Recherche dans les fiches")
    print("  5. Statistiques du système")
    print("  6. Construire les index")
    print("  7. Couleurs liturgiques")
    print("  8. Catégories")
    print("  9. Ordinarium")
    print("  0. Quitter")
    print("\n Tapez le numéro de la commande ou 'help' pour plus d'aide")


def get_date_input(prompt: str = "Date (YYYY-MM-DD)") -> str:
    """Demande une date à l'utilisateur"""
    while True:
        date_str = input(f"{prompt}: ").strip()
        if not date_str:
            print(" Date requise")
            continue

        # Validation basique du format
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print(" Format invalide. Utilisez YYYY-MM-DD (ex: 2025-01-13)")


def get_year_input(prompt: str = "Année") -> str:
    """Demande une année à l'utilisateur"""
    while True:
        year_str = input(f"{prompt}: ").strip()
        if not year_str:
            print(" Année requise")
            continue

        try:
            year = int(year_str)
            if 1900 <= year <= 2100:
                return year_str
            else:
                print(" Année invalide (1900-2100)")
        except ValueError:
            print(" Année invalide (doit être un nombre)")


def get_search_input(prompt: str = "Terme à rechercher") -> str:
    """Demande un terme de recherche"""
    while True:
        search_str = input(f"{prompt}: ").strip()
        if not search_str:
            print(" Terme de recherche requis")
            continue
        return search_str


def get_id_input(prompt: str = "ID") -> str:
    """Demande un ID à l'utilisateur"""
    while True:
        id_str = input(f"{prompt}: ").strip()
        if not id_str:
            print(" ID requis")
            continue
        return id_str


def interactive_mode():
    """Mode interactif avec menu"""
    print_header()

    while True:
        print_menu()
        choice = input("\nVotre choix: ").strip().lower()

        if choice in ['0', 'quit', 'exit', 'q']:
            break

        elif choice in ['1', 'sanctoral', 'fête', 'fete']:
            cmd_sanctoral_interactive()

        elif choice in ['2', 'temporal', 'temporelle', 'fiche']:
            cmd_temporal_interactive()

        elif choice in ['3', 'calendar', 'calendrier', 'année', 'annee']:
            cmd_calendar_interactive()

        elif choice in ['4', 'search', 'recherche', 'chercher']:
            cmd_search_interactive()

        elif choice in ['5', 'stats', 'statistiques']:
            cmd_stats_interactive()

        elif choice in ['6', 'build', 'index', 'construire']:
            cmd_build_indexes_interactive()

        elif choice in ['7', 'colors', 'couleurs', 'couleur']:
            cmd_colors_interactive()

        elif choice in ['8', 'category', 'categories', 'catégorie', 'categorie']:
            cmd_category_interactive()

        elif choice in ['9', 'ordinarium', 'ordi']:
            cmd_ordinarium_interactive()

        elif choice in ['help', 'h', 'aide', '?']:
            show_help()

        else:
            print(f"\n Commande '{choice}' non reconnue.")
            print(" Tapez 'help' pour voir l'aide")

        input("\n Appuyez sur Entrée pour continuer...")
        print_header()


def show_help():
    """Affiche l'aide détaillée"""
    print("\n" + "="*60)
    print(" AIDE DÉTAILLÉE")
    print("="*60)
    print("\n COMMANDES:")
    print("  1. Fête Sanctorale    - Saints et fêtes du jour")
    print("  2. Fiche Temporelle   - Calendrier liturgique")
    print("  3. Calendrier Annuel  - Année complète")
    print("  4. Recherche          - Chercher dans les fiches")
    print("  5. Statistiques       - Infos sur les données")
    print("  6. Construire index   - Mettre à jour les index")
    print("  7. Couleurs           - Consulter couleurs liturgiques")
    print("  8. Catégories         - Consulter catégories")
    print("  9. Ordinarium         - Calcul avec règles diocésaines")
    print("  0. Quitter            - Sortir du programme")

    print("\n OPTIONS DE FORMAT:")
    print("  --format json         - Sortie JSON")
    print("  --format text         - Sortie texte (défaut)")
    print("  --color on/off/auto   - Couleurs (auto par défaut)")
    print("  --debug               - Mode debug")

    print("\n EXEMPLES D'USAGE:")
    print("  python commandlines.py sanctoral 2025-01-13")
    print("  python commandlines.py temporal 2025-04-20 --format json")
    print("  python commandlines.py calendar 2025")
    print("  python commandlines.py search saint")
    print("  python commandlines.py stats")
    print("\n" + "-"*60)
    print(" Tapez 'help' à tout moment pour revoir cette aide")


def cmd_sanctoral_interactive():
    """Mode interactif pour fête sanctorale"""
    print("\n" + "="*50)
    print(" FÊTE SANCTORALE")
    print("="*50)

    date_str = get_date_input("Date de la fête sanctorale")
    format_choice = input("Format (text/json) [text]: ").strip().lower() or 'text'

    # Créer les arguments
    args = argparse.Namespace()
    args.date = date_str
    args.format = format_choice
    args.color = 'auto'
    args.debug = False

    print(f"\n🔍 Recherche de la fête sanctorale pour {date_str}...")
    cmd_sanctoral(args)


def cmd_temporal_interactive():
    """Mode interactif pour fiche temporelle"""
    print("\n" + "="*50)
    print("🎯 FICHE TEMPORELLE")
    print("="*50)

    date_str = get_date_input("Date de la fiche temporelle")
    format_choice = input("Format (text/json) [text]: ").strip().lower() or 'text'

    args = argparse.Namespace()
    args.date = date_str
    args.format = format_choice
    args.color = 'auto'
    args.debug = False

    print(f"\n🔍 Recherche de la fiche temporelle pour {date_str}...")
    cmd_temporal(args)


def cmd_calendar_interactive():
    """Mode interactif pour calendrier"""
    print("\n" + "="*50)
    print("🎯 CALENDRIER ANNUEL")
    print("="*50)

    year_str = get_year_input("Année liturgique")
    format_choice = input("Format (text/json) [text]: ").strip().lower() or 'text'

    args = argparse.Namespace()
    args.year = year_str
    args.format = format_choice
    args.color = 'auto'
    args.debug = False

    print(f"\n🔍 Génération du calendrier pour {year_str}...")
    cmd_calendar(args)


def cmd_search_interactive():
    """Mode interactif pour recherche"""
    print("\n" + "="*50)
    print("🎯 RECHERCHE")
    print("="*50)

    query = get_search_input("Terme à rechercher")
    format_choice = input("Format (text/json) [text]: ").strip().lower() or 'text'

    args = argparse.Namespace()
    args.query = query
    args.format = format_choice
    args.color = 'auto'
    args.debug = False

    print(f"\n🔍 Recherche de '{query}'...")
    cmd_search(args)


def cmd_stats_interactive():
    """Mode interactif pour statistiques"""
    print("\n" + "="*50)
    print("🎯 STATISTIQUES")
    print("="*50)

    format_choice = input("Format (text/json) [text]: ").strip().lower() or 'text'

    args = argparse.Namespace()
    args.format = format_choice
    args.color = 'auto'
    args.debug = False

    cmd_stats(args)


def cmd_build_indexes_interactive():
    """Mode interactif pour construction d'index"""
    print("\n" + "="*50)
    print("🎯 CONSTRUCTION DES INDEX")
    print("="*50)

    print("⚠️  Cette opération peut prendre du temps...")
    confirm = input("Confirmer? (o/n) [o]: ").strip().lower() or 'o'

    if confirm in ['o', 'oui', 'y', 'yes']:
        cmd_build_indexes(None)
    else:
        print(" Opération annulée")


def cmd_colors_interactive():
    """Mode interactif pour couleurs"""
    print("\n" + "="*50)
    print("🎯 COULEURS LITURGIQUES")
    print("="*50)

    id_str = get_id_input("ID de la couleur")

    args = argparse.Namespace()
    args.id = id_str

    cmd_colors(args)


def cmd_category_interactive():
    """Mode interactif pour catégories"""
    print("\n" + "="*50)
    print("🎯 CATÉGORIES")
    print("="*50)

    id_str = get_id_input("ID de la catégorie")

    args = argparse.Namespace()
    args.id = id_str

    cmd_category(args)


def cmd_ordinarium_interactive():
    """Mode interactif pour ordinarium"""
    print("\n" + "="*50)
    print("🎯 ORDINARIUM")
    print("="*50)

    date_str = get_date_input("Date pour le calcul ordinarium")
    country = input("Pays [FR]: ").strip() or 'FR'
    diocese = input("Diocèse (optionnel): ").strip()
    congregation = input("Congrégation (optionnel): ").strip()
    format_choice = input("Format (text/json) [text]: ").strip().lower() or 'text'

    args = argparse.Namespace()
    args.date = date_str
    args.country = country
    args.diocese = diocese
    args.congregation = congregation
    args.format = format_choice
    args.color = 'auto'
    args.debug = False

    print(f"\n🔍 Calcul ordinarium pour {date_str}...")
    cmd_ordinarium(args)


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
    if not mass:
        return ""

    # Si c'est une string, l'afficher directement
    if isinstance(mass, str):
        # Vérifier si c'est une string qui représente un dictionnaire
        mass_str = mass.strip()
        if mass_str.startswith("{") and mass_str.endswith("}"):
            try:
                # Essayer de parser la string comme un dictionnaire
                import ast
                mass_dict = ast.literal_eval(mass_str)
                if isinstance(mass_dict, dict):
                    return _format_mass_dict(mass_dict)
            except (ValueError, SyntaxError):
                # Si ce n'est pas un dictionnaire valide, afficher la string telle quelle
                pass
        return f"{_h('Messe')}: {mass}"

    # Si ce n'est pas un dictionnaire, le convertir en string
    if not isinstance(mass, dict):
        return f"{_h('Messe')}: {str(mass)}"

    return _format_mass_dict(mass)


def _format_mass_dict(mass_dict: dict) -> str:
    """Formate un dictionnaire de messe"""
    lines = []

    # Cas 1: dictionnaire avec _value (format principal)
    if "_value" in mass_dict and mass_dict["_value"]:
        main_text = str(mass_dict["_value"]).strip()
        if main_text:
            lines.append(f"{_h('Messe')}: {main_text}")

    # Cas 2: dictionnaire avec title
    elif "title" in mass_dict and mass_dict["title"]:
        lines.append(f"{_h('Messe')}: {mass_dict['title']}")

    # Cas 3: dictionnaire avec d'autres champs mais pas de _value ni title
    elif mass_dict:
        # Chercher s'il y a du contenu textuel dans le dictionnaire
        for key, value in mass_dict.items():
            if key not in ["commemoration", "gloria", "credo", "preface"] and value:
                if isinstance(value, str) and value.strip():
                    lines.append(f"{_h('Messe')}: {value.strip()}")
                    break

    # Ajouter les éléments structurés (seulement s'ils ne sont pas vides)
    label_map = {
        "commemoration": "Commémoration",
        "gloria": "Gloria",
        "credo": "Credo",
        "preface": "Préface",
    }

    structured_items = []
    for k in ("commemoration", "gloria", "credo", "preface"):
        v = mass_dict.get(k)
        if v and str(v).strip():  # Ne pas afficher les valeurs vides ou juste des espaces
            label = label_map.get(k, k)
            structured_items.append(f"    - {_lbl(label)}: {v}")

    if structured_items:
        lines.extend(structured_items)

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
    # Debug info
    if DEBUG:
        occ = fest.get('occ')
        con = fest.get('con')
        if occ:
            parts.append(f"{_lbl('Occurrence')}: {occ}")
        if con:
            parts.append(f"{_lbl('Contenu')}: {con}")

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
    # Martyrology (list of entries) - display last
    mart = fest.get('martyrology')
    if isinstance(mart, list) and mart:
        bullets = "\n".join([f"  - {item}" for item in mart])
        parts.append(f"{_h('Martirologe')}:\n" + bullets)
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
        parts.append(f"{_h('Office')}:\n" + "\n".join(office_parts))
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


def cmd_calendar(args: argparse.Namespace) -> None:
    year = int(args.year)
    calendar = CalendarRom()
    cycles = calendar.liturgical_year(year)

    if args.format == 'json':
        print(json.dumps({
            'year': year,
            'cycles': to_serializable(cycles)
        }, ensure_ascii=False, indent=2))
    else:
        print(f"{_h(f'Calendrier Liturgique {year}')}")
        print(f"{'='*50}")

        for cycle_name, cycle_data in cycles.items():
            print(f"\n{_lbl(f'Cycle {cycle_name.upper()}')}:\n")
            for date, ordo_id in sorted(cycle_data.items()):
                print(f"  {date.strftime('%Y-%m-%d')}: {ordo_id}")


def cmd_search(args: argparse.Namespace) -> None:
    query = args.query.lower()
    results = []

    # Recherche dans les fichiers temporaux
    temporal_dir = BASE_DIR / 'models' / 'fr' / 'Temporal'
    if temporal_dir.exists():
        for file_path in temporal_dir.glob('*.txt'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query in content.lower():
                        results.append({
                            'type': 'temporal',
                            'file': file_path.name,
                            'content': content[:200] + ('...' if len(content) > 200 else '')
                        })
            except:
                pass

    # Recherche dans les fichiers sanctoraux
    sanctoral_dir = BASE_DIR / 'models' / 'fr' / 'Sanctoral'
    if sanctoral_dir.exists():
        for file_path in sanctoral_dir.glob('*.txt'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query in content.lower():
                        results.append({
                            'type': 'sanctoral',
                            'file': file_path.name,
                            'content': content[:200] + ('...' if len(content) > 200 else '')
                        })
            except:
                pass

    if args.format == 'json':
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print(f"Aucun résultat pour '{query}'")
            return

        print(f"{_h(f'Recherche: {query}')}")
        print(f"{'='*50}")
        print(f"{len(results)} résultats trouvés\n")

        for result in results[:20]:  # Limiter à 20 résultats
            print(f"{_lbl(result['type'].upper())}: {result['file']}")
            print(f"  {result['content']}\n")


def cmd_stats(args: argparse.Namespace) -> None:
    stats = {
        'timestamp': datetime.now().isoformat(),
        'directories': {},
        'counts': {},
        'sizes': {}
    }

    # Statistiques des répertoires
    models_dir = BASE_DIR / 'models' / 'fr'
    for subdir_name in ['Temporal', 'Sanctoral', 'Common']:
        subdir = models_dir / subdir_name
        if subdir.exists():
            files = list(subdir.glob('*.txt'))
            stats['directories'][subdir_name] = {
                'file_count': len(files),
                'total_size': sum(f.stat().st_size for f in files)
            }

    # Comptages par type
    temporal_dir = models_dir / 'Temporal'
    if temporal_dir.exists():
        type_counts = Counter()
        for file_path in temporal_dir.glob('*.txt'):
            filename = file_path.name
            if filename.startswith('sun_'):
                type_counts['dimanches'] += 1
            elif filename.startswith(('mon_', 'tue_', 'wed_', 'thu_', 'fri_', 'sat_')):
                type_counts['jours_semaine'] += 1
            elif 'lent' in filename:
                type_counts['careme'] += 1
            elif 'advent' in filename:
                type_counts['avent'] += 1
            else:
                type_counts['autres'] += 1
        stats['counts']['temporal_types'] = dict(type_counts)

    if args.format == 'json':
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    else:
        print(f"{_h('Statistiques OrdoRomanum')}")
        print(f"{'='*50}")

        for dir_name, dir_stats in stats['directories'].items():
            print(f"{_lbl(dir_name)}:")
            print(f"  • {dir_stats['file_count']} fichiers")
            print(f"  • {dir_stats['total_size']:,} octets")

        if 'temporal_types' in stats['counts']:
            print(f"\n{_lbl('Répartition temporelle')}:")
            for type_name, count in stats['counts']['temporal_types'].items():
                print(f"  • {type_name}: {count}")


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


def cmd_ordinarium(args: argparse.Namespace) -> None:
    date = datetime.strptime(args.date, "%Y-%m-%d")
    ordination = Ordination()
    fest = ordination.office(args.country, args.diocese, args.congregation, date)
    if args.format == 'json':
        print(json.dumps(to_serializable(fest), ensure_ascii=False, indent=2))
    else:
        text = _render_sanctoral(None, fest)
        _print_text(text)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="OrdoRomanum CLI - Interface Liturgique Interactive",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Exemples d'usage:
          python commandlines.py sanctoral 2025-01-13
          python commandlines.py temporal 2025-04-20 --format json
          python commandlines.py calendar 2025
          python commandlines.py search saint
          python commandlines.py stats
          python commandlines.py (mode interactif)
        """
    )

    # Configuration globale
    parser.add_argument("--format", choices=["text", "json"], default="text",
                       help="Format de sortie")
    parser.add_argument("--color", choices=["auto", "on", "off"], default="auto",
                       help="Couleur en sortie texte")
    parser.add_argument("--debug", action="store_true",
                       help="Mode debug")

    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    # Commandes principales (sans arguments requis)
    subparsers.add_parser("stats", help="Statistiques du système")
    subparsers.add_parser("build-indexes", help="Construire les index")

    # Commandes avec arguments requis
    sanctoral_parser = subparsers.add_parser("sanctoral", help="Fête sanctorale")
    sanctoral_parser.add_argument("date", help="Date (YYYY-MM-DD)")

    temporal_parser = subparsers.add_parser("temporal", help="Fiche temporelle")
    temporal_parser.add_argument("date", help="Date (YYYY-MM-DD)")

    calendar_parser = subparsers.add_parser("calendar", help="Calendrier liturgique")
    calendar_parser.add_argument("year", help="Année liturgique")

    search_parser = subparsers.add_parser("search", help="Recherche")
    search_parser.add_argument("query", help="Terme à rechercher")

    colors_parser = subparsers.add_parser("colors", help="Couleur liturgique")
    colors_parser.add_argument("id", help="ID de couleur")

    category_parser = subparsers.add_parser("category", help="Catégorie")
    category_parser.add_argument("id", help="ID de catégorie")

    ordinarium_parser = subparsers.add_parser("ordinarium", help="Calcul ordinarium")
    ordinarium_parser.add_argument("date", help="Date (YYYY-MM-DD)")
    ordinarium_parser.add_argument("--country", default="FR", help="Pays")
    ordinarium_parser.add_argument("--diocese", default="", help="Diocèse")
    ordinarium_parser.add_argument("--congregation", default="", help="Congrégation")

    args = parser.parse_args()

    # Configuration couleur/debug
    global USE_COLOR, DEBUG
    if getattr(args, 'format', 'text') == 'json':
        USE_COLOR = False
    elif getattr(args, 'color', 'auto') == 'on':
        USE_COLOR = True
    elif getattr(args, 'color', 'auto') == 'off':
        USE_COLOR = False
    else:  # auto
        USE_COLOR = sys.stdout.isatty()
    DEBUG = bool(getattr(args, 'debug', False))

    # Si aucun argument, mode interactif
    if len(sys.argv) == 1:
        try:
            interactive_mode()
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir !")
        except Exception as e:
            print(f"\n Erreur dans le mode interactif: {e}")
            print("💡 Utilisez 'python commandlines.py --help' pour l'aide")
        return

    # Commandes avec arguments requis
    if hasattr(args, 'command') and args.command in ['sanctoral', 'temporal', 'calendar', 'search', 'colors', 'category', 'ordinarium']:
        # Vérifier que les arguments requis sont présents
        required_args = {
            'sanctoral': 'date',
            'temporal': 'date',
            'calendar': 'year',
            'search': 'query',
            'colors': 'id',
            'category': 'id',
            'ordinarium': 'date'
        }

        required_arg = required_args.get(args.command)
        if required_arg and not hasattr(args, required_arg):
            parser.error(f"Argument requis manquant: --{required_arg}")
        elif required_arg and not getattr(args, required_arg):
            parser.error(f"Argument requis manquant: --{required_arg}")

    # Routing vers les méthodes appropriées
    command_map = {
        'sanctoral': cmd_sanctoral,
        'temporal': cmd_temporal,
        'calendar': cmd_calendar,
        'search': cmd_search,
        'stats': cmd_stats,
        'build-indexes': cmd_build_indexes,
        'colors': cmd_colors,
        'category': cmd_category,
        'ordinarium': cmd_ordinarium,
    }

    if args.command in command_map:
        try:
            command_map[args.command](args)
        except Exception as e:
            print(f"Erreur lors de l'exécution: {e}")
            if DEBUG:
                raise
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
