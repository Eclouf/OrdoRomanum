#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour formater les fichiers des dimanches après la Pentecôte.
Pour chaque fichier sun_pentecost_XX.txt dans models/fr/Temporal/,
met à jour le titre pour "XXe Dimanche après la Pentecôte" et applique le format standard.
"""

import os
import re
from pathlib import Path

# Chemin du répertoire Temporal
TEMPORAL_DIR = Path('models/fr/Temporal')

# Template complet pour le format standard
TEMPLATE = """#title: {title}
#degree: 2
#category:
#occ: D2
#con: D2
#rank:
#type: Temporal
#color: 2

#office:
    ##common: per Annunm
    ##matins:
    ##laudes:
    ##prime: Psaume 117
    ##terce:
    ##sext:
    ##none:
    ##vespers:
    ##compline:


#messe: Propre:
    ##commemoration:
    ##gloria: oui
    ##credo:
    ##preface: de la Très Sainte Trinité

#notes:
"""

def format_sunday_file(filepath: Path) -> None:
    """Formatte et complète un fichier de dimanche après la Pentecôte."""
    # Extraire le numéro du nom de fichier
    filename = filepath.name
    match = re.match(r'sun_pentecost_(\d+)\.txt', filename)
    if not match:
        print(f"Ignoré: {filename} (ne correspond pas au pattern)")
        return

    numero = int(match.group(1))
    title = f"{numero}e Dimanche après la Pentecôte"

    # Lire le contenu actuel
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Fichier manquant: {filepath}, création complète à partir du template")
        content = ""
        updated_content = TEMPLATE.format(title=title)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Créé: {filename} -> {title}")
        return

    # Remplacer ou ajouter les lignes selon le template
    lines = content.split('\n')
    updated_lines = []
    template_lines = TEMPLATE.format(title=title).split('\n')

    # Parcourir le template et utiliser les lignes existantes si elles correspondent exactement
    for template_line in template_lines:
        if template_line.strip():  # Si la ligne n'est pas vide
            # Chercher une ligne existante qui commence de la même façon
            matching_line = None
            for line in lines:
                if line.startswith(template_line.split(':')[0] + ':'):
                    # Remplacer si la ligne existante est incomplète (valeur vide après :)
                    key = template_line.split(':')[0] + ':'
                    if line.strip() == key or not line.split(':', 1)[1].strip():
                        matching_line = template_line  # Utiliser la template
                    else:
                        matching_line = line  # Garder la ligne existante si elle a une valeur
                    break
            if matching_line:
                updated_lines.append(matching_line)
            else:
                updated_lines.append(template_line)
        else:
            updated_lines.append(template_line)

    # Ajouter les lignes restantes du fichier original si elles ne sont pas dans le template et ne sont pas vides/incomplètes
    for line in lines:
        if line not in updated_lines and line.strip():
            # Vérifier si la ligne est incomplète (pas de valeur après :)
            if ':' in line:
                key, value = line.split(':', 1)
                if not value.strip():
                    continue  # Ne pas ajouter les lignes incomplètes
            updated_lines.append(line)

    # Reconstruire le contenu
    updated_content = '\n'.join(updated_lines)

    # Écrire le fichier
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Complété: {filename} -> {title}")

def main():
    """Point d'entrée principal."""
    if not TEMPORAL_DIR.exists():
        print(f"Répertoire {TEMPORAL_DIR} introuvable.")
        return

    # Lister et traiter les fichiers
    for filepath in TEMPORAL_DIR.glob('sun_pentecost_*.txt'):
        format_sunday_file(filepath)

    print("Formatage terminé.")

if __name__ == "__main__":
    main()
