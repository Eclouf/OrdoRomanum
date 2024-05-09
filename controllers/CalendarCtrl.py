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
                chrismas - timedelta(days=8):'',  # 4 tps
                chrismas - timedelta(days=9):'',
                chrismas - timedelta(day=11):'',
                chrismas - timedelta(days=14):'', # 3
                chrismas - timedelta(days=21):'', # 2
                chrismas - timedelta(days=28):''  # 1
            }
        else:  # touver le dimanche avant chrismas
            sun_adv_4 = chrismas - timedelta(days=chrismas.weekday() + 1)
            cycle_chrismas = {
                sun_adv_4:'',
                sun_adv_4 - timedelta(days=1):'',
                sun_adv_4 - timedelta(days=2):'',
                sun_adv_4 - timedelta(days=4):'',
                sun_adv_4 - timedelta(days=7):'', 
                sun_adv_4 - timedelta(days=14):'',
                sun_adv_4 - timedelta(days=21):''
            }
        
        # Cycle of Epiphany
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
            sundays_epi[dimanche] = nb_sun_epi
            if dimanche + timedelta(days=7) == easter - timedelta(days=63):
                break
        
        cycle_epiphany = sundays_epi
        
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
            easter + timedelta(days=1):'', # Octave
            easter + timedelta(days=2):'',
            easter + timedelta(days=3):'',
            easter + timedelta(days=4):'',
            easter + timedelta(days=5):'',
            easter + timedelta(days=6):'',
            easter + timedelta(days=7):'', # Dim in albis
            easter + timedelta(days=14):'',
            easter + timedelta(days=21):'',
            easter + timedelta(days=28):'',
            easter + timedelta(days=35):'',
            easter + timedelta(days=39):'', # Ascension
            easter + timedelta(days=40):''
        }
        
        # Cycle of Pentecost
        pentecost = easter + timedelta(days=49)
        cycle_pentecote = {
            pentecost:'', # Pentcôte
            pentecost + timedelta(days=11):'', # Fête Dieu
            pentecost + timedelta(days=7):'', # 1
            pentecost + timedelta(days=14):'', # 2
            pentecost + timedelta(days=21):'', # 3
            pentecost + timedelta(days=28):'', # 4
            pentecost + timedelta(days=35):'', # 5
            pentecost + timedelta(days=42):'', # 6
            pentecost + timedelta(days=49):'', # 7
            pentecost + timedelta(days=56):'', # 8
            pentecost + timedelta(days=63):'', # 9
            pentecost + timedelta(days=70):'', # 10
            pentecost + timedelta(days=77):'', # 11
            pentecost + timedelta(days=84):'', # 12
            pentecost + timedelta(days=91):'', # 13
            pentecost + timedelta(days=98):'', # 14
            pentecost + timedelta(days=105):'', # 15
            pentecost + timedelta(days=112):'', # 16
            pentecost + timedelta(days=119):'', # 17
            pentecost + timedelta(days=126):'', # 18
            pentecost + timedelta(days=133):'', # 19
            pentecost + timedelta(days=140):'', # 20
            pentecost + timedelta(days=147):'', # 21
            pentecost + timedelta(days=154):'', # 22
            pentecost + timedelta(days=151):'', # 23
        }
        
        
        
        # Fonction pour calculer le nombre de dimanches entre deux dates
        def count_sundays(start_date, end_date):
            sundays = 0
            current_date = start_date
            while current_date <= end_date:
                if current_date.weekday() == 6: # 6 représente le dimanche
                    sundays += 1
                current_date += timedelta(days=1)
            return sundays
        
        # Calculer le nombre de dimanches entre la Pentecôte et le premier dimanche de l'Avent
        first_advent_sunday = datetime(year, 12, 1) + timedelta(days=(6 - datetime(year, 12, 1).weekday()))
        nb_sun_pent = count_sundays(pentecost, first_advent_sunday)
        
        
        
        if nb_sun_pent == 24:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'', # 24
            })

        elif nb_sun_pent == 25:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'', # 24
                pentecost + timedelta(days=165):'', # 25
            })

        elif nb_sun_pent == 26:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'', # 24
                pentecost + timedelta(days=165):'', # 25
                pentecost + timedelta(days=172):'', # 26
            })
            
        elif nb_sun_pent == 27:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'', # 24
                pentecost + timedelta(days=165):'', # 25
                pentecost + timedelta(days=172):'', # 26
                pentecost + timedelta(days=179):'', # 27
            })
            
        elif nb_sun_pent == 28:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'', # 24
                pentecost + timedelta(days=165):'', # 25
                pentecost + timedelta(days=172):'', # 26
                pentecost + timedelta(days=179):'', # 27
                pentecost + timedelta(days=186):'', # 28
            })
        
        return cycle_chrismas, cycle_epiphany, cycle_lent, cycle_easter, cycle_pentecote
        