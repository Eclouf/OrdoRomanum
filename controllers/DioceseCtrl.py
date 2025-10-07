# -*- encoding:utf-8 -*-
from datetime import datetime
from models.ModelManager import ModelManager
from .BaseFestivalCtrl import BaseFestivalCtrl


"""
    Diocesan calendar controller.
    Contains logic regarding actions performed by the user about the diocesan calendar
"""


class DioceseCtrl(BaseFestivalCtrl):
    def __init__(self, model: ModelManager):
        super().__init__(model)
        self.dao = model.get_diocese_dao()

    def get_diocese_fest(self, country: str, diocese: str, date_obj):
        """
        Récupère la fête d'un diocèse spécifique ou du pays si non trouvé
        
        Args:
            country: Code pays (ex: 'fr', 'it')
            diocese: Code diocèse (ex: 'paris', 'lyon')
            date_obj: Objet date ou datetime
            
        Returns:
            Dict avec les informations de la fête ou None si non trouvée
        """
        month = date_obj.month
        day = date_obj.day
        
        # 1. Essayer d'abord le diocèse spécifique
        if diocese:
            fest = self.dao.get_by_id(f"{country}/{diocese}", month, day)
            if fest:
                return self._format_fest(fest)
        
        # 2. Sinon, essayer le pays
        if country:
            fest = self.dao.get_by_id(country, month, day)
            if fest:
                return self._format_fest(fest)
        
        # 3. Si rien trouvé, retourner None
        return None
    
    def calendar_diocese(self, country: str, diocese: str, day: datetime):
        """
        Récupère la fête d'un diocèse pour un jour donné
        
        Args:
            country: Code pays (ex: 'fr', 'it')
            diocese: Code diocèse (ex: 'paris', 'lyon')
            day: Date pour laquelle récupérer la fête
            
        Returns:
            Dict avec les informations de la fête ou None si non trouvée
        """
        return self.get_diocese_fest(country, diocese, day)
    
    def _format_fest(self, fest):
        """Format a festival for output"""
        if not fest:
            return None
            
        try:
            # Get raw office ID before resolution
            raw_office_id = getattr(fest, 'office', None)
            raw_mass = getattr(fest, 'mass', None)
            
            # Initialize basic data
            fest_data = {
                'title': getattr(fest, 'title', ''),
                'category': self._get_category(fest),
                'color': self._get_color(fest),
                'office': self._get_office(fest),
                'degree': getattr(fest, 'degree', None),
                'rank': getattr(fest, 'rank', None),
                'occ': getattr(fest, 'occ', None),
                'con': getattr(fest, 'con', None),
                'martyrology': getattr(fest, 'martyrology', []),
                'mass': raw_mass
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
    
    # Les méthodes _get_category, _get_color et _get_office sont maintenant dans la classe de base