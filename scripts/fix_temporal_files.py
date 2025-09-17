import argparse
import re
from pathlib import Path
from typing import Optional, Tuple, Dict, List, Set
import unicodedata

BASE_DIR = Path(__file__).resolve().parents[1]
TEMPORAL_DIR = BASE_DIR / "models" / "fr" / "Temporal"
CATEGORY_FILE = BASE_DIR / "models" / "fr" / "Category.txt"

CATEGORY_KEYS = ("#categorie", "#category")
TYPE_KEY = "#type"
COLOR_KEY = "#color"
TITLE_KEY = "#title"

line_re = re.compile(r"^(#\w+)\s*:\s*(.*)$")


def _norm(s: str) -> str:
    # Lower, strip accents, collapse spaces
    s = s.strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"\s+", " ", s)
    return s


def load_categories(path: Path) -> Tuple[Dict[int, str], Dict[str, int]]:
    id_to_label: Dict[int, str] = {}
    label_to_id: Dict[str, int] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            parts = re.split(r"\t+", line, maxsplit=1)
            if len(parts) != 2:
                continue
            try:
                idx = int(parts[0])
            except ValueError:
                continue
            label = parts[1].strip()
            id_to_label[idx] = label
            label_to_id[_norm(label)] = idx
    return id_to_label, label_to_id


def guess_label_from_title(title: str, existing_labels: List[str]) -> Optional[str]:
    if not title:
        return None
    tnorm = _norm(title)
    # Prefer longest matching existing label contained in title
    best_match = None
    for label in existing_labels:
        lnorm = _norm(label)
        if lnorm and lnorm in tnorm:
            if best_match is None or len(lnorm) > len(_norm(best_match)):
                best_match = label
    if best_match:
        return best_match
    # Heuristic synonyms from common words in titles
    synonyms = {
        "abbe": "Abbé",
        "pape": "Pape",
        "martyr": "Martyr",
        "martyrs": "Martyrs",
        "confesseur": "Confesseur",
        "confesseurs": "Confesseurs",
        "eveque": "Évêque",
        "eveques": "Évêques",
        "docteur": "Docteur de l'Église",
        "vierge": "Vierge",
        "vierges": "Vierges",
        "diacre": "Diacre, Confesseur et Docteur de l'Église",
        "reine": "Reine & Veuve",
        "veuve": "Veuve",
        "veuves": "Veuves",
        "empereur": "Empereur & Confesseur",
        "apotre": "Âpotre",
        "apôtres": "Âpotres",
        "apôtres": "Âpotres",
        "apôtres": "Âpotres",
        "apotreS": "Âpotres",
        "evangeliste": "Évangéliste",
        "penitente": "Pénitente",
    }
    for key, label in synonyms.items():
        if key in tnorm:
            return label
    return None


def process_text(content: str, label_to_id: Dict[str, int], id_to_label: Dict[int, str], new_labels: Set[str]) -> Tuple[str, bool]:
    lines = content.splitlines()

    # Capture original values (prefer the first occurrence)
    category_idx: Optional[int] = None
    category_key_found: Optional[str] = None
    category_val: Optional[str] = None

    type_idx: Optional[int] = None
    type_val: Optional[str] = None

    color_idx: Optional[int] = None
    title_idx: Optional[int] = None
    title_val: Optional[str] = None

    # First pass: find indices and original values
    for i, line in enumerate(lines):
        m = line_re.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        k_lower = key.lower()
        if k_lower in CATEGORY_KEYS and category_idx is None:
            category_idx = i
            category_key_found = key  # may be misspelled or correct
            category_val = val
        elif k_lower == TYPE_KEY and type_idx is None:
            type_idx = i
            type_val = val
        elif k_lower == COLOR_KEY and color_idx is None:
            color_idx = i
        elif k_lower == TITLE_KEY and title_idx is None:
            title_idx = i
            title_val = val

    changed = False

    # Ensure category key is corrected to #category (keeping current value for now)
    if category_idx is not None and category_key_found != "#category":
        # Replace just the key spelling
        old = lines[category_idx]
        # Preserve spacing around ':' by reconstructing with a single ': '
        current_val = category_val if category_val is not None else ""
        lines[category_idx] = f"#category: {current_val}".rstrip()
        changed = changed or (lines[category_idx] != old)
        category_key_found = "#category"

    # Ensure a category line exists even if previously missing
    if category_idx is None:
        insert_pos = type_idx if type_idx is not None else (title_idx if title_idx is not None else 0)
        lines.insert(insert_pos, "#category: ")
        category_idx = insert_pos
        category_val = ""
        changed = True

    # Empty the color value if present
    if color_idx is not None:
        if lines[color_idx] != "#color: ":
            lines[color_idx] = "#color: "
            changed = True

    # Resolve category to numeric ID, using current value or inferred from title
    current_cat = (category_val or "").strip()
    cat_id_str: Optional[str] = None

    # If already numeric, keep it
    if current_cat.isdigit():
        cat_id_str = current_cat
    else:
        # Determine a label: prefer explicit current value; else infer from title
        label_candidate = current_cat if current_cat else None
        if not label_candidate and title_val:
            label_candidate = guess_label_from_title(title_val, list(id_to_label.values()))

        if label_candidate:
            norm = _norm(label_candidate)
            if norm in label_to_id:
                cat_id_str = str(label_to_id[norm])
            else:
                # New label -> assign new ID later (after all files), but we need a temporary ID now
                new_labels.add(label_candidate.strip())
                # Tentative ID will be assigned after aggregation; leave blank for now
                cat_id_str = None

    # Update category line if we have a resolved ID or need to clear it
    desired_line = f"#category: {cat_id_str}".rstrip() if cat_id_str is not None else "#category: "
    if lines[category_idx] != desired_line:
        lines[category_idx] = desired_line
        changed = True

    return ("\n".join(lines) + ("\n" if content.endswith("\n") else ""), changed)


