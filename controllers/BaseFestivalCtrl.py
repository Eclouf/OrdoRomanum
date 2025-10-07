# -*- encoding:utf-8 -*-
from models.ModelManager import ModelManager

"""
    Base controller for festival-related controllers.
    Contains common functionality for SanctoralCtrl and DioceseCtrl.
"""

class BaseFestivalCtrl:
    """Base controller for festival-related controllers"""
    
    def __init__(self, model: ModelManager):
        """Initialize with model manager"""
        self.category_dao = model.get_category_dao()
        self.color_dao = model.get_colors_dao()
        self.office_dao = model.get_office_dao()
    
    def _get_category(self, fest):
        """Get category with error handling"""
        return self._safe_dao_get(self.category_dao.get_by_id, getattr(fest, 'category', None))
    
    def _get_color(self, fest):
        """Get color with error handling"""
        return self._safe_dao_get(self.color_dao.get_by_id, getattr(fest, 'color', None))
    
    def _get_office(self, fest):
        """Get office with error handling"""
        return self._safe_dao_get(self.office_dao.get_office, getattr(fest, 'office', None))
    
    def _get_office_field(self, fest, field, default=None):
        """Generic method to get office-related fields"""
        value = getattr(fest, field, None)
        if value is None:
            return default
            
        dao_method = getattr(self.office_dao, f'get_{field}', None)
        if not dao_method:
            return default
            
        return self._safe_dao_get(dao_method, value)
    
    def _merge_mass_defaults(self, fest_data, raw_office_id, raw_mass):
        """Merge mass defaults from common definitions"""
        if not hasattr(self.office_dao, 'get_common_inline_details') or not raw_office_id:
            return fest_data
            
        # Merge defaults from common
        inline = self.office_dao.get_common_inline_details(raw_office_id) or {}
        inline_mass = inline.get('mass') if isinstance(inline, dict) else None
        
        if inline_mass:
            if not fest_data.get('mass'):
                fest_data['mass'] = dict(inline_mass)
            else:
                fest_data['mass'] = self._merge_dicts(dict(inline_mass), fest_data['mass'])
        
        # Handle mass common references (e.g., '#messe: 8')
        mass_common_id = None
        if isinstance(raw_mass, dict):
            mass_common_id = raw_mass.get('common_id')
            
        if mass_common_id is not None:
            self._merge_mass_common_reference(fest_data, mass_common_id, inline_mass)
            
        return fest_data
    
    def _merge_mass_common_reference(self, fest_data, mass_common_id, base_inline_mass):
        """Merge mass data from common reference"""
        inline2 = self.office_dao.get_common_inline_details(mass_common_id) or {}
        inline_mass2 = inline2.get('mass') if isinstance(inline2, dict) else None
        
        if not inline_mass2:
            return
            
        if not fest_data.get('mass'):
            fest_data['mass'] = dict(inline_mass2)
        else:
            fest_data['mass'] = self._merge_dicts(dict(inline_mass2), fest_data['mass'])
        
        # Handle title replacement for numeric placeholders
        if isinstance(fest_data.get('mass'), dict):
            t = fest_data['mass'].get('title')
            if isinstance(t, str) and t.strip().isdigit() and base_inline_mass and base_inline_mass.get('title'):
                fest_data['mass']['title'] = base_inline_mass['title']
    
    @staticmethod
    def _merge_dicts(defaults, overrides):
        """Deep merge two dictionaries"""
        if not isinstance(defaults, dict) or not isinstance(overrides, dict):
            return overrides or defaults or {}
        
        result = dict(defaults)
        for k, v in overrides.items():
            if v is not None and v != '':  # Only override non-empty values
                if isinstance(v, dict) and k in defaults and isinstance(defaults[k], dict):
                    result[k] = BaseFestivalCtrl._merge_dicts(defaults[k], v)
                else:
                    result[k] = v
        return result
    
    @staticmethod
    def _safe_dao_get(dao_method, value):
        """Safely call DAO method with error handling"""
        try:
            return dao_method(value) if value is not None else None
        except Exception:
            return None
            
    def _format_mass(self, fest_data, fest, raw_office_id, raw_mass):
        """Format mass data with defaults and overrides"""
        # Handle mass defaults and common references
        self._merge_mass_defaults(fest_data, raw_office_id, raw_mass)
        
        # Ensure mass is properly formatted with all fields
        if fest.mass and isinstance(fest.mass, dict):
            if 'mass' not in fest_data or not isinstance(fest_data['mass'], dict):
                fest_data['mass'] = {}
            
            # Copy all mass fields from the original fest.mass to the output
            for key, value in fest.mass.items():
                if value is not None and value != '':
                    fest_data['mass'][key] = value
                    
        return fest_data
