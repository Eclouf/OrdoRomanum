import argparse
from pathlib import Path
from datetime import datetime
import json

# Import dynamique sans dépendre du PYTHONPATH en supposant exécution à la racine du projet
import importlib.util

BASE_DIR = Path(__file__).resolve().parents[1]
CALENDAR_PATH = BASE_DIR / "controllers" / "CalendarCtrl.py"
OUTPUT_ROOT = BASE_DIR / "models" / "fr" / "Temporal"

TEMPLATE = """#title: {title}
#date: 
    ##day: {day}
    ##month: {month}
#degree: 
#category: 
#rank: 
#type: Temporal
#color: 


#martirologe:


#office: 
    ##common: 
    ##matins: 
    ##laudes: 
    ##prime: 
    ##terce: 
    ##sext: 
    ##none: 
    ##vespers: 
    ##compline: 


#messe: 
    ##commemoration: 
    ##gloria: 
    ##credo:
    
#notes:

.
"""


def load_calendar_class():
    spec = importlib.util.spec_from_file_location("controllers.CalendarCtrl", CALENDAR_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)  # type: ignore
    # CalendarRom is defined in the module
    return getattr(mod, "CalendarRom")


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def date_to_paths(dt: datetime) -> tuple[Path, str]:
    mm = f"{dt.month:02d}"
    dd = f"{dt.day:02d}"
    dir_path = OUTPUT_ROOT / mm
    file_name = f"{dd}-{mm}.txt"  # DD-MM pour cohérence visuelle
    return dir_path, file_name


def default_title_for_bucket(bucket: str, index: int | None = None) -> str:
    names = {
        "cycle_chrismas": "Temps de l'Avent/Noël",
        "cycle_epiphany": "Dimanche après l'Épiphanie",
        "cycle_lent": "Temps de la Septuagésime/Carême",
        "cycle_easter": "Temps Pascal",
        "cycle_pentecote": "Dimanche après la Pentecôte",
    }
    base = names.get(bucket, "Temporal")
    if index is not None:
        return f"{base} {index}"
    return base


def collect_dates_for_year(year: int):
    CalendarRom = load_calendar_class()
    cal = CalendarRom()
    cy_chr, cy_epi, cy_lent, cy_easter, cy_pent = cal.liturgical_year(year)
    # Chaque cycle est un dict {datetime: ''}
    buckets = {
        "cycle_chrismas": cy_chr,
        "cycle_epiphany": cy_epi,
        "cycle_lent": cy_lent,
        "cycle_easter": cy_easter,
        "cycle_pentecote": cy_pent,
    }
    return buckets


def generate_files(year: int, overwrite: bool = False, dry_run: bool = False) -> dict:
    buckets = collect_dates_for_year(year)
    mapping = {}

    for bucket_name, dct in buckets.items():
        # Dictionnaire non ordonné, on trie par date
        for idx, dt in enumerate(sorted(dct.keys())):
            dir_path, file_name = date_to_paths(dt)
            file_path = dir_path / file_name
            title = default_title_for_bucket(bucket_name, idx + 1 if bucket_name != "cycle_chrismas" else None)

            mapping_key = dt.strftime("%Y-%m-%d")
            mapping[mapping_key] = {
                "bucket": bucket_name,
                "path": str(file_path.relative_to(OUTPUT_ROOT)),
                "suggested_title": title,
            }

            if dry_run:
                continue

            ensure_dir(dir_path)
            if file_path.exists() and not overwrite:
                # Ne pas écraser, on laisse tel quel
                continue

            content = TEMPLATE.format(title=title, day=f"{dt.day}", month=f"{dt.month}")
            file_path.write_text(content, encoding="utf-8")

    return mapping


def write_mapping(year: int, mapping: dict, dry_run: bool = False):
    out_json = OUTPUT_ROOT / f"mapping_dates_{year}.json"
    ensure_dir(out_json.parent)
    data = json.dumps(mapping, ensure_ascii=False, indent=2)
    if not dry_run:
        out_json.write_text(data, encoding="utf-8")
    return out_json


def main():
    parser = argparse.ArgumentParser(description="Générer des fiches Temporal depuis CalendarCtrl pour une année donnée")
    parser.add_argument("year", type=int, help="Année (ex: 2025)")
    parser.add_argument("--overwrite", action="store_true", help="Écraser les fiches existantes")
    parser.add_argument("--dry-run", action="store_true", help="Aucun fichier écrit, seulement le mapping JSON")
    args = parser.parse_args()

    mapping = generate_files(args.year, overwrite=args.overwrite, dry_run=args.dry_run)
    out_json = write_mapping(args.year, mapping, dry_run=args.dry_run)

    print(f"Génération terminée pour {args.year}.")
    print(f"Mapping écrit dans: {out_json}")
    if args.dry_run:
        print("Dry-run: aucun fichier .txt créé.")


if __name__ == "__main__":
    main()
