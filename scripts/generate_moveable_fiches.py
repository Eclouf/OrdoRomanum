import argparse
from pathlib import Path
from datetime import datetime, timedelta
import json
import importlib.util

BASE_DIR = Path(__file__).resolve().parents[1]
CALENDAR_PATH = BASE_DIR / "controllers" / "CalendarCtrl.py"
MOVEABLE_DIR = BASE_DIR / "models" / "fr" / "Temporal"

TEMPLATE = """#title: {title}
#date: 
    ##day: 
    ##month: 
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


def load_calendar():
    spec = importlib.util.spec_from_file_location("controllers.CalendarCtrl", CALENDAR_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)  # type: ignore
    CalendarRom = getattr(mod, "CalendarRom")
    return CalendarRom()


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def weekday_fr(dt: datetime) -> str:
    return ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"][dt.weekday()]


def slugify(label: str) -> str:
    s = label.lower()
    repl = {
        " ": "-",
        "'": "",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a",
        "î": "i", "ï": "i",
        "ô": "o",
        "ù": "u", "û": "u",
        "ç": "c",
        ",": "", ".": "", ":": "", ";": "", "!": "", "?": "",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    s = ''.join(ch for ch in s if (ch.isalnum() or ch == '-'))
    s = '-'.join(filter(None, s.split('-')))
    return s


def name_for_lent(easter: datetime, dt: datetime) -> tuple[str, str]:
    d = (easter - dt).days
    # Fixed pre-Lent
    if d == 63:
        return "septuagesime", "Septuagésime"
    if d == 56:
        return "sexagesime", "Sexagésime"
    if d == 49:
        return "quinquagesime", "Quinquagésime"
    if d == 46:
        return "ash-wednesday", "Mercredi des Cendres"
    # Ember days in Lent (Wed/Fri/Sat before 1st Sunday)
    if d in (39, 37, 36):
        wd = weekday_fr(dt)
        return f"ember-lent-{wd}", f"Quatre-Temps de Carême ({wd.capitalize()})"
    # Sundays of Lent
    if 7 <= d <= 42 and dt.weekday() == 6:
        n = (42 - d) // 7 + 1
        return f"lent-sunday-{n}", f"{n}e dimanche de Carême" if n != 1 else "1er dimanche de Carême"
    # Weekdays of Lent
    return f"lent-{d}-days-before-easter", f"Jour de Carême (J-{d} Pâques)"


def name_for_easter_cycle(easter: datetime, dt: datetime) -> tuple[str, str]:
    d = (dt - easter).days
    if d == 0:
        return "easter", "Dimanche de Pâques"
    if 1 <= d <= 6:
        names = [
            "Lundi de l'Octave de Pâques",
            "Mardi de l'Octave de Pâques",
            "Mercredi de l'Octave de Pâques",
            "Jeudi de l'Octave de Pâques",
            "Vendredi de l'Octave de Pâques",
            "Samedi de l'Octave de Pâques",
        ]
        return f"easter-octave-day-{d}", names[d-1]
    if d == 7:
        return "quasimodo", "Dimanche in Albis (Quasimodo)"
    if d in (36, 37, 38):
        # Minor Rogations before Ascension: Monday..Wednesday
        names = {36: "Lundi des Rogations", 37: "Mardi des Rogations", 38: "Mercredi des Rogations"}
        return f"rogations-{d-35}", names[d]
    if d == 39:
        return "ascension", "Ascension du Seigneur"
    if d == 42 and dt.weekday() == 6:
        return "sunday-after-ascension", "Dimanche après l'Ascension"
    return f"easter-cycle-day-{d}", f"Jour du Temps Pascal (J+{d} Pâques)"


def name_for_pentecost(easter: datetime, dt: datetime) -> tuple[str, str]:
    pentecost = easter + timedelta(days=49)
    d = (dt - pentecost).days
    if d == 0:
        return "pentecost", "Pentecôte"
    if d in (3, 5, 6):
        wd = weekday_fr(dt)
        return f"ember-pentecost-{wd}", f"Quatre-Temps de Pentecôte ({wd.capitalize()})"
    if d == 11:
        return "corpus-christi", "Fête-Dieu (Corpus Christi)"
    # Sundays after Pentecost
    if dt.weekday() == 6 and d > 0:
        n = d // 7 + 1
        return f"sunday-after-pentecost-{n}", f"{n}e dimanche après la Pentecôte" if n != 1 else "1er dimanche après la Pentecôte"
    return f"pentecost-cycle-day-{d}", f"Jour du Temps après la Pentecôte (J+{d} Pentecôte)"


def name_for_epiphany(year: int, dt: datetime, cycle_epiphany: dict) -> tuple[str, str]:
    epiphany = datetime(year, 1, 6)
    # Holy Family is the first entry in cycle_epiphany
    sundays_sorted = sorted(cycle_epiphany.keys())
    if sundays_sorted and dt == sundays_sorted[0]:
        return "holy-family", "Fête de la Sainte Famille"
    # Other Sundays after Epiphany
    n = sundays_sorted.index(dt) + 1 if dt in sundays_sorted else None
    if n is not None:
        return f"sunday-after-epiphany-{n}", f"{n}e dimanche après l'Épiphanie" if n != 1 else "1er dimanche après l'Épiphanie"
    return "epiphany-cycle", "Temps après l'Épiphanie"


def name_for_chrismas(year: int, dt: datetime, cycle_chrismas: dict) -> tuple[str, str]:
    # Try to label Advent Sundays 1..4; others as ember days if Wed/Fri/Sat (approx)
    sundays = sorted([d for d in cycle_chrismas.keys() if d.weekday() == 6])
    if dt in sundays:
        n = sundays.index(dt) + 1
        return f"advent-sunday-{n}", f"{n}e dimanche de l'Avent" if n != 1 else "1er dimanche de l'Avent"
    # Ember days (approx): Wed/Fri/Sat entries in the cycle
    if dt in cycle_chrismas:
        wd = weekday_fr(dt)
        return f"ember-advent-{wd}", f"Quatre-Temps de l'Avent ({wd.capitalize()})"
    return "advent-christmas-cycle", "Temps de l'Avent/Noël"


def build_mapping_for_year(year: int) -> dict:
    cal = load_calendar()
    cy_chr, cy_epi, cy_lent, cy_easter, cy_pent = cal.liturgical_year(year)
    easter = None
    # easter is not directly returned; recompute like in the class
    # We'll infer from keys: easter is the min date in cycle_easter with comment easter
    easter = min(cy_easter.keys())

    mapping: dict[str, dict] = {}

    # Christmas/Advent
    for dt in sorted(cy_chr.keys()):
        slug, title = name_for_chrismas(year, dt, cy_chr)
        mapping[dt.strftime("%Y-%m-%d")] = {"slug": slug, "title": title}

    # Epiphany cycle
    for dt in sorted(cy_epi.keys()):
        slug, title = name_for_epiphany(year, dt, cy_epi)
        mapping[dt.strftime("%Y-%m-%d")] = {"slug": slug, "title": title}

    # Lent
    for dt in sorted(cy_lent.keys()):
        slug, title = name_for_lent(easter, dt)
        mapping[dt.strftime("%Y-%m-%d")] = {"slug": slug, "title": title}

    # Easter cycle
    for dt in sorted(cy_easter.keys()):
        slug, title = name_for_easter_cycle(easter, dt)
        mapping[dt.strftime("%Y-%m-%d")] = {"slug": slug, "title": title}

    # Pentecost
    for dt in sorted(cy_pent.keys()):
        slug, title = name_for_pentecost(easter, dt)
        mapping[dt.strftime("%Y-%m-%d")] = {"slug": slug, "title": title}

    return mapping


def write_fiches_from_mapping(mapping: dict, overwrite: bool = False, dry_run: bool = False):
    ensure_dir(MOVEABLE_DIR)
    created, skipped = 0, 0
    for info in mapping.values():
        slug = info["slug"]
        title = info["title"]
        path = MOVEABLE_DIR / f"{slug}.txt"
        if path.exists() and not overwrite:
            skipped += 1
            continue
        if not dry_run:
            path.write_text(TEMPLATE.format(title=title), encoding="utf-8")
        created += 1
    return created, skipped


def write_mapping_json(year: int, mapping: dict, dry_run: bool = False):
    out = MOVEABLE_DIR / f"mapping_moveable_{year}.json"
    data = json.dumps(mapping, ensure_ascii=False, indent=2)
    if not dry_run:
        out.write_text(data, encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="Génère des fiches 'moveable' (indépendantes de l'année) et un mapping date→slug pour l'année donnée")
    parser.add_argument("year", type=int, help="Année")
    parser.add_argument("--overwrite", action="store_true", help="Écraser les fiches existantes")
    parser.add_argument("--dry-run", action="store_true", help="Ne rien écrire, seulement afficher où et quoi")
    args = parser.parse_args()

    mapping = build_mapping_for_year(args.year)

    created, skipped = write_fiches_from_mapping(mapping, overwrite=args.overwrite, dry_run=args.dry_run)
    out_json = write_mapping_json(args.year, mapping, dry_run=args.dry_run)

    print(f"Fiches créées: {created} | Fiches inchangées: {skipped}")
    print(f"Mapping écrit: {out_json}")
    if args.dry_run:
        print("Dry-run: aucun fichier créé.")


if __name__ == "__main__":
    main()
