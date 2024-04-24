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
            cycle_chrismas = {
                chrismas - timedelta(days=7):'',  # 4 '' -> id of temporal
                chrismas - timedelta(days=14):'', # 3
                chrismas - timedelta(days=21):'', # 2
                chrismas - timedelta(days=28):''  # 1
            }
        else:  # touver le dimanche avant chrismas
            sun_adv_4 = chrismas - timedelta(days=chrismas.weekday() + 1)
            cycle_chrismas = {
                sun_adv_4:'',
                sun_adv_4 - timedelta(days=7):'', 
                sun_adv_4 - timedelta(days=14):'',
                sun_adv_4 - timedelta(days=21):''
            }
        
       
        
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
            if dimanche + timedelta(days=7) == easter - timedelta(days=63):
                break
        
        cycle_epiphany = list(sundays_epi.items())
        
        # Cycle of Lent
        cycle_lent = {
            easter - timedelta(days=63):'', # septuagesima
            easter - timedelta(days=56):'', # sexagesima
            easter - timedelta(days=49):'', # quinquagesima
            easter - timedelta(days=46):'', # ash_wednesday
            easter - timedelta(days=45):'',
            easter - timedelta(days=44):'',
            easter - timedelta(days=43):'',
            easter - timedelta(days=42):'', # sun_lent_1
            easter - timedelta(days=41):'',
            easter - timedelta(days=40):'',
            easter - timedelta(days=39):'',
            easter - timedelta(days=38):'',
            easter - timedelta(days=37):'',
            easter - timedelta(days=36):'',
            easter - timedelta(days=35):'', # sun_lent_2
            easter - timedelta(days=34):'',
            easter - timedelta(days=33):'',
            easter - timedelta(days=32):'',
            easter - timedelta(days=31):'',
            easter - timedelta(days=30):'',
            easter - timedelta(days=29):'',
            easter - timedelta(days=28):'', # sun_lent_3
            easter - timedelta(days=27):'',
            easter - timedelta(days=26):'',
            easter - timedelta(days=25):'',
            easter - timedelta(days=24):'',
            easter - timedelta(days=23):'',
            easter - timedelta(days=22):'',
            easter - timedelta(days=21):'', # sun_lent_4
            easter - timedelta(days=20):'',
            easter - timedelta(days=19):'',
            easter - timedelta(days=18):'',
            easter - timedelta(days=17):'',
            easter - timedelta(days=16):'',
            easter - timedelta(days=15):'',
            easter - timedelta(days=14):'', # sun_lent_5
            easter - timedelta(days=13):'',
            easter - timedelta(days=12):'',
            easter - timedelta(days=11):'',
            easter - timedelta(days=10):'',
            easter - timedelta(days=9):'',
            easter - timedelta(days=8):'',
            easter - timedelta(days=7):'', # sun_lent_6
            easter - timedelta(days=6):'',
            easter - timedelta(days=5):'',
            easter - timedelta(days=4):'',
            easter - timedelta(days=3):'',
            easter - timedelta(days=2):'',
            easter - timedelta(days=1):'',
        }
        
        # Cycle of Easter
        cycle_easter = {
            easter:'',
            easter + timedelta(days=1):'',
            easter + timedelta(days=2):'',
            easter + timedelta(days=3):'',
            easter + timedelta(days=4):'',
            easter + timedelta(days=5):'',
            easter + timedelta(days=6):'',
            easter + timedelta(days=7):'',
            easter + timedelta(days=14):'',
            easter + timedelta(days=21):'',
            easter + timedelta(days=28):'',
            easter + timedelta(days=35):'',
            easter + timedelta(days=40):''
        }
        
        # Cycle of Pentecost
        return cycle_chrismas, cycle_epiphany, cycle_lent, cycle_easter
        