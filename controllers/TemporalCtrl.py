# -*- encoding:utf-8 -*-
from models.ModelManager import ModelManager
from datetime import datetime

"""
    Temporal controller.
    Contains logic regarding actions performed by the user about temporal
"""


class TemporalCtrl:
    def __init__(self, model: ModelManager):
        self.dao = model.get_temporal_dao()
        self.category_dao = model.get_category_dao()
        self.color_dao = model.get_colors_dao()
        self.office_dao = model.get_office_dao()

    def get_all_fest(self):
        pass

    def get_fest_name(self):
        # return the Feast as dict
        return "Fête de truc"
    
    def get_fest(self, day: datetime):
        """
        Return a dict describing the temporal feast for a given date, with the
        same structure as SanctoralCtrl.get_fest(), so it can be compared/merged
        by OccurenceCtrl/ContentsCtrl/Ordinarium.
        """
        if self.dao is None:
            return None
        fiche = self.dao.get_by_date(day)
        if fiche is None:
            return None
        # helper to safely access attributes
        def ga(name, default=None):
            return getattr(fiche, name, default)

        raw_office_id = ga('office')
        fest = {
            'title': ga('title', ''),
            'category': self.category_dao.get_by_id(ga('category')),
            'color': self.color_dao.get_by_id(ga('color')),
            'office': self.office_dao.get_office(raw_office_id),
            'matins': self.office_dao.get_matins(ga('matins')),
            'lauds': self.office_dao.get_lauds(ga('lauds')),
            'prime': self.office_dao.get_prime(ga('prime')),
            'little_hours': self.office_dao.get_little_hours(ga('little_hours')),
            'vespers': self.office_dao.get_vespers(ga('vespers')),
            'compline': self.office_dao.get_compline(ga('compline')),
            'mass': ga('mass'),
            'com': ga('com', ''),
            'note': ga('note', ''),
            'degree': ga('degree'),
            'rank': ga('rank'),
            'occ': ga('occ'),
            'con': ga('con'),
        }
        return fest
