# -*- encoding:utf-8 -*-
from controllers.ControllerManager import ControllerManager
from datetime import datetime

"""
    Ordination of the office and mass for the given day.
"""


class Ordination:
    def __init__(self):
        cm = ControllerManager()
        self.occurence_ctrl = cm.get_occurrence_ctrl()
        self.contents_ctrl = cm.get_contents_ctrl()
        self.temporal_ctrl = cm.get_temporal_ctrl()
        self.sanctoral_ctrl = cm.get_sanctoral_ctrl()
        self.diocese_ctrl = cm.get_diocese_ctrl()
        self.congregation_ctrl = cm.get_congregation_ctrl()

    def office(self, country:str, diocese: str, congregation: str, day: datetime):
        # find the Feast for the given day.
          # follow this logic for all possible holidays on the given day.
        fest: dict =[]
        day_dioc = self.diocese_ctrl.calendar_diocese(country, diocese, day)
        day_cong = self.congregation_ctrl.calendar_congregation(congregation, day)
        day_temp = self.temporal_ctrl.get_fest(day)
        day_sanct = self.sanctoral_ctrl.get_fest(day)
        
        if day_dioc  and day_cong :
            if day_dioc['title'] == day_cong['title']:
                fest = max(day_dioc, day_cong, key=lambda x: x['rank'])
            else:
                fest = self.occurence_ctrl.search(day_dioc, day_cong)
        elif not day_dioc  and day_cong :
            fest = day_cong
        else:
            fest = day_dioc
            
        if day_sanct and fest :
            if day_sanct['title'] == fest['title']:
                fest = max(day_sanct, fest, key=lambda x: x['rank'])
            else:
                fest = self.occurence_ctrl.search(day_sanct, fest)
        elif day_sanct  and not fest:
            fest = day_sanct
        else:
            fest = fest
        
        if day_temp and fest:
            if day_temp['title'] == fest['title']:
                fest = max(day_temp, fest, key=lambda x: x['rank'])
            else:
                fest = self.occurence_ctrl.search(day_temp, fest)
        elif day_temp and not fest:
            fest = day_temp
        else:
            fest=fest
       
        return(fest)

    def mass(self):
        pass
