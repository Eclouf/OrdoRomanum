# -*- encoding:utf-8 -*-
from datetime import datetime, timedelta
from typing import Dict


class CalendarRom:
    def __init__(self):
        pass

    def liturgical_year(self, year: int):
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        easter = datetime(year, month, day)
        chrismas = datetime(year, 12, 25)

        if chrismas.weekday() == 6:
            cycle_chrismas = {
                chrismas - timedelta(days=7): 'sun_advent_4',
                chrismas - timedelta(days=8): 'sun_advent_3',
                chrismas - timedelta(days=9): 'sun_advent_2',
                chrismas - timedelta(days=11): 'sun_advent_1',
                chrismas - timedelta(days=14): 'sun_advent_3',
                chrismas - timedelta(days=21): 'sun_advent_2',
                chrismas - timedelta(days=28): 'sun_advent_1',
            }
        else:
            sun_adv_4 = chrismas - timedelta(days=chrismas.weekday() + 1)
            cycle_chrismas = {
                sun_adv_4: 'sun_advent_4',
                sun_adv_4 - timedelta(days=1): 'sun_advent_3',
                sun_adv_4 - timedelta(days=2): 'sun_advent_2',
                sun_adv_4 - timedelta(days=4): 'sun_advent_1',
                sun_adv_4 - timedelta(days=7): 'sun_advent_3',
                sun_adv_4 - timedelta(days=14): 'sun_advent_2',
                sun_adv_4 - timedelta(days=21): 'sun_advent_1',
            }

        epiphany = datetime(year, 1, 6)
        sundays_epi = {}
        if epiphany.weekday() == 6:
            holy_family = epiphany + timedelta(days=7)
            sundays_epi[holy_family] = 1
        else:
            holy_family = epiphany + timedelta(days=(6 - epiphany.weekday()))
            sundays_epi[holy_family] = 1

        nb_sun_epi = 1
        dimanche = holy_family
        for i in range(2, 6):
            nb_sun_epi += 1
            dimanche = dimanche + timedelta(days=7)
            sundays_epi[dimanche] = f'sun_epi_{nb_sun_epi}'
            if dimanche + timedelta(days=7) == easter - timedelta(days=63):
                break

        cycle_epiphany = sundays_epi

        cycle_lent = {
            easter - timedelta(days=63): 'septuagesima',
            easter - timedelta(days=56): 'sexagesima',
            easter - timedelta(days=49): 'quinquagesima',
            easter - timedelta(days=46): 'ash_wednesday',
            easter - timedelta(days=45): 'lent_d45',
            easter - timedelta(days=44): 'lent_d44',
            easter - timedelta(days=43): 'lent_d43',
            easter - timedelta(days=42): 'sun_lent_1',
            easter - timedelta(days=41): 'lent_d41',
            easter - timedelta(days=40): 'lent_d40',
            easter - timedelta(days=39): 'lent_d39',
            easter - timedelta(days=38): 'lent_d38',
            easter - timedelta(days=37): 'lent_d37',
            easter - timedelta(days=36): 'lent_d36',
            easter - timedelta(days=35): 'sun_lent_2',
            easter - timedelta(days=34): 'lent_d34',
            easter - timedelta(days=33): 'lent_d33',
            easter - timedelta(days=32): 'lent_d32',
            easter - timedelta(days=31): 'lent_d31',
            easter - timedelta(days=30): 'lent_d30',
            easter - timedelta(days=29): 'lent_d29',
            easter - timedelta(days=28): 'sun_lent_3',
            easter - timedelta(days=27): 'lent_d27',
            easter - timedelta(days=26): 'lent_d26',
            easter - timedelta(days=25): 'lent_d25',
            easter - timedelta(days=24): 'lent_d24',
            easter - timedelta(days=23): 'lent_d23',
            easter - timedelta(days=22): 'lent_d22',
            easter - timedelta(days=21): 'sun_lent_4',
            easter - timedelta(days=20): 'lent_d20',
            easter - timedelta(days=19): 'lent_d19',
            easter - timedelta(days=18): 'lent_d18',
            easter - timedelta(days=17): 'lent_d17',
            easter - timedelta(days=16): 'lent_d16',
            easter - timedelta(days=15): 'lent_d15',
            easter - timedelta(days=14): 'sun_lent_5',
            easter - timedelta(days=13): 'lent_d13',
            easter - timedelta(days=12): 'lent_d12',
            easter - timedelta(days=11): 'lent_d11',
            easter - timedelta(days=10): 'lent_d10',
            easter - timedelta(days=9): 'lent_d9',
            easter - timedelta(days=8): 'lent_d8',
            easter - timedelta(days=7): 'sun_lent_6',
            easter - timedelta(days=6): 'lent_d6',
            easter - timedelta(days=5): 'lent_d5',
            easter - timedelta(days=4): 'lent_d4',
            easter - timedelta(days=3): 'lent_d3',
            easter - timedelta(days=2): 'lent_d2',
            easter - timedelta(days=1): 'lent_d1',
        }

        cycle_easter = {
            easter: 'easter_sunday',
            easter + timedelta(days=1): 'mon_easter',
            easter + timedelta(days=2): 'tue_easter',
            easter + timedelta(days=3): 'wed_easter',
            easter + timedelta(days=4): 'thur_easter',
            easter + timedelta(days=5): 'fri_easter',
            easter + timedelta(days=6): 'sat_easter',
            easter + timedelta(days=7): 'sun_easter',
            easter + timedelta(days=14): 'sun_easter_2',
            easter + timedelta(days=21): 'sun_easter_3',
            easter + timedelta(days=28): 'sun_easter_4',
            easter + timedelta(days=35): 'sun_easter_5',
            easter + timedelta(days=36): 'mon_rogations',
            easter + timedelta(days=37): 'tue_rogations',
            easter + timedelta(days=38): 'wed_rogations',
            easter + timedelta(days=39): 'thur_ascension',
            easter + timedelta(days=42): 'sun_easter_6',
        }

        pentecost = easter + timedelta(days=49)
        cycle_pentecote = {
            pentecost: 'pentecost',
            pentecost + timedelta(days=3): 'mon_pentecost',
            pentecost + timedelta(days=5): 'wed_pentecost',
            pentecost + timedelta(days=6): 'thur_pentecost',
            pentecost + timedelta(days=7): 'sun_pentecost_1',
            pentecost + timedelta(days=11): 'thur_corpus_christi',
            pentecost + timedelta(days=14): 'sun_pentecost_2',
            pentecost + timedelta(days=21): 'sun_pentecost_3',
            pentecost + timedelta(days=28): 'sun_pentecost_4',
            pentecost + timedelta(days=35): 'sun_pentecost_5',
            pentecost + timedelta(days=42): 'sun_pentecost_6',
            pentecost + timedelta(days=49): 'sun_pentecost_7',
            pentecost + timedelta(days=56): 'sun_pentecost_8',
            pentecost + timedelta(days=63): 'sun_pentecost_9',
            pentecost + timedelta(days=70): 'sun_pentecost_10',
            pentecost + timedelta(days=77): 'sun_pentecost_11',
            pentecost + timedelta(days=84): 'sun_pentecost_12',
            pentecost + timedelta(days=91): 'sun_pentecost_13',
            pentecost + timedelta(days=98): 'sun_pentecost_14',
            pentecost + timedelta(days=105): 'sun_pentecost_15',
            pentecost + timedelta(days=112): 'sun_pentecost_16',
            pentecost + timedelta(days=119): 'sun_pentecost_17',
            pentecost + timedelta(days=126): 'sun_pentecost_18',
            pentecost + timedelta(days=133): 'sun_pentecost_19',
            pentecost + timedelta(days=140): 'sun_pentecost_20',
            pentecost + timedelta(days=147): 'sun_pentecost_21',
            pentecost + timedelta(days=154): 'sun_pentecost_22',
            pentecost + timedelta(days=161): 'sun_pentecost_23',
            pentecost + timedelta(days=168): 'sun_pentecost_24',
            pentecost + timedelta(days=175): 'sun_pentecost_25',
            pentecost + timedelta(days=182): 'sun_pentecost_26',
            pentecost + timedelta(days=189): 'sun_pentecost_27',
            pentecost + timedelta(days=196): 'sun_pentecost_28',
        }

        crux = datetime(year, 9, 14)
        start = crux
        if start.weekday() == 2:
            wen = start + timedelta(days=7)
            fri = wen + timedelta(days=2)
            sat = wen + timedelta(days=3)
        else:
            wen = start + timedelta(days=((start.weekday() + 1) % 7))
            fri = start + timedelta(days=((start.weekday() + 4) % 7))
            sat = start + timedelta(days=((start.weekday() + 5) % 7))

        cycle_pentecote.update({
            wen: 'wen_4tps_pentecost',
            fri: 'fri_4tps_pentecost',
            sat: 'sat_4tps_pentecost',
        })

        def count_sundays(start_date, end_date):
            sundays = 0
            current_date = start_date
            while current_date <= end_date:
                if current_date.weekday() == 6:
                    sundays += 1
                current_date += timedelta(days=1)
            return sundays

        first_advent_sunday = datetime(year, 12, 1) + timedelta(days=(6 - datetime(year, 12, 1).weekday()))
        nb_sun_pent = count_sundays(pentecost, first_advent_sunday)

        if nb_sun_pent == 24:
            cycle_pentecote.update({pentecost + timedelta(days=158): 'sun_pentecost_24'})
        elif nb_sun_pent == 25:
            cycle_pentecote.update({
                pentecost + timedelta(days=158): 'sun_pentecost_24',
                pentecost + timedelta(days=165): 'sun_pentecost_25',
            })
        elif nb_sun_pent == 26:
            cycle_pentecote.update({
                pentecost + timedelta(days=158): 'sun_pentecost_24',
                pentecost + timedelta(days=165): 'sun_pentecost_25',
                pentecost + timedelta(days=172): 'sun_pentecost_26',
            })
        elif nb_sun_pent == 27:
            cycle_pentecote.update({
                pentecost + timedelta(days=158): 'sun_pentecost_24',
                pentecost + timedelta(days=165): 'sun_pentecost_25',
                pentecost + timedelta(days=172): 'sun_pentecost_26',
                pentecost + timedelta(days=179): 'sun_pentecost_27',
            })
        elif nb_sun_pent == 28:
            cycle_pentecote.update({
                pentecost + timedelta(days=158): 'sun_pentecost_24',
                pentecost + timedelta(days=165): 'sun_pentecost_25',
                pentecost + timedelta(days=172): 'sun_pentecost_26',
                pentecost + timedelta(days=179): 'sun_pentecost_27',
                pentecost + timedelta(days=186): 'sun_pentecost_28',
            })

        return cycle_chrismas, cycle_epiphany, cycle_lent, cycle_easter, cycle_pentecote

    def date_to_id_map(self, year: int) -> Dict[str, str]:
        cy_chr, cy_epi, cy_lent, cy_easter, cy_pent = self.liturgical_year(year)
        merged: Dict[str, str] = {}
        for dct in (cy_chr, cy_epi, cy_lent, cy_easter, cy_pent):
            for dt, id_ in dct.items():
                merged[dt.strftime("%Y-%m-%d")] = id_
        return merged
