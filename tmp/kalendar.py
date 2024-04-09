# Ad Majorem Dei Gloriam

from datetime import datetime, timedelta


def calculer_paques(annee):
    a = annee % 19
    b = annee // 100
    c = annee % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mois = (h + l - 7 * m + 114) // 31
    jour = ((h + l - 7 * m + 114) % 31) + 1
    return datetime(annee, mois, jour)


def calculer_dates_liturgiques(annee):
    paques = calculer_paques(annee)
    mercredi_des_cendres = paques - timedelta(days=46)  # 46 jours avant Pâques
    dim_carem_1 = mercredi_des_cendres + timedelta(days=4)
    dim_carem_2 = mercredi_des_cendres + timedelta(days=11)
    dim_carem_3 = mercredi_des_cendres + timedelta(days=18)
    septuagesima = mercredi_des_cendres - timedelta(days=17)
    sexagesima = septuagesima + timedelta(days=7)
    quinquagesima = septuagesima + timedelta(days=14)
    dimanche_laetare = paques - timedelta(days=21)  # Le quatrième dimanche de Carême
    dim_carem_5 = dimanche_laetare + timedelta(days=7)
    dimanche_des_rameaux = paques - timedelta(days=7)  # Une semaine avant Pâques
    jeudi_saint = paques - timedelta(days=3)  # Trois jours avant Pâques
    vendredi_saint = paques - timedelta(days=2)  # Deux jours avant Pâques
    samedi_saint = paques - timedelta(days=1)  # La veille de Pâques
    ascension = paques + timedelta(days=39)  # 39 jours après Pâques
    pentecote = paques + timedelta(days=49)  # 49 jours après Pâques
    # print(septuagesima)

    # cycle de noël
    noel = datetime(annee, 12, 25)
    st_nom = datetime(annee, 1, 2)
    if noel.weekday() == 6:  # alors il y a 4 dimanche de l'avent
        dim_avent_4 = noel - timedelta(days=7)
        dim_avent_3 = noel - timedelta(days=14)  # gaudete
        dim_avent_2 = noel - timedelta(days=21)
        dim_avent_1 = noel - timedelta(days=28)
    else:  # touver le dimanche avant noel
        dim_avent_4 = noel - timedelta(days=noel.weekday() + 1)
        dim_avent_3 = dim_avent_4 - timedelta(days=7)  # gaudete
        dim_avent_2 = dim_avent_4 - timedelta(days=14)
        dim_avent_1 = dim_avent_4 - timedelta(days=21)
    # print( 'gaudete', dim_avent_3)

    

    # Calcule les 28 dimanches possibles après la Pentecôte
    dimanches_pent = {}
    nb_dim_pent = 0
    for i in range(1, 28):
        # Calcule la date du dimanche
        nb_dim_pent += 1
        dimanche = pentecote + timedelta(days=i * 7)
        # Stocke la date dans le dictionnaire
        dimanches_pent["dim_pent_" + str(i)] = dimanche
        if dimanche + timedelta(days=7) == dim_avent_1:
            break

    sacre_coeur = ""

    # Calcule les 6 dimanches possibles après l'Epiphanie
    
    epiphanie = datetime(annee, 1, 6)
    dimanches_epi = {}
    if epiphanie.weekday() == 6:
        st_famille = epiphanie + timedelta(days=7)
        dimanches_epi["dim_epi_1"] = st_famille
    else:
        st_famille = epiphanie + timedelta(days=(6 - epiphanie.weekday()))
        dimanches_epi["dim_epi_1"] = st_famille
    
    nb_dim_epi = 0
    dimanche = st_famille
    for i in range(2, 6):
        nb_dim_epi += 1
        dimanche = dimanche + timedelta(days=7)
        dimanches_epi["dim_epi_" + str(i)] = dimanche
        if dimanche + timedelta(days=7) == septuagesima:
            break
    
    # quatre temps de septembre
    saint_croix = datetime(annee,9,14)
    mer_q_tps_sep = saint_croix + timedelta(days=((3 - saint_croix.weekday() + 7) % 7)) 
    if mer_q_tps_sep == saint_croix:
        mer_q_tps_sep = mer_q_tps_sep + timedelta(days=7)
    ven_q_tps_sep = mer_q_tps_sep + timedelta(days=2)
    sam_q_tps_sep = mer_q_tps_sep + timedelta(days=3) 
    
    
    # nombre d'or liturgique
    aureum = (annee + 1) / 19
    # epacte
    # epacte =
    return (
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
        sam_q_tps_sep
    )


# calculer_dates_liturgiques(2023)
# calculer tous les dimanche après la pentecote et après l'epiphanie
