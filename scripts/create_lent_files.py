#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script pour créer les fichiers Temporal correspondant aux nouveaux noms de jours de Carême.
Remplace l'ancien système de nommage par le nouveau système structuré.
"""

import os
from datetime import datetime, timedelta
from pathlib import Path

# Chemin du répertoire Temporal
TEMPORAL_DIR = Path('models/fr/Temporal')

# Template pour les jours de Carême (lundi à samedi)
LENT_WEEKDAY_TEMPLATE = """#title: {title}
#degree: 3
#category:
#occ: f3
#con: f3
#rank:
#type: Temporal
#color: 3

#office:
    ##common: Du temps de Carême.
    ##matins:
    ##laudes: Laudes II
    ##prime:
    ##terce:
    ##sext:
    ##none:
    ##vespers:
    ##compline:


#messe: Propre:
    ##commemoration:
    ##gloria:
    ##credo:
    ##preface: du Carême

#notes:
"""

# Template pour les dimanches de Carême
LENT_SUNDAY_TEMPLATE = """#title: {title}
#degree: 3
#category:
#occ: f3
#con: f3
#rank:
#type: Temporal
#color: 3

#office:
    ##common: Du temps de Carême.
    ##matins:
    ##laudes: Laudes II
    ##prime:
    ##terce:
    ##sext:
    ##none:
    ##vespers:
    ##compline:


#messe: Propre:
    ##commemoration:
    ##gloria:
    ##credo:
    ##preface: du Carême

#notes:
"""

# Template pour les jours après les Cendres
ASH_DAYS_TEMPLATE = """#title: {title}
#degree: 3
#category:
#occ: f3
#con: f3
#rank:
#type: Temporal
#color: 3

#office:
    ##common: Du temps de Carême.
    ##matins:
    ##laudes: Laudes II
    ##prime:
    ##terce:
    ##sext:
    ##none:
    ##vespers:
    ##compline:


#messe: Propre:
    ##commemoration:
    ##gloria:
    ##credo:
    ##preface: du Carême

#notes:
"""

def create_lent_files():
    """Crée tous les fichiers Temporal pour le cycle de Carême."""

    if not TEMPORAL_DIR.exists():
        print(f"Répertoire {TEMPORAL_DIR} introuvable.")
        return

    # Liste des jours à créer
    days_to_create = []

    # Jours après les Cendres
    days_to_create.extend([
        ('ash_thursday', 'Jeudi après les Cendres'),
        ('ash_friday', 'Vendredi après les Cendres'),
        ('ash_saturday', 'Samedi après les Cendres'),
    ])

    # Jours de semaine pour les 6 semaines de Carême
    for week in range(1, 7):
        days_to_create.extend([
            (f'mon_lent_{week}', f'Lundi de la {week}e semaine de Carême'),
            (f'tue_lent_{week}', f'Mardi de la {week}e semaine de Carême'),
            (f'wed_lent_{week}', f'Mercredi de la {week}e semaine de Carême'),
            (f'thu_lent_{week}', f'Jeudi de la {week}e semaine de Carême'),
            (f'fri_lent_{week}', f'Vendredi de la {week}e semaine de Carême'),
            (f'sat_lent_{week}', f'Samedi de la {week}e semaine de Carême'),
        ])

    # Dimanches de Carême
    for week in range(1, 7):
        days_to_create.append((f'sun_lent_{week}', f'{week}e Dimanche de Carême'))

    # Créer les fichiers
    for filename, title in days_to_create:
        filepath = TEMPORAL_DIR / f'{filename}.txt'

        # Choisir le bon template
        if filename.startswith('sun_lent_'):
            template = LENT_SUNDAY_TEMPLATE
        elif filename in ['ash_thursday', 'ash_friday', 'ash_saturday']:
            template = ASH_DAYS_TEMPLATE
        else:
            template = LENT_WEEKDAY_TEMPLATE

        # Créer le contenu
        content = template.format(title=title)

        # Écrire le fichier
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Créé: {filename}.txt -> {title}")

def main():
    """Point d'entrée principal."""
    print("Création des fichiers Temporal pour le cycle de Carême...")
    create_lent_files()
    print("Création terminée.")

if __name__ == "__main__":
    main()
