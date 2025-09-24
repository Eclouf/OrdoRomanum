# -*- encoding:utf-8 -*-
from datetime import datetime, timedelta
from typing import Dict

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
                chrismas - timedelta(days=7):'sun_advent_4',
                chrismas - timedelta(days=8):'sun_advent_3',
                chrismas - timedelta(days=9):'sun_advent_2',
                chrismas - timedelta(days=11):'sun_advent_1',
                chrismas - timedelta(days=14):'sun_advent_3',
                chrismas - timedelta(days=21):'sun_advent_2',
                chrismas - timedelta(days=28):'sun_advent_1'
            }
        
        else:  # touver le dimanche avant chrismas
            sun_adv_4 = chrismas - timedelta(days=chrismas.weekday() + 1)
            cycle_chrismas = {
                sun_adv_4:'sun_advent_4',
                sun_adv_4 - timedelta(days=1):'sun_advent_3', # 4tps
                sun_adv_4 - timedelta(days=2):'sun_advent_2', # 4tps
                sun_adv_4 - timedelta(days=4):'sun_advent_1', # 4tps
                sun_adv_4 - timedelta(days=7):'sun_advent_3', 
                sun_adv_4 - timedelta(days=14):'sun_advent_2',
                sun_adv_4 - timedelta(days=21):'sun_advent_1'
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
            sundays_epi[dimanche] = f'sun_epi_{nb_sun_epi}'
            if dimanche + timedelta(days=7) == easter - timedelta(days=63):
                break
        
        cycle_epiphany = sundays_epi
        
        # Cycle of Lent — assign explicit IDs for Sundays and key days; generic for others
        cycle_lent = {
            easter - timedelta(days=63): 'septuagesima',
            easter - timedelta(days=56): 'sexagesima',
            easter - timedelta(days=49): 'quinquagesima',
            easter - timedelta(days=46): 'ash_wednesday',
        }
        
        # Calculate Lent weeks with proper day names
        # Lent starts on Ash Wednesday (46 days before Easter)
        ash_wednesday = easter - timedelta(days=46)
        
        # Add the three days after Ash Wednesday
        cycle_lent[ash_wednesday + timedelta(days=1)] = 'ash_thursday'  # Thursday after Ash Wednesday
        cycle_lent[ash_wednesday + timedelta(days=2)] = 'ash_friday'    # Friday after Ash Wednesday
        cycle_lent[ash_wednesday + timedelta(days=3)] = 'ash_saturday'  # Saturday after Ash Wednesday
        
        # Generate Lent calendar with proper naming
        # Lent has 6 weeks, starting from the Monday after Ash Wednesday
        lent_start = ash_wednesday + timedelta(days=4)  # Monday after Ash Wednesday
        
        for week in range(1, 7):  # 6 weeks of Lent
            week_start = lent_start + timedelta(days=(week-1)*7)
            
            # Monday to Saturday
            cycle_lent[week_start] = f'mon_lent_{week}'      # Monday
            cycle_lent[week_start + timedelta(days=1)] = f'tue_lent_{week}'  # Tuesday
            cycle_lent[week_start + timedelta(days=2)] = f'wed_lent_{week}'  # Wednesday
            cycle_lent[week_start + timedelta(days=3)] = f'thu_lent_{week}'  # Thursday
            cycle_lent[week_start + timedelta(days=4)] = f'fri_lent_{week}'  # Friday
            cycle_lent[week_start + timedelta(days=5)] = f'sat_lent_{week}'  # Saturday
            
            # Sunday
            sunday_date = week_start + timedelta(days=6)
            cycle_lent[sunday_date] = f'sun_lent_{week}'
        
        # Cycle of Easter
        cycle_easter = {
            easter:'easter_sunday',
            easter + timedelta(days=1):'mon_easter', # Octave
            easter + timedelta(days=2):'tue_easter',
            easter + timedelta(days=3):'wed_easter',
            easter + timedelta(days=4):'thur_easter',
            easter + timedelta(days=5):'fri_easter',
            easter + timedelta(days=6):'sat_easter',
            easter + timedelta(days=7):'sun_easter', # Dim in albis
            easter + timedelta(days=14):'sun_easter_2',
            easter + timedelta(days=21):'sun_easter_3',
            easter + timedelta(days=28):'sun_easter_4',
            easter + timedelta(days=35):'sun_easter_5',
            easter + timedelta(days=36):'mon_rogations', # Rogations x3
            easter + timedelta(days=37):'tue_rogations',
            easter + timedelta(days=38):'wed_rogations',
            easter + timedelta(days=39):'thur_ascension', # Ascension
            easter + timedelta(days=42):'sun_easter_6' # Sunday after Ascension
        }
        
        # Cycle of Pentecost
        pentecost = easter + timedelta(days=49)
        cycle_pentecote = {
            pentecost:'pentecost', # Pentcôte
            pentecost + timedelta(days=3):'mon_pentecost', # 4tps
            pentecost + timedelta(days=5):'wed_pentecost', # 4tps
            pentecost + timedelta(days=6):'thur_pentecost', # 4tps
            pentecost + timedelta(days=7):'sun_pentecost_1', # 1
            pentecost + timedelta(days=11):'thur_corpus_christi', # Fête Dieu
            pentecost + timedelta(days=14):'sun_pentecost_2', # 2
            pentecost + timedelta(days=21):'sun_pentecost_3', # 3
            pentecost + timedelta(days=28):'sun_pentecost_4', # 4
            pentecost + timedelta(days=35):'sun_pentecost_5', # 5
            pentecost + timedelta(days=42):'sun_pentecost_6', # 6
            pentecost + timedelta(days=49):'sun_pentecost_7', # 7
            pentecost + timedelta(days=56):'sun_pentecost_8', # 8
            pentecost + timedelta(days=63):'sun_pentecost_9', # 9
            pentecost + timedelta(days=70):'sun_pentecost_10', # 10
            pentecost + timedelta(days=77):'sun_pentecost_11', # 11
            pentecost + timedelta(days=84):'sun_pentecost_12', # 12
            pentecost + timedelta(days=91):'sun_pentecost_13', # 13
            pentecost + timedelta(days=98):'sun_pentecost_14', # 14
            pentecost + timedelta(days=105):'sun_pentecost_15', # 15
            pentecost + timedelta(days=112):'sun_pentecost_16', # 16
            pentecost + timedelta(days=119):'sun_pentecost_17', # 17
            pentecost + timedelta(days=126):'sun_pentecost_18', # 18
            pentecost + timedelta(days=133):'sun_pentecost_19', # 19
            pentecost + timedelta(days=140):'sun_pentecost_20', # 20
            pentecost + timedelta(days=147):'sun_pentecost_21', # 21
            pentecost + timedelta(days=154):'sun_pentecost_22', # 22
            pentecost + timedelta(days=161):'sun_pentecost_23', # 23
            pentecost + timedelta(days=168):'sun_pentecost_24', # 24
            pentecost + timedelta(days=175):'sun_pentecost_25', # 25
            pentecost + timedelta(days=182):'sun_pentecost_26', # 26
            pentecost + timedelta(days=189):'sun_pentecost_27', # 27
            pentecost + timedelta(days=196):'sun_pentecost_28', # 28
        }
        
        # 4tps of september
        crux = datetime(year, 9, 14)
        start = crux
        
        if start.weekday() == 2:  # 2 représente le mercredi
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
            sat: 'sat_4tps_pentecost'
        })
        
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
                pentecost + timedelta(days=158):'sun_pentecost_24', # 24
            })

        elif nb_sun_pent == 25:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'sun_pentecost_24', # 24
                pentecost + timedelta(days=165):'sun_pentecost_25', # 25
            })

        elif nb_sun_pent == 26:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'sun_pentecost_24', # 24
                pentecost + timedelta(days=165):'sun_pentecost_25', # 25
                pentecost + timedelta(days=172):'sun_pentecost_26', # 26
            })
            
        elif nb_sun_pent == 27:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'sun_pentecost_24', # 24
                pentecost + timedelta(days=165):'sun_pentecost_25', # 25
                pentecost + timedelta(days=172):'sun_pentecost_26', # 26
                pentecost + timedelta(days=179):'sun_pentecost_27', # 27
            })
            
        elif nb_sun_pent == 28:
            cycle_pentecote.update({
                pentecost + timedelta(days=158):'sun_pentecost_24', # 24
                pentecost + timedelta(days=165):'sun_pentecost_25', # 25
                pentecost + timedelta(days=172):'sun_pentecost_26', # 26
                pentecost + timedelta(days=179):'sun_pentecost_27', # 27
                pentecost + timedelta(days=186):'sun_pentecost_28', # 28
            })
        
        return cycle_chrismas, cycle_epiphany, cycle_lent, cycle_easter, cycle_pentecote

    def date_to_id_map(self, year: int) -> Dict[str, str]:
        """
        Returns a consolidated mapping for the given year:
          ISO date string (YYYY-MM-DD) -> id

        This provides the direct date -> id link, where the fiche filename is
        '<id>.txt'.
        """
        cy_chr, cy_epi, cy_lent, cy_easter, cy_pent = self.liturgical_year(year)
        merged: Dict[str, str] = {}
        for dct in (cy_chr, cy_epi, cy_lent, cy_easter, cy_pent):
            for dt, id_ in dct.items():
                merged[dt.strftime("%Y-%m-%d")] = id_
        return merged