# Ad Majorem Dei Gloriam


from datetime import datetime, timedelta
import kalendar


# test:
# day_select = 17
# mois_select = 12
# annee = 2022
# D1 = dimanche de 1er classe
# f1 = ferie de 1er classe
# OU1 octave universelle de 1er classe
# FU1 = fete universelle de 1er classe
#
#
def calcul_kalendar(annee, day_select, mois_select):

    (
        mercredi_des_cendres,
        dim_carem_1,
        dim_carem_2,
        dim_carem_3,
        dim_carem_5,
        septuagesima,
        sexagesima,
        quinquagesima,
        dimanche_laetare,
        dimanche_des_rameaux,
        jeudi_saint,
        vendredi_saint,
        samedi_saint,
        paques,
        ascension,
        pentecote,
        dim_avent_1,
        dim_avent_2,
        dim_avent_3,
        dim_avent_4,
        noel,
        st_nom,
        dimanches_pent,
        sacre_coeur,
        nb_dim_pent,
        epiphanie,
        st_famille,
        dimanches_epi,
        nb_dim_epi,
        mer_q_tps_sep,
        ven_q_tps_sep,
        sam_q_tps_sep,
    ) = kalendar.calculer_dates_liturgiques(annee)

    # 'titre':,'degre':,'couleur':,'office':,'messe':,'note':
    year_litugique = {
        dim_avent_1: {
            "titre": "1ER DIMANCHE DE L’AVENT",
            "couleur": "violet",
            "office": "du Temps de l’Avent. Antiennes & Capitules propres. Matines : 1 Nocturne, 9 Pss. Laudes I.",
            "messe": "Messe propre (Ad Te levavi) : Credo. Préface. de la Très Sainte Trinité.",
            "note": None,
            "degre": "I",
            "ferie": ["III", 500],
            "rank": 2300,
        },
        dim_avent_2: {
            "titre": "2E DIMANCHE DE L’AVENT",
            "couleur": "violet",
            "office": "du Temps de l’Avent. Ant. & Capitules propres. Matines : 1 Noct., 9 Pss. Laudes I.",
            "messe": "Messe propre (Populus Sion) : Credo. Préf. de la Très Sainte Trinité.",
            "note": None,
            "degre": "I",
            "ferie": ["III", 500],
            "rank": 2300,
        },
        dim_avent_3: {
            "titre": "3E DIMANCHE DE L’AVENT, DIT DE “GAUDETE”",
            "couleur": "rose ou violet",
            "office": "du Temps de l’Avent. Ant. & Capitules propres. Matines : Invitatoire Prope est. 1 Noct., 9 Pss. Laudes I.",
            "messe": "Messe propre (Gaudete) : Credo. Préf. de la Très Sainte Trinité.",
            "note": "Orgues & Fleurs permises (pas de reliques néanmoins)",
            "degre": "I",
            "ferie": ["III", 500],
            "rank": 2300,
        },
        dim_avent_3 + timedelta(days=3): {
            },
        dim_avent_3 + timedelta(days=5): {
            },
        dim_avent_3 + timedelta(days=6): {
            },
        dim_avent_4: {
            "titre": "4E DIMANCHE DE L’AVENT",
            "couleur": "violet",
            "office": "du Temps de l’Avent. Ant. & Capitules propres. Matines : Invitatoire Prope est. 1 Noct., 9 Pss. Laudes I.",
            "messe": "Messe propre (Rorate, cæli) : Credo. Préf. de la Très Sainte Trinité.",
            "note": None,
            "degre": "I",
            "ferie": ["III", 500],
            "rank": 2300,
        },
        noel: {
            "titre": "NATIVITÉ DE NOTRE-SEIGNEUR JÉSUS-CHRIST",
            "degre": "I classe avec octave de II classe",
            "couleur": "blanc",
            "office": "Propre, Laudes après la messe de Minuit",
            "messe": "Messe de Minuit : Gloria. Credo. Préface & Communicantes de la Nativité.\nMesse de l'Aurore : Gloria. Mémoire de Ste Anastasie, martyre. Credo. Préface & Communicantes de la Nativité.\nMesse du Jour : Gloria. Credo. Préface & Communicantes de la Nativité.",
            "note": "2em Vêpres sans memoire.\nComplies : du dimanche, Ton de Noël",
            "rank": 2800,
        },
        st_nom: {
            "titre": "SAINT NOM DE JÉSUS",
            "degre": "II",
            "couleur": "blanc",
            "office": "propre. Matines : 3 Nocturnes & Te Deum.\nAntiennes & Pss. du dimanche aux Petites Heures.",
            "messe": "Messe propre (In nomine Jesu) : Gloria. Mém. pro Papa. Credo. Préf. Nativ. Comm. ordinaire.",
            "note": None,
            "rank": 1550,
        },
        epiphanie: {
            "titre": "ÉPIPHANIE DE NOTRE SEIGNEUR",
            "degre": "I",
            "couleur": "blanc",
            "office": "propre. Complies : du dim., Ton de l’Épiphanie.",
            "messe": "Messe propre (Ecce advenit) : Gloria. Credo. Préf. & Communicantes propres.",
            "note": "Messes des Défunts/Funérailles interdites.\nAnnonce des fêtes mobiles\nBénédiction des Maisons",
            "rank": 2600,
        },
        st_famille: {
            "titre": "SAINTE FAMILLE DE JÉSUS, MARIE & JOSEPH",
            "degre": "II",
            "couleur": "blanc",
            "office": "propre. Complies : doxologie Jesu tuis, à l’hymne.",
            "messe": "Messe propre (Exsultat) : Gloria. Mém. pro Papa. Credo. Préf. de l’Épiphanie.",
            "note": "SOLENNITÉ DE L’ÉPIPHANIE (1re cl. / Blanc), Messe (& Vêpres, si en public) comme à la fête, sans mémoire.",
            "rank": 1600,
        },
        dimanches_epi["dim_epi_2"]: {
            "titre": "2E DIMANCHE APRÈS L’ÉPIPHANIE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Omnis terra) : Gloria. Oraison pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        septuagesima: {
            "titre": "DIMANCHE DE LA SEPTUAGÉSIME",
            "degre": "II",
            "couleur": "violet",
            "office": "propre. Laudes II. Prime : Ps. LIII au lieu du CXVIIe ; leçon brève Dominus autem.",
            "messe": "Messe propre (Circumdederunt me) : Pas de Gloria. Mém. pro Papa. Trait. Credo. Préf. de la T. Ste Trinité.",
            "note": None,
            "rank": 1500,
        },
        sexagesima: {
            "titre": "DIMANCHE DE LA SEXAGÉSIME",
            "degre": "II",
            "couleur": "violet",
            "office": "propre. Laudes II. Prime : Ps. LIII ; leçon brève Dominus autem.",
            "messe": "Messe propre (Exsurge) : Pas de Gloria. Mém. pro Papa. Trait. Credo. Préf. de la T. Ste Trinité.",
            "note": None,
            "rank": 1500,
        },
        quinquagesima: {
            "titre": "DIMANCHE DE LA QUINQUAGÉSIME",
            "degre": "II",
            "couleur": "violet",
            "office": "propre. Laudes II. Prime : Ps. LIII ; leçon brève Dominus autem.",
            "messe": "Messe propre (Esto mihi). Pas de Gloria. Mém. pro Papa. Trait. Credo. Préf. de la T. Ste Trinité.",
            "note": None,
            "rank": 1500,
        },
        mercredi_des_cendres: {
            "titre": "MERCREDI DES CENDRES",
            "degre": "I",
            "couleur": "violet",
            "office": "per annum. Laudes II. Laudes/Vêpres : Prières fériales.",
            "messe": "Messe propre (Misereris). Mém. pro Papa. Préf. du Carême.",
            "note": "Bénédiction & Imposition des Cendres.",
            "rank": 2200,
        },
        dim_carem_1: {
            "titre": "1ER DIMANCHE DE CARÊME",
            "degre": "I",
            "couleur": "violet",
            "office": "dom. du Carême & propre. Laudes II. Ant. propres (sauf Vêpres). Prime : Ps. LIII.",
            "messe": "Messe propre (Invocabit me) : Mém. pro Papa. Credo. Préf. du Carême.",
            "note": "Imposition des Cendres possible (après la messe).",
            "rank": 2300,
        },
        dim_carem_1
        + timedelta(days=3): {
            "titre": "MERCREDI DES QUATRE-TEMPS DE CARÊME",
            "degre": "II",
            "couleur": "violet",
            "office": "du carême. Laudes II. Laudes/Vêpres : Prières fériales.",
            "messe": "Messe propre (Reminiscere) : Mém. pro Papa. 2 épîtres. Préf. du Carême.",
            "note": "",
            "rank": 1200,
        },  # 4temps de printemps
        dim_carem_1
        + timedelta(days=5): {
            "titre": "VENDREDI DES QUATRE-TEMPS DE CARÊME",
            "degre": "II",
            "couleur": "violet",
            "office": "du Carême. Laudes II. Laudes/Vêpres: Prières fériales.",
            "messe": "Messe propre (De necessitatibus) : Mém. pro Papa. Préf. du Carême.",
            "note": "Abstinence\nChemin de Croix",
            "rank": 1200,
        },
        dim_carem_1
        + timedelta(days=6): {
            "titre": "SAMEDI DES QUATRE-TEMPS DE CARÊME",
            "degre": "II",
            "couleur": "violet",
            "office": "du carême. Laudes II. Laudes : Prières fériales.",
            "messe": "Messe propre (Intret) : 5 Lectures. Mém. pro Papa. Préf. du Carême.",
            "note": "",
            "rank": 1200,
        },
        dim_carem_2: {
            "titre": "2E DIMANCHE DE CARÊME",
            "degre": "I",
            "couleur": "violet",
            "office": "dom. du Carême & propre. Laudes II. Ant. propres (sauf Vêpres). Prime : Ps. LIII.",
            "messe": "Messe propre (Reminiscere) : Mém. pro Papa. Credo. Préf. du Carême.",
            "note": None,
            "rank": 2300,
        },
        dim_carem_3: {
            "titre": "3E DIMANCHE DE CARÊME",
            "degre": "I",
            "couleur": "violet",
            "office": "dom. du Carême & propre. Laudes II. Ant. propres (sauf Vêpres). Prime : Ps. LIII.",
            "messe": "Messe propre (Oculi mei) : Mém. pro Papa. Credo. Préf. du Carême.",
            "note": None,
            "rank": 2300,
        },
        dimanche_laetare: {
            "titre": "4E DIMANCHE DE CARÊME, DIT DE “LÆTARE”",
            "degre": "I",
            "couleur": "rose ou violet",
            "office": "dom. de Carême & propre. Laudes II. Ant. propres (sauf Vêpres). Prime : Ps. LIII.",
            "messe": "Messe propre (Lætare, Jerusalem) : Mém. pro Papa. Credo. Préf. du Carême.",
            "note": "Orgues & fleurs permises (pas de reliques néanmoins).\nBénédiction de la Rose d’or par le Pape.",
            "rank": 2300,
        },
        dim_carem_5: {
            "titre": "DIMANCHE DE LA PASSION",
            "degre": "I",
            "couleur": "violet",
            "office": "dom. de la Passion & propre. Laudes II. Ant. propres (sauf Vêpres). Prime : Ps. LIII.",
            "messe": "Messe propre (Judica me) : Mém. pro Papa. Credo. Préf. de la Ste Croix.",
            "note": "Messe des Funérailles interdite.",
            "rank": 2300,
        },
        dimanche_des_rameaux: {
            "titre": "DIMANCHE DES RAMEAUX",
            "degre": "I",
            "couleur": "violet",
            "office": "dom. de la Passion & propre. Laudes II. Ant. propres (sauf Vêpres). Prime : Ps. LIII.",
            "messe": "Bénédiction des Rameaux, Procession & Messe (Violet) propre (Domine, ne longe) : Credo. Préf. de la Ste Croix.",
            "note": "Aux autres Messes, dernier évangile de la Bénédiction des Rameaux (Cum appropinquasset).",
            "rank": 2300,
        },
        jeudi_saint: {
            "titre": "JEUDI-SAINT – SAINTE-CÈNE DE NOTRE-SEIGNEUR JÉSUS-CHRIST",
            "degre": "I",
            "couleur": "Violet à l’Office, Blanc à la Messe",
            "office": "Propre",
            "messe": "Messe propre (Nos autem) : Gloria (cloches & sonneries). Credo. Préface de la Ste Croix.\nCommunicantes, Hanc igitur & Qui pridie propres. Pas de baiser de paix.\nPuis Procession au Reposoir, Vêpres & Dépouillement des autels (étoles violettes seulement).",
            "note": "Les Prêtres communient à cette Messe, une seule étant autorisée par Maison religieuse.\nLe Mandatum est ad libitum : il peut se célébrer avant ou après la messe, dans un lieu plutôt discret (chape violette).",
            "rank": 2700,
        },
        vendredi_saint: {
            "titre": "VENDREDI-SAINT – PASSION & MORT DE N.-S. JÉSUS-CHRIST",
            "degre": "I",
            "couleur": "Noir",
            "office": "propre",
            "messe": "Messe des Présanctifiés en chasuble noire pour toute la cérémonie, sauf pour le découvrement et l’Adoration de la Croix (en simple étole).",
            "note": "Jeûne & abstinence, Messe interdite.\nAprès l’Adoration de la Croix, dévoilement des Croix. Génuflexion à la Croix de l’Autel pour tous.",
            "rank": 2700,
        },
        samedi_saint: {
            "titre": "SAMEDI-SAINT",
            "degre": "I",
            "couleur": "",
            "office": "Propre",
            "messe": "Messe (Blanc) de la Vigile. Pas d’Introït ni d’antienne d’offertoire, ni d’Agnus Dei, ni de baiser de paix.\nGloria (cloches & sonneries, orgues, dévoilement des statues).\nPréface Pascale (in hac potissimum nocte).\nCommunicantes & Hanc igitur propres.\nAprès la communion, Alleluia et psaume 116. Antienne Vespere autem sabbati puis Magnificat.",
            "note": "Complies : propres.",
            "rank": 2700,
        },
        paques: {
            "titre": "SOLENNITÉ DE LA RÉSURRECTION DE N.-S. JÉSUS-CHRIST",
            "degre": "1re classe avec Octave de 1re classe",
            "couleur": "blanc",
            "office": "propre : Matines & Laudes de Pâques.",
            "messe": "Messe de la Résurrection (Resurrexi) : Gloria. Séquence. Credo. Préface Pascale (in hac potissimum die). Communicantes & Hanc igitur propres.",
            "note": "Vêpres & Complies de Pâques.\nÀ l’Aspersion : Vidi aquam.\nBénédiction de l’agneau pascal, des oeufs, du pain, etc.\nMesses des Défunts/Funérailles interdites.",
            "rank": 2800,
        },
        paques
        + timedelta(days=1): {
            "titre": "LUNDI DE PÂQUES",
            "degre": "I",
            "couleur": "blanc",
            "office": "de Pâques.",
            "messe": "Messe propre (Introduxit).",
            "note": None,
            "rank": 1990,
        },
        paques
        + timedelta(days=2): {
            "titre": "MARDI DE PÂQUES",
            "degre": "I",
            "couleur": "blanc",
            "office": "de Pâques.",
            "messe": "Messe propre (Aqua).",
            "note": None,
            "rank": 1990,
        },
        paques
        + timedelta(days=3): {
            "titre": "MERCREDI DE PÂQUES",
            "degre": "I",
            "couleur": "blanc",
            "office": "de Pâques.",
            "messe": "Messe propre (Venite).",
            "note": None,
            "rank": 1990,
        },
        paques
        + timedelta(days=4): {
            "titre": "JEUDI DE PÂQUES",
            "degre": "I",
            "couleur": "blanc",
            "office": "de Pâques.",
            "messe": "Messe propre (Victricem).",
            "note": None,
            "rank": 1990,
        },
        paques
        + timedelta(days=5): {
            "titre": "VENDREDI DE PÂQUES",
            "degre": "I",
            "couleur": "blanc",
            "office": "de Pâques.",
            "messe": "Messe propre (Eduxit eos).",
            "note": None,
            "rank": 1990,
        },
        paques
        + timedelta(days=6): {
            "titre": "SAMEDI DE PÂQUES « in Albis »",
            "degre": "I",
            "couleur": "blanc",
            "office": "de Pâques.",
            "messe": "Messe propre (Eduxit Dominus).",
            "note": "Les néophytes déposent leurs vêtements blancs.\n1res Vêpres du Dim. « in Albis » (1re cl. / Blanc) : Antienne unique et Psaumes fériaux. Complies : Ton Pascal.",
            "rank": 1990,
        },
        ascension: {
            "titre": "ASCENSION DE NOTRE-SEIGNEUR JÉSUS-CHRIST",
            "degre": "I",
            "couleur": "blanc",
            "office": "propre. Prime : Ps. LIII ; verset propre au Répons bref. Complies : du dimanche, Ton de l’Ascension (jusqu’à la Pentecôte exclue).",
            "messe": "Messe propre (Viri Galilæi) : Gloria. Credo. Préf. et Communicantes de l’Ascension.",
            "note": "Après l’évangile, on éteint le Cierge Pascal.\nMesses des Défunts/Funérailles interdites.",
            "rank": 2600,
        },
        # dimanche après pâque : 5
        pentecote
        - timedelta(days=1): {
            "titre": "VIGILE DE LA PENTECÔTE",
            "degre": "I",
            "couleur": "blanc & rouge",
            "office": "du Temps de l’Ascension. Oraison du Dim. après l’Ascension.\n1res Vêpres de la Pent. (1re cl. / Rouge). Complies : du dimanche, Ton de la Pentecôte (pendant toute l’octave).",
            "messe": "Messe (Cum sanctificatus) de la Vigile (Rouge). Gloria. Préf. du Saint-Esprit (Hodierna die). Communicantes & Hanc igitur propres.",
            "note": "",
            "rank": 2000,
        },
        pentecote: {
            "titre": "DIMANCHE DE LA PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "propre. Tierce : Hymne Veni Creator (jusqu’à samedi). Complies : Ton de la Pentecôte.",
            "messe": "Messe propre (Spiritus Domini) : Gloria. Séquence. Credo. Préf. du Saint-Esprit (Hodierna die). Communicantes & Hanc igitur propres.",
            "note": "Messes des Défunts/Funérailles interdites.",
            "rank": 2800,
        },
        pentecote
        + timedelta(days=1): {
            "titre": "LUNDI DE PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "de la Pentecôte.",
            "messe": "Messe propre (Cibavit eos).",
            "note": "",
            "rank": 1990,
        },
        pentecote
        + timedelta(days=2): {
            "titre": "MARDI DE PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "de la Pentecôte.",
            "messe": "Messe propre (Accipite).",
            "note": "",
            "rank": 1990,
        },
        pentecote
        + timedelta(days=3): {
            "titre": "QUATRE-TEMPS DE PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "de la Pentecôte.",
            "messe": "Messe propre (Deus). 2 épîtres.",
            "note": "",
            "rank": 1990,
        },
        pentecote
        + timedelta(days=4): {
            "titre": "JEUDI DE PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "de la Pentecôte.",
            "messe": "Messe (Spiritus Domini) de la Pentecôte : avec épître & évangile propres.",
            "note": "",
            "rank": 1990,
        },
        pentecote
        + timedelta(days=5): {
            "titre": "QUATRE-TEMPS DE PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "de la Pentecôte.",
            "messe": "Messe propre (Repleatur).",
            "note": "",
            "rank": 1990,
        },
        pentecote
        + timedelta(days=6): {
            "titre": "QUATRE-TEMPS DE PENTECÔTE",
            "degre": "I",
            "couleur": "rouge",
            "office": "de la Pentecôte.\n1res Vêpres de la T. Ste Trinité (1re cl. / Bl.). Complies : du dimanche, Ton solennel & Salve Regina.",
            "messe": "Messe propre (Caritas Dei).",
            "note": "Le Temps Pascal se termine après None.",
            "rank": 1990,
        },
        dimanches_pent["dim_pent_1"]: {
            "titre": "FÊTE DE LA TRÈS SAINTE TRINITÉ",
            "degre": "I",
            "couleur": "blanc",
            "office": "propre. Prime : Ps. LIII au lieu du CXVIIe et Symbole Quicumque (à la suite des Pss., avant la reprise de l’Antienne). Complies : Ton solennel.",
            "messe": "Messe propre (Benedicta sit). Gloria. Credo. Préf. de la T. Ste Trinité.",
            "note": "La Messe du 1er Dim. après la Pentecôte peut être célébrée au premier jour libre de la semaine.\nMesses des Défunts/Funérailles interdites.",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_2"]: {
            "titre": "2E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum. Matines : Invit. Dominum, qui fecit nos ; Hymne Nocte surgentes. Laudes : Hymne Ecce jam.",
            "messe": "Messe propre (Factus est) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "SOLENNITÉ DE LA FÊTE -DIEU (2e cl. / Blanc)\n Messe (& Vêpres, si en public) comme à la fête, sans mémoire du dimanche. Mém. pro Papa.",  # verifier!!!!!
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_3"]: {
            "titre": "3E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Respice in me) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "SOLENNITÉ DU SACRÉ -COEUR DE JÉSUS (2e cl. / Blanc)\n Messe (& Vêpres, si en public) comme à la fête, sans mémoire du dimanche. Mém. pro Papa.",  # verifier!!!!!
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_4"]: {
            "titre": "4E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Dominus illuminatio) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_5"]: {
            "titre": "5E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Exaudi) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_6"]: {
            "titre": "6E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Dominus) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_7"]: {
            "titre": "7E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Omnes gentes) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_8"]: {
            "titre": "8E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Suscepimus) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_9"]: {
            "titre": "9E DIMANCHE APRÈS LA PENTECÔTE",  # voir comment mettre en place les particulariter du mois d'Aout
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Ecce Deus) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_10"]: {
            "titre": "10E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Cum clamarem) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_11"]: {
            "titre": "11E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Deus in loco) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_12"]: {
            "titre": "12E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Deus in adjutorium) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_13"]: {
            "titre": "13E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Respice) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_14"]: {
            "titre": "14E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Protector) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_15"]: {
            "titre": "15E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Inclina) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_16"]: {
            "titre": "16E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Miserere) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_17"]: {
            "titre": "17E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Justus est) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_18"]: {
            "titre": "18E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Da pacem) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_19"]: {
            "titre": "19E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Salus populi) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_20"]: {
            "titre": "20E DIMANCHE APRÈS LA PENTECÔTE",  # 4em dimanche octobre pour les missions : pro Propaganda Fidei sous la même conclusion que les oraisons de la Messe.
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Omnia) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_21"]: {
            "titre": "21E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (In voluntate tua) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_22"]: {
            "titre": "22E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Si iniquitates) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        dimanches_pent["dim_pent_23"]: {
            "titre": "23E DIMANCHE APRÈS LA PENTECÔTE",
            "degre": "II",
            "couleur": "vert",
            "office": "per annum.",
            "messe": "Messe propre (Dicit Dominus) : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        },
        sacre_coeur: {
            "titre": "",
            "degre": "",
            "couleur": "",
            "office": "",
            "messe": "",
            "note": "",
            "rank": 2600,
        },
        mer_q_tps_sep: {  # quatre-temps de septembre
            "titre": "MERCREDI DES QUATRE-TEMPS DE SEPTEMBRE",
            "degre": "II",
            "couleur": "violet",
            "office": "",
            "messe": "",
            "note": "",
            "rank": 1200,
        },
        ven_q_tps_sep: {  # quatre-temps de septembre
            "titre": "VENDREDI DES QUATRE-TEMPS DE SEPTEMBRE",
            "degre": "II",
            "couleur": "violet",
            "office": "per annum. Matines : 1 Noct. (9 Pss., 3 Leçons de l’Homélie). Laudes II. \nLaudes/Vêpres : Prières fériales. Ant. Bened. & Magnif. propres.",
            "messe": "Messe propre (Lætetur cor) : Mém. pro Papa. Préf. commune.",
            "note": "Abstinence",
            "rank": 1200,
        },
        sam_q_tps_sep: {  # quatre-temps de septembre
            "titre": "SAMEDI DES QUATRE-TEMPS DE SEPTEMBRE",
            "degre": "II",
            "couleur": "violet",
            "office": "per annum. Matines : 1 Noct. (9 Pss., 3 Leçons de l’Homélie). Laudes II. \nLaudes : Prières fériales. Ant. Bened. propre.",
            "messe": "Messe propre (Venite) : Mém. pro Papa. Préf. commune.",
            "note": "",
            "rank": 1200,
        },
    }
    # avec led dimanche après la pentecote lier les dimanche après épiphanie variation de 1 à 6 donc 5 variables.
    if nb_dim_pent == 24:
        year_litugique.update(
            {
                dimanches_pent["dim_pent_24"]: {
                    "titre": "24E & DERNIER DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Dicit Dominus) du dernier Dimanche après la Pentecôte : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": None,
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
            }
        )
    elif nb_dim_pent == 25:
        year_litugique.update(
            {
                
                dimanches_pent["dim_pent_24"]: {
                    "titre": "24E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 24e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 6e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_25"]: {
                    "titre": "25E & DERNIER DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "",
                    "messe": "Messe propre (Dicit Dominus) du dernier Dimanche après la Pentecôte : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": None,
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
            }
        )
    elif nb_dim_pent == 26:
        year_litugique.update(
            {
                dimanches_pent["dim_pent_24"]: {
                    "titre": "24E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 24e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 5e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_25"]: {
                    "titre": "25E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 25e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 6e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_26"]: {
                    "titre": "26E & DERNIER DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "",
                    "messe": "Messe propre (Dicit Dominus) du dernier Dimanche après la Pentecôte : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": None,
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
            }
        )
    elif nb_dim_pent == 27:
        year_litugique.update(
            {
               
                dimanches_pent["dim_pent_24"]: {
                    "titre": "24E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 25e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 4e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_25"]: {
                    "titre": "25E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 25e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 5e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_26"]: {
                    "titre": "26E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 26e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 6e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_27"]: {
                    "titre": "27E & DERNIER DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Dicit Dominus) du dernier Dimanche après la Pentecôte : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": None,
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
            }
        )
    elif nb_dim_pent == 28:
        year_litugique.update({
            
                dimanches_pent["dim_pent_24"]: {
                    "titre": "24E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 24e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 3e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_25"]: {
                    "titre": "25E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 25e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 4e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_26"]: {
                    "titre": "26E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 26e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 5e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_27"]: {
                    "titre": "27E DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe du 27e Dim. après la Pentecôte (Dicit Dominus) : Gloria. Oraisons, épître & évangile du 6e Dim. après l’Épiphanie. \nMém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_pent["dim_pent_28"]: {
                    "titre": "28E & DERNIER DIMANCHE APRÈS LA PENTECÔTE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Dicit Dominus) du dernier Dimanche après la Pentecôte : Gloria. Mém. pro Papa. Credo. Préf. de la T. Ste Trinité.",
                    "note": None,
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
            }
        )
    if nb_dim_epi == 3:
        year_litugique.update(
            {
                dimanches_epi["dim_epi_3"]: {
                    "titre": "3E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                }
            }
        )
    elif nb_dim_epi == 4:
        year_litugique.update({
            dimanches_epi["dim_epi_3"]: {
                    "titre": "3E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_epi["dim_epi_4"]: {
                    "titre": "4E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
        }
        )
    elif nb_dim_epi == 5:
         year_litugique.update(
            {
                dimanches_epi["dim_epi_3"]: {
                    "titre": "3E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_epi["dim_epi_4"]: {
                    "titre": "4E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_epi["dim_epi_5"]: {
                    "titre": "5E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
            }
        )
    elif nb_dim_epi == 6:
        year_litugique.update(
            {
                dimanches_epi["dim_epi_3"]: {
                    "titre": "3E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_epi["dim_epi_4"]: {
                    "titre": "4E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_epi["dim_epi_5"]: {
                    "titre": "5E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                },
                dimanches_epi["dim_epi_6"]: {
                    "titre": "6E DIMANCHE APRES L’ÉPIPHANIE",
                    "degre": "II",
                    "couleur": "vert",
                    "office": "per annum.",
                    "messe": "Messe propre (Adorate Deum) : Gloria. Mém. pro Papa. Credo. Préface de la T. Ste Trinité.",
                    "note": "",
                    "ferie": ["IV", 200],
                    "rank": 1500,
                }
            }
        )

    day_temporal = datetime(annee, mois_select, day_select)

    # férie particulière si dimanche est fête
    except_ferie = {
        dimanches_epi["dim_epi_1"]: {
            "titre": "1E DIMANCHE APRÈS L’ÉPIPHANIE",
            "degre": "II",
            "couleur": "blanc",
            "office": "Office du Temps de l’Épiphanie. Matines : Répons « avant le 13 janv. ». Oraison Vota",
            "messe": "Messe (In excelso).Gloria. Mém. pro Papa. Préf. de l’Épiphanie.",
            "note": "",
            "ferie": ["IV", 200],
            "rank": 1500,
        }
    }

    # Dimanche
    if day_temporal in year_litugique:
        titre = year_litugique[day_temporal]["titre"]
        degre = year_litugique[day_temporal]["degre"]
        couleur = year_litugique[day_temporal]["couleur"]
        office = year_litugique[day_temporal]["office"]
        messe = year_litugique[day_temporal]["messe"]
        note = year_litugique[day_temporal]["note"]
        rank = year_litugique[day_temporal]["rank"]
    # feries courrantes
    else:
        d = day_temporal.weekday() + 1
        dim_preced = day_temporal - timedelta(days=d)

        if dim_preced in except_ferie:
            year_litugique[dim_preced] = except_ferie[dim_preced]
        print(year_litugique[dim_preced]["titre"])
        titre = "Férie après le " + str(year_litugique[dim_preced]["titre"])
        print(titre)
        degre = year_litugique[dim_preced]["ferie"][0]
        couleur = year_litugique[dim_preced]["couleur"]
        office = "per annum"
        messe = year_litugique[dim_preced]["messe"]
        note = ""
        rank = year_litugique[dim_preced]["ferie"][1]

    # print(titre)
    # print(degre)
    # print(couleur)
    # print(office)
    # print(messe)
    # print(note)
    return titre, degre, couleur, office, messe, note, rank


# test :
# calcul_kalendar(annee,day_select,mois_select)
