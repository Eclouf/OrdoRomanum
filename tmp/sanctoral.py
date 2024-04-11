# Ad Majorem Dei Gloriam


def get_saint(day_select, mois_select, langue):
    # global saint, cate, degre,couleur,ap,souv,veu,arc, souv_mart,mart,marts,epi_mart,conf_ponf,conf_ponf_doc, conf, doc,abb,vir,stf,stfs,com,rouge, blanc

    # def langue:
    if langue == "Fr":
        from langue_Fr import (
            ap,
            violet,
            souv,
            souv_mart,
            mart,
            marts,
            conf,
            conf_ponf,
            conf_ponf_doc,
            doc,
            epi_mart,
            doc,
            abb,
            arc,
            vir,
            vir_mart,
            stf,
            stfs,
            veu,
            rouge,
            blanc,
            com,
        )
        from langue_Fr import office_st, messe_st, jr_fev, jr_mar, jr_dec

    def commun():
        if messe == "":
            messe = messe_st[cate]
        if office == "":
            office = office_st[cate]
            pass

    def janvier():
        dict_jour = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: {
                "saint": "Saint Telesphore",
                "cate": conf,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            6: "",
            7: "",
            8: "",
            9: "",
            10: "",
            11: {
                "saint": "Saint Hygin",
                "cate": conf,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            12: "",
            13: "",
            14: {
                1: {
                    "saint": "Saint Hilaire",
                    "cate": conf_ponf_doc,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                },
                2: {
                    "saint": "Saint Felix de Nole",
                    "cate": mart,
                    "degre": com,
                    "couleur": rouge,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
            },
            15: {
                1: {
                    "saint": "Saint Paul premier ermite",
                    "cate": conf,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
                2: {
                    "saint": "Saint Maur",
                    "cate": abb,
                    "degre": com,
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
            },
            16: {
                "saint": "Saint Marcel Ier",
                "cate": souv_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            17: {
                "saint": "Saint Antoine",
                "cate": abb,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            18: {
                "saint": "Sainte Prisque",
                "cate": vir_mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            19: {
                "saint": "Les saints Marius, Marthe, Audifax, et Abachus",
                "cate": marts,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            20: {
                "saint": "Saints Fabien et Sebastien",
                "cate": marts,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            21: {
                "saint": "Sainte Agnès",
                "cate": vir_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            22: {
                "saint": "Saints Vincent et Anastase",
                "cate": marts,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            23: {
                1: {
                    "saint": "Saint Raymond de Pegnafort",
                    "cate": conf,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
                2: {
                    "saint": "Sainte Émérentienne,",
                    "cate": vir_mart,
                    "degre": com,
                    "couleur": rouge,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
            },
            24: {
                "saint": "Saint Timothée",
                "cate": epi_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            25: {
                "saint": "Conversion de Saint Paul",
                "cate": ap,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "station": "Mémoire de Saint Pierre",
                "rank": 0,
            },
            56: {
                "saint": "Saint Polycarpe",
                "cate": epi_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            27: {
                "saint": "Saint Jean Chrysostome",
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            28: {
                1: {
                    "saint": "Saint Pierre Nolasque",
                    "cate": conf,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
                2: {
                    "saint": "Sainte Agnès",
                    "cate": vir_mart,
                    "degre": com,
                    "couleur": rouge,
                    "office": "",
                    "messe": "",
                    "station": "Cette deuxième fête de Sainte Agnès est peut-être la survivance d'une ancienne octave",
                    "rank": 0,
                },
            },
            29: {
                "saint": "Saint François de Sales",
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            30: {
                "saint": "Sainte Martine",
                "cate": vir_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            31: {
                "saint": "Saint Jean Bosco",
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def fevrier():
        dict_jour = {
            1: {
                "saint": jr_fev[1],
                "cate": epi_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            2: {
                "saint": jr_fev[2],
                "cate": "",
                "degre": "II",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            3: {
                "saint": jr_fev[3],
                "cate": epi_mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            4: {
                "saint": jr_fev[4],
                "cate": conf_ponf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            5: {
                "saint": jr_fev[5],
                "cate": vir_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            6: {
                1: {
                    "saint": jr_fev[6][0],
                    "cate": conf_ponf,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
                2: {
                    "saint": jr_fev[6][1],
                    "cate": vir_mart,
                    "degre": com,
                    "couleur": rouge,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
            },
            7: {
                "saint": jr_fev[7],
                "cate": abb,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            8: {
                "saint": jr_fev[8],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            9: {
                1: {
                    "saint": jr_fev[9][0],
                    "cate": conf_ponf_doc,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
                2: {
                    "saint": jr_fev[9][1],
                    "cate": vir_mart,
                    "degre": com,
                    "couleur": rouge,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
            },
            10: {
                "saint": jr_fev[10],
                "cate": vir,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            11: {
                "saint": jr_fev[11],
                "cate": "",
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            12: {
                "saint": jr_fev[12],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            13: {},
            14: {
                "saint": jr_fev[14],
                "cate": mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            15: {
                "saint": jr_fev[15],
                "cate": marts,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            16: {},
            17: {},
            18: {
                "saint": jr_fev[18],
                "cate": epi_mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            19: {},
            20: {},
            # 21:{},
            22: {
                "saint": jr_fev[22],
                "cate": ap,
                "degre": "II",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            23: {
                "saint": jr_fev[23],
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            24: {
                "saint": jr_fev[24],
                "cate": ap,
                "degre": "II",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            25: {},
            26: {},
            27: {
                "saint": jr_fev[27],
                "cate": "",
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            28: {},
            29: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def mars():
        dict_jour = {
            4: {
                1: {
                    "saint": jr_mar[4][0],
                    "cate": conf,
                    "degre": "III",
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
                2: {
                    "saint": jr_mar[4][1],
                    "cate": mart,
                    "degre": com,
                    "couleur": blanc,
                    "office": "",
                    "messe": "",
                    "rank": 0,
                },
            },
            6: {
                "saint": jr_mar[day_select],
                "cate": marts,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            7: {
                "saint": jr_mar[day_select],
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            8: {
                "saint": jr_mar[day_select],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            9: {
                "saint": jr_mar[day_select],
                "cate": veu,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            10: {
                "saint": jr_mar[day_select],
                "cate": marts,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            12: {
                "saint": jr_mar[day_select],
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            17: {
                "saint": jr_mar[day_select],
                "cate": conf_ponf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            18: {
                "saint": jr_mar[day_select],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            19: {
                "saint": jr_mar[day_select],
                "cate": conf,
                "degre": "I",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            21: {
                "saint": jr_mar[day_select],
                "cate": abb,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            24: {
                "saint": jr_mar[day_select],
                "cate": arc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            25: {
                "saint": jr_mar[day_select],
                "cate": vir,
                "degre": "I",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            27: {
                "saint": jr_mar[day_select],
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            28: {
                "saint": jr_mar[day_select],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            31: {
                "saint": jr_mar[day_select],
                "cate": vir,
                "degre": com,
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def avril():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {
                "saint": "Saint Anselme",
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def mai():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {},
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def juin():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {},
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def juillet():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {},
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def aout():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {},
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def septembre():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {
                "saint": "S. MATTHIEU, APÔTRE, ÉVANGÉLISTE",
                "cate": ap,
                "degre": "II",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            22: {},
            # 23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def octobre():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {},
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def novembre():
        dict_jour = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10: {},
            11: {},
            12: {},
            13: {},
            14: {},
            15: {},
            16: {},
            17: {},
            18: {},
            19: {},
            20: {},
            21: {},
            22: {},
            23: {},
            24: {},
            25: {},
            56: {},
            27: {},
            28: {},
            29: {},
            30: {},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def decembre():
        dict_jour = {
            2: {
                "saint": jr_dec[day_select],
                "cate": vir_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            3: {
                "saint": jr_dec[day_select],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            4: {"saint": jr_dec[day_select]},
            5: {
                "saint": jr_dec[day_select],
                "cate": abb,
                "degre": com,
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            6: {
                "saint": jr_dec[day_select],
                "cate": conf_ponf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            7: {
                "saint": jr_dec[day_select],
                "cate": conf_ponf_doc,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            8: {
                "saint": jr_dec[day_select],
                "cate": "",
                "degre": "I",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            10: {
                "saint": jr_dec[day_select],
                "cate": mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            11: {
                "saint": jr_dec[day_select],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            13: {
                "saint": jr_dec[day_select],
                "cate": vir_mart,
                "degre": "III",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            16: {
                "saint": jr_dec[day_select],
                "cate": epi_mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            21: {
                "saint": jr_dec[day_select],
                "cate": ap,
                "degre": "II",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            24: {
                "saint": jr_dec[day_select],
                "cate": "",
                "degre": "I",
                "couleur": violet,
                "office": "propre. Matines : Ant. & Pss. fériaux., Invitatoire Hodie scietis, 1 Nocturne.\nLaudes et Petites Heures : Pss. dominicaux (Laudes I). Prime : Ps. LIII.\n1res Vêpres de la Nativité de Notre-Seigneur (1re cl. / Blanc).\nComplies : du dim., Ton de Noël. Verset Post partum & Oraison Deus, qui salutis à l’Antienne mariale.",
                "messe": "Messe propre (Hodie scietis). Préf. commune.",
                "note": "Lorsqu’elles sont chantées, les Matines de Noël précèdent immédiatement la Messe de Minuit.\nTe Deum. Oraison Concede. Pas de Fidelium.",
                "rank": 2400,
            },
            25: {
                "saint": jr_dec[day_select],
                "cate": mart,
                "degre": com,
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            26: {
                "saint": jr_dec[day_select],
                "cate": mart,
                "degre": "II",
                "couleur": rouge,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            27: {
                "saint": jr_dec[day_select],
                "cate": conf,
                "degre": "III",
                "couleur": blanc,
                "office": "",
                "messe": "",
                "rank": 0,
            },
            28: {"saint": jr_dec[day_select]},
            29: {"saint": jr_dec[day_select]},
            30: {"saint": jr_dec[day_select]},
            31: {"saint": jr_dec[day_select]},
        }
        saint, cate, degre, couleur, come, office, messe, station, rank = final(
            dict_jour
        )
        return saint, cate, degre, couleur, come, office, messe, station, rank

    def final(dict_jour):

        if day_select in dict_jour:
            if isinstance(dict_jour[day_select], dict):
                if 1 in dict_jour[day_select]:
                    saint = dict_jour[day_select][1]["saint"]
                    cate = dict_jour[day_select][1]["cate"]
                    degre = dict_jour[day_select][1]["degre"]
                    couleur = dict_jour[day_select][1]["couleur"]
                    come = dict_jour[day_select][2]["saint"]
                    office = dict_jour[day_select][1]["office"]
                    messe = dict_jour[day_select][1]["messe"]
                    if "station" in dict_jour[day_select][1]:
                        station = dict_jour[day_select][1]["station"]
                    else:
                        station = ""
                    rank = dict_jour[day_select][1]["rank"]
                else:
                    saint = dict_jour[day_select]["saint"]
                    cate = dict_jour[day_select]["cate"]
                    degre = dict_jour[day_select]["degre"]
                    couleur = dict_jour[day_select]["couleur"]
                    office = dict_jour[day_select]["office"]
                    messe = dict_jour[day_select]["messe"]
                    come = ""
                    station = ""
                    if "station" in dict_jour[day_select]:
                        station = dict_jour[day_select]["station"]
                    rank = dict_jour[day_select]["rank"]
            else:
                saint = cate = degre = couleur = office = come = messe = station = (
                    rank
                ) = 0
        else:
            saint = cate = degre = couleur = office = come = messe = station = rank = 0
        return saint, cate, degre, couleur, come, office, messe, station, rank

    dict_mois = {
        1: janvier,
        2: fevrier,
        3: mars,
        4: avril,
        5: mai,
        6: juin,
        7: juillet,
        8: aout,
        9: septembre,
        10: octobre,
        11: novembre,
        12: decembre,
    }
    # print(mois_select, day_select)
    saint, cate, degre, couleur, come, office, messe, station, rank = dict_mois[
        mois_select
    ]()
    print(saint, cate, degre, couleur, come, office, messe, station, rank)
    return saint, cate, degre, couleur, come, office, messe, station, rank


# test
# get_saint(17,3,'Fr')
