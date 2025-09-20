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
            raw_office_id = fest.office  # keep numeric/string id before resolution
            raw_mass = fest.mass
            fest = {
                'title': fest.title,
                'category': self.category_dao.get_by_id(fest.category),
                'color': self.color_dao.get_by_id(fest.color),
                'office': self.office_dao.get_office(raw_office_id),
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
                'con': fest.con,
                'martyrology': fest.martyrology,
            }
            # Merge inline defaults from Common.txt for the given 'common' id
            inline = self.office_dao.get_common_inline_details(raw_office_id) if hasattr(self.office_dao, 'get_common_inline_details') else {}
            inline_mass = inline.get('mass') if isinstance(inline, dict) else None
            if inline_mass:
                if not isinstance(fest.get('mass'), dict) or not fest['mass']:
                    fest['mass'] = dict(inline_mass)
                else:
                    for k, v in inline_mass.items():
                        fest['mass'].setdefault(k, v)

            # If mass references a specific common id (e.g., '#messe: 8'), merge its defaults too
            mass_common_id = None
            if isinstance(raw_mass, dict):
                mass_common_id = raw_mass.get('common_id')
            if mass_common_id is not None:
                inline2 = self.office_dao.get_common_inline_details(mass_common_id) if hasattr(self.office_dao, 'get_common_inline_details') else {}
                inline_mass2 = inline2.get('mass') if isinstance(inline2, dict) else None
                if inline_mass2:
                    if not isinstance(fest.get('mass'), dict) or not fest['mass']:
                        fest['mass'] = dict(inline_mass2)
                    else:
                        for k, v in inline_mass2.items():
                            fest['mass'].setdefault(k, v)
                        # If title remains a numeric placeholder, replace it with the inline title
                        t = fest['mass'].get('title')
                        if isinstance(t, str) and t.strip().isdigit() and inline_mass2.get('title'):
                            fest['mass']['title'] = inline_mass2['title']
        else:
            fest = {}
        return fest
        