def process_file(path: Path, label_to_id: Dict[str, int], id_to_label: Dict[int, str], new_labels: Set[str], dry_run: bool = False) -> bool:
    original = path.read_text(encoding="utf-8")
    new_content, changed = process_text(original, label_to_id, id_to_label, new_labels)
    if changed and not dry_run:
        path.write_text(new_content, encoding="utf-8")
    return changed


def main():
    parser = argparse.ArgumentParser(description="Fix Temporal files: categorie->category, clear color, map category to numeric ID from Category.txt, infer from title if empty, append missing categories")
    parser.add_argument("--root", type=str, default=str(TEMPORAL_DIR), help="Path to models/fr/Temporal directory")
    parser.add_argument("--category-file", type=str, default=str(CATEGORY_FILE), help="Path to models/fr/Category.txt")
    parser.add_argument("--dry-run", action="store_true", help="Only report changes, do not write")
    args = parser.parse_args()

    temporal_dir = Path(args.root)
    if not temporal_dir.exists():
        raise SystemExit(f"Directory not found: {temporal_dir}")

    category_path = Path(args.category_file)
    id_to_label, label_to_id = load_categories(category_path)

    changed_files = 0
    scanned = 0
    new_labels: Set[str] = set()
    for path in temporal_dir.rglob("*.txt"):
        scanned += 1
        try:
            if process_file(path, label_to_id, id_to_label, new_labels, dry_run=args.dry_run):
                changed_files += 1
                print(f"Changed: {path}")
            else:
                print(f"OK:      {path}")
        except Exception as e:
            print(f"ERROR:   {path} -> {e}")

    # If there are new labels, append them to the Category.txt with new IDs
    appended = 0
    if new_labels:
        if args.dry_run:
            print("\nNew categories to append (dry-run):")
            for lbl in sorted(new_labels):
                print(f"- {lbl}")
        else:
            if not category_path.exists():
                category_path.parent.mkdir(parents=True, exist_ok=True)
                category_path.write_text("", encoding="utf-8")
            current_max = max(id_to_label.keys(), default=-1)
            lines_to_append = []
            for lbl in sorted(new_labels):
                n_lbl = _norm(lbl)
                if n_lbl in label_to_id:
                    continue  # was added in the meantime
                current_max += 1
                lines_to_append.append(f"{current_max}\t{lbl}")
                # Update maps so any subsequent runs can resolve
                id_to_label[current_max] = lbl
                label_to_id[n_lbl] = current_max
            if lines_to_append:
                with category_path.open("a", encoding="utf-8") as f:
                    for ln in lines_to_append:
                        f.write(ln + "\n")
                appended = len(lines_to_append)

    print("\nSummary:")
    print(f"Scanned: {scanned}")
    print(f"Changed: {changed_files}")
    if new_labels:
        if args.dry_run:
            print(f"Would append: {len(new_labels)} new labels")
        else:
            print(f"Appended: {appended} new labels to {category_path}")


if __name__ == "__main__":
    main()
