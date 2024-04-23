# -*- encoding:utf-8 -*-
from datetime import datetime, timedelta

"""
    calculates the dates of the liturgical year
    calculates the moving holidays of the universal calendar
"""
class CalendarRom():
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
    
        # Cycle of Chrismas
        if chrismas.weekday() == 6:  # alors il y a 4 dimanche de l'avent
            sun_adv_4 = chrismas - timedelta(days=7)
            sun_adv_3 = chrismas - timedelta(days=14)  # gaudete
            sun_adv_2 = chrismas - timedelta(days=21)
            sun_adv_1 = chrismas - timedelta(days=28)
        else:  # touver le dimanche avant chrismas
            sun_adv_4 = chrismas - timedelta(days=chrismas.weekday() + 1)
            sun_adv_3 = sun_adv_4 - timedelta(days=7)  # gaudete
            sun_adv_2 = sun_adv_4 - timedelta(days=14)
            sun_adv_1 = sun_adv_4 - timedelta(days=21)
        
        # Cycle of Epiphany
        epiphany = datetime(year, 1, 6)
        sundays_epi = {}
        if epiphany.weekday() == 6:
            holy_family = epiphany + timedelta(days=7)
            sundays_epi["sun_epi_1"] = holy_family
        else:
            holy_family = epiphany + timedelta(days=(6 - epiphany.weekday()))
            sundays_epi["sun_epi_1"] = holy_family
        
        nb_sun_epi = 0
        dimanche = holy_family
        for i in range(2, 6):
            nb_sun_epi += 1
            dimanche = dimanche + timedelta(days=7)
            sundays_epi["sun_epi_" + str(i)] = dimanche
            if dimanche + timedelta(days=7) == septuagesima:
                break
        
        # Cycle of Lent
        septuagesima = easter - timedelta(days=63)
        sexagesima = easter - timedelta(days=56)
        quinquagesima = easter - timedelta(days=49)
        ash_wednesday = easter - timedelta(days=46)
        sun_lent_1 = easter - timedelta(days=42)
        sun_lent_2 = easter - timedelta(days=35)
        sun_lent_3 = easter - timedelta(days=28)
        sun_lent_4 = easter - timedelta(days=21)  
        sun_passion_1 = easter - timedelta(days=14)
        sun_passion_2 = easter - timedelta(days=7)  
        jeudi_saint = easter - timedelta(days=3)  
        vendredi_saint = easter - timedelta(days=2) 
        samedi_saint = easter - timedelta(days=1)  
        
        # Cycle of Easter
        sun_easter_1 = easter + timedelta(days=7)
        sun_easter_2 = easter + timedelta(days=14)
        sun_easter_3 = easter + timedelta(days=21)
        sun_easter_4 = easter + timedelta(days=28)
        sun_easter_5 = easter + timedelta(days=35)
        ascension = easter + timedelta(days=40)
        
        # Cycle of Pentecost
        