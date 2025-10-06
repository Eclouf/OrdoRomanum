# -*- encoding:utf-8 -*-
from datetime import datetime
from models.ModelManager import ModelManager
from .BaseFestivalCtrl import BaseFestivalCtrl


"""
    Temporal controller.
    Contains logic regarding actions performed by the user about temporal
"""


class SanctoralCtrl(BaseFestivalCtrl):
    def __init__(self, model: ModelManager):
        super().__init__(model)
        self.dao = model.get_sanctoral_dao()

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
            return self._format_fest(fest)
        return None
        
    def _format_fest(self, fest):
        """Format a festival for output"""
        if not fest:
            return None
            
        try:
            raw_office_id = getattr(fest, 'office', None)
            raw_mass = getattr(fest, 'mass', None)
            
            # Initialize basic data
            fest_data = {
                'title': getattr(fest, 'title', ''),
                'category': self._get_category(fest),
                'color': self._get_color(fest),
                'office': self._get_office(fest),
                'com': getattr(fest, 'com', ''),
                'note': getattr(fest, 'note', ''),
                'degree': getattr(fest, 'degree', None),
                'rank': getattr(fest, 'rank', None),
                'occ': getattr(fest, 'occ', None),
                'con': getattr(fest, 'con', None),
                'martyrology': fest.martyrology,
            }
            
            # Add office fields
            office_fields = [
                'matins', 'lauds', 'prime', 'little_hours', 
                'vespers', 'compline'
            ]
            
            for field in office_fields:
                fest_data[field] = self._get_office_field(fest, field)
            
            # Format mass data using the base class method
            self._format_mass(fest_data, fest, raw_office_id, raw_mass)
            
            return fest_data
            
        except Exception as e:
            print(f"Error formatting festival: {e}")
            return None