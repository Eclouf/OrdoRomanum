import argparse
from pathlib import Path
from typing import List, Tuple, Dict

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "models" / "fr" / "Temporal" / "Moveable"

# Canonical, year-independent slugs with suggested French titles
STABLE_ENTRIES: List[Tuple[str, str]] = [
    # Advent
    ("advent-sunday-1", "1er dimanche de l'Avent"),
    ("advent-sunday-2", "2e dimanche de l'Avent"),
    ("advent-sunday-3", "3e dimanche de l'Avent"),
    ("advent-sunday-4", "4e dimanche de l'Avent"),
    ("ember-advent-wednesday", "Quatre-Temps de l'Avent (Mercredi)"),
    ("ember-advent-friday", "Quatre-Temps de l'Avent (Vendredi)"),
    ("ember-advent-saturday", "Quatre-Temps de l'Avent (Samedi)"),
    ("christmas", "Nativité du Seigneur (Noël)"),

    # After Epiphany
    ("epiphany", "Épiphanie du Seigneur"),
    ("holy-family", "Fête de la Sainte Famille"),
    ("sunday-after-epiphany-1", "1er dimanche après l'Épiphanie"),
    ("sunday-after-epiphany-2", "2e dimanche après l'Épiphanie"),
    ("sunday-after-epiphany-3", "3e dimanche après l'Épiphanie"),
    ("sunday-after-epiphany-4", "4e dimanche après l'Épiphanie"),
    ("sunday-after-epiphany-5", "5e dimanche après l'Épiphanie"),

    # Pre-Lent and Lent
    ("septuagesime", "Septuagésime"),
    ("sexagesime", "Sexagésime"),
    ("quinquagesime", "Quinquagésime"),
    ("ash-wednesday", "Mercredi des Cendres"),
    ("ember-lent-wednesday", "Quatre-Temps de Carême (Mercredi)"),
    ("ember-lent-friday", "Quatre-Temps de Carême (Vendredi)"),
    ("ember-lent-saturday", "Quatre-Temps de Carême (Samedi)"),
    ("lent-sunday-1", "1er dimanche de Carême"),
    ("lent-sunday-2", "2e dimanche de Carême"),
    ("lent-sunday-3", "3e dimanche de Carême"),
    ("lent-sunday-4", "4e dimanche de Carême (Lætare)"),
    ("lent-sunday-5", "Dimanche de la Passion"),
    ("lent-sunday-6", "Dimanche des Rameaux"),

    # Eastertide
    ("easter", "Dimanche de Pâques"),
    ("easter-octave-day-1", "Lundi de l'Octave de Pâques"),
    ("easter-octave-day-2", "Mardi de l'Octave de Pâques"),
    ("easter-octave-day-3", "Mercredi de l'Octave de Pâques"),
    ("easter-octave-day-4", "Jeudi de l'Octave de Pâques"),
    ("easter-octave-day-5", "Vendredi de l'Octave de Pâques"),
    ("easter-octave-day-6", "Samedi de l'Octave de Pâques"),
    ("quasimodo", "Dimanche in Albis (Quasimodo)"),
    ("rogations-1", "Lundi des Rogations"),
    ("rogations-2", "Mardi des Rogations"),
    ("rogations-3", "Mercredi des Rogations"),
    ("ascension", "Ascension du Seigneur"),
    ("sunday-after-ascension", "Dimanche après l'Ascension"),

    # Pentecost cycle
    ("pentecost", "Pentecôte"),
    ("ember-pentecost-wednesday", "Quatre-Temps de Pentecôte (Mercredi)"),
    ("ember-pentecost-friday", "Quatre-Temps de Pentecôte (Vendredi)"),
    ("ember-pentecost-saturday", "Quatre-Temps de Pentecôte (Samedi)"),
    ("corpus-christi", "Fête-Dieu (Corpus Christi)"),
]

# Add Sundays after Pentecost up to 28 (max case)
for n in range(1, 29):
    STABLE_ENTRIES.append((f"sunday-after-pentecost-{n}", f"{n}e dimanche après la Pentecôte" if n != 1 else "1er dimanche après la Pentecôte"))

# Ember days of September (after Exaltation of the Holy Cross)
STABLE_ENTRIES.extend([
    ("ember-september-wednesday", "Quatre-Temps de Septembre (Mercredi)"),
    ("ember-september-friday", "Quatre-Temps de Septembre (Vendredi)"),
    ("ember-september-saturday", "Quatre-Temps de Septembre (Samedi)"),
])

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


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def create_all(overwrite: bool = False, dry_run: bool = False) -> Dict[str, str]:
    ensure_dir(OUTPUT_DIR)
    created, skipped = 0, 0
    catalog: Dict[str, str] = {}

    for slug, title in STABLE_ENTRIES:
        path = OUTPUT_DIR / f"{slug}.txt"
        catalog[slug] = str(path.relative_to(BASE_DIR))
        if path.exists() and not overwrite:
            skipped += 1
            continue
        if not dry_run:
            path.write_text(TEMPLATE.format(title=title), encoding="utf-8")
        created += 1

    # Save a catalog file to easily reference slugs from CalendarCtrl
    catalog_path = OUTPUT_DIR / "catalog_moveable.json"
    if not dry_run:
        import json
        catalog_data = {slug: {"title": title, "path": str((OUTPUT_DIR / f"{slug}.txt").relative_to(BASE_DIR))} for slug, title in STABLE_ENTRIES}
        catalog_path.write_text(json.dumps(catalog_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Fiches créées: {created} | Fiches inchangées: {skipped}")
    print(f"Catalogue: {catalog_path}")
    return catalog


def main():
    parser = argparse.ArgumentParser(description="Crée les fiches 'mobiles' avec des noms stables, indépendantes de l'année")
    parser.add_argument("--overwrite", action="store_true", help="Écraser les fiches existantes")
    parser.add_argument("--dry-run", action="store_true", help="Ne rien écrire, seulement compter")
    args = parser.parse_args()

    create_all(overwrite=args.overwrite, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
