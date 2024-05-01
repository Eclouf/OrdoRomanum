# -*- encoding:utf-8 -*-
from datetime import datetime
from models.ModelManager import ModelManager


"""
    Temporal controller.
    Contains logic regarding actions performed by the user about temporal
"""


class SanctoralCtrl:
    def __init__(self, model: ModelManager):
        self.dao = model.get_sanctoral_dao()
        self.category_dao = model.get_category_dao()
        self.color_dao = model.get_colors_dao()
        self.office_dao = model.get_office_dao()

    def get_all_fest(self):
        pass

    def get_fest_name(self):
        # return the Feast as dict
        return "Fête de truc"

    def get_fest(self, day: datetime):
        month = day.month
        day = day.day
        fest = self.dao.get_by_id(month, day)
        if fest is not None:
            fest = {
                'title': fest.title,
                'category': self.category_dao.get_by_id(fest.category),
                'color': self.color_dao.get_by_id(fest.color),
                'office': self.office_dao.get_office(fest.office),
                'matins': self.office_dao.get_matins(fest.matins),
                'lauds': self.office_dao.get_lauds(fest.lauds),
                'prime': self.office_dao.get_prime(fest.prime),
                'little_hours': self.office_dao.get_little_hours(fest.little_hours),
                'vespers': self.office_dao.get_vespers(fest.vespers),
                'compline': self.office_dao.get_compline(fest.compline),
                'mass': fest.mass,
                'com': fest.com,
                'note': fest.note,
                'degree': fest.degree,
                'rank': fest.rank,
                'occ': fest.occ,
                'con': fest.con
            }
        else:
            fest = {}
        return fest
        