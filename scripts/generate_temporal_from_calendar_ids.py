import argparse
from pathlib import Path
from datetime import datetime, timedelta
import importlib.util
import json

BASE_DIR = Path(__file__).resolve().parents[1]
CALENDAR_PATH = BASE_DIR / "controllers" / "CalendarCtrl.py"
OUTPUT_DIR = BASE_DIR / "models" / "fr" / "Temporal"

TEMPLATE = """#title: 
#degree: 
#category: 
#rank: 
#type: Temporal
#color: 

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
    ##preface:
    
#notes:

.
"""

def load_calendar_class():
    spec = importlib.util.spec_from_file_location("controllers.CalendarCtrl", CALENDAR_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)  # type: ignore
    return getattr(mod, "CalendarRom")


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def weekday_code(dt: datetime) -> str:
    return ["mon", "tue", "wed", "thu", "fri", "sat", "sun"][dt.weekday()]


def build_ids_for_year(year: int) -> dict[str, str]:
    """
    Build mapping date->ID by reading values directly from CalendarCtrl dictionaries.
    If an ID is empty for known Ember days, auto-correct with standard IDs.
    Otherwise, skip empty values.
    """
    CalendarRom = load_calendar_class()
    cal = CalendarRom()
    cy_chr, cy_epi, cy_lent, cy_easter, cy_pent = cal.liturgical_year(year)

    # Infer reference dates
    easter = min(cy_easter.keys())
    pentecost = easter + timedelta(days=49)

    date_to_id: dict[str, str] = {}

    def set_id(dt: datetime, val: object):
        iso = dt.strftime("%Y-%m-%d")
        if isinstance(val, str) and val.strip():
            date_to_id[iso] = val.strip()
        elif isinstance(val, (int, float)):
            date_to_id[iso] = str(val)
        else:
            # Try to correct Ember days if value is empty
            wd = weekday_code(dt)
            # Advent Ember: any Wed/Fri/Sat in Advent cycle with empty value
            if dt in cy_chr and wd in ("wed", "fri", "sat"):
                date_to_id[iso] = f"ember_advent_{wd}"
                return
            # Lent Ember: offsets 39,37,36 before Easter
            d_before = (easter - dt).days
            if dt in cy_lent and d_before in (39, 37, 36):
                date_to_id[iso] = f"ember_lent_{wd}"
                return
            # Ember after Pentecost: +3, +5, +6 days
            d_after_pent = (dt - pentecost).days
            if dt in cy_pent and d_after_pent in (3, 5, 6):
                date_to_id[iso] = f"ember_pentecost_{wd}"
                return
            # September Ember: any Wed/Fri/Sat in September computed block
            if dt in cy_pent and dt.month == 9 and wd in ("wed", "fri", "sat"):
                date_to_id[iso] = f"ember_september_{wd}"
                return
            # Otherwise, leave unmapped (no fiche for empty ID)
            return

    # Collect from all cycles
    for dt, v in cy_chr.items():
        set_id(dt, v)
    for dt, v in cy_epi.items():
        set_id(dt, v)
    for dt, v in cy_lent.items():
        set_id(dt, v)
    for dt, v in cy_easter.items():
        set_id(dt, v)
    for dt, v in cy_pent.items():
        set_id(dt, v)

    return date_to_id


def build_ids_for_year_range(start_year: int, end_year: int) -> set[str]:
    ids: set[str] = set()
    for y in range(start_year, end_year + 1):
        by_date = build_ids_for_year(y)
        ids.update(by_date.values())
    return ids


def write_fiches_from_ids(ids: set[str], overwrite: bool = False, dry_run: bool = False) -> tuple[int, int]:
    ensure_dir(OUTPUT_DIR)
    created = skipped = 0
    for id_ in sorted(ids):
        path = OUTPUT_DIR / f"{id_}.txt"
        if path.exists() and not overwrite:
            skipped += 1
            continue
        if not dry_run:
            path.write_text(TEMPLATE, encoding="utf-8")
        created += 1
    return created, skipped


def write_mapping_json(year: int, date_to_id: dict[str, str], dry_run: bool = False) -> Path:
    out = OUTPUT_DIR / f"mapping_temporal_{year}.json"
    data = json.dumps(date_to_id, ensure_ascii=False, indent=2)
    if not dry_run:
        out.write_text(data, encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="Générer un jeu FIXE de fiches Temporal <id>.txt à partir des dictionnaires du calendrier (union d'un intervalle d'années), en corrigeant les IDs de Quatre-Temps manquants.")
    parser.add_argument("--years", type=str, default="1900:2100", help="Intervalle d'années à scanner pour collecter tous les IDs (ex: 1900:2100)")
    parser.add_argument("--overwrite", action="store_true", help="Écraser les fiches existantes")
    parser.add_argument("--dry-run", action="store_true", help="Ne pas écrire les fichiers, seulement afficher")
    parser.add_argument("--write-mapping-for", type=int, default=0, help="Optionnel: écrire aussi un mapping date->ID pour une année donnée")
    args = parser.parse_args()

    # Parse year range
    try:
        start_s, end_s = args.years.split(":")
        start_y, end_y = int(start_s), int(end_s)
    except Exception:
        raise SystemExit("--years doit être au format 'YYYY:YYYY', ex: 1900:2100")

    ids = build_ids_for_year_range(start_y, end_y)
    print(f"IDs uniques trouvés sur [{start_y}, {end_y}]: {len(ids)}")
    created, skipped = write_fiches_from_ids(ids, overwrite=args.overwrite, dry_run=args.dry_run)
    print(f"Fiches créées: {created} | Fiches inchangées: {skipped}")

    if args.write_mapping_for:
        date_to_id = build_ids_for_year(args.write_mapping_for)
        out_json = write_mapping_json(args.write_mapping_for, date_to_id, dry_run=args.dry_run)
        print(f"Mapping écrit: {out_json}")
    if args.dry_run:
        print("Dry-run: aucun fichier créé.")


if __name__ == "__main__":
    main()
