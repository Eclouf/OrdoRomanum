# -*- encoding:utf-8 -*-
from controllers.ControllerManager import ControllerManager

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

    def office(self, day):
        # find the Feast for the given day.
          # follow this logic for all possible holidays on the given day.
        day_temp = self.temporal_ctrl.get_fest_name(day)
        day_sanct = self.sanctoral_ctrl.get_fest_name(day)
        # search the Feast who is celebrat.
        fest = self.occurence_ctrl.search(day_temp,day_sanct)
        # see if there are any first vespers.
        fest = self.contents_ctrl.search(day)
        # 
        return(fest)

    def mass(self):
        pass
