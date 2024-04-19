# -*- encoding:utf-8 -*-
from datetime import datetime, timedelta

"""
    calculates the dates of the liturgical year
"""
class CalendarRom():
    def __init__(self):
        pass
    
    def liturgical_year(self, year):
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
            dim_avent_4 = chrismas - timedelta(days=7)
            dim_avent_3 = chrismas - timedelta(days=14)  # gaudete
            dim_avent_2 = chrismas - timedelta(days=21)
            dim_avent_1 = chrismas - timedelta(days=28)
        else:  # touver le dimanche avant chrismas
            dim_avent_4 = chrismas - timedelta(days=chrismas.weekday() + 1)
            dim_avent_3 = dim_avent_4 - timedelta(days=7)  # gaudete
            dim_avent_2 = dim_avent_4 - timedelta(days=14)
            dim_avent_1 = dim_avent_4 - timedelta(days=21)
        
        # Cycle of 