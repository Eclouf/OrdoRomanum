# -*- encoding:utf-8 -*-
from controllers.ControllerManager import ControllerManager
from functools import lru_cache
from datetime import datetime, timedelta

"""
    Ordination of the office and mass for the given day.
    rules:
    - Temporal has global priority over Sanctoral/Diocese/Congregation.
    The function is defensive against missing fields (rank/occ/con).
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

    def _extract_martirologe(self, day: datetime | None) -> str | None:
        """Extrait le contenu du martyrologe d'une fête si présent.
        
        Args:
            day: Date pour laquelle extraire le martyrologe
            
        Returns:
            str: Le texte du martyrologe ou None si non trouvé
        """
        if not day:
            return None
            
        # Récupérer la fête du sanctoral pour le jour donné
        fest = self.sanctoral_ctrl.get_fest(day)
        if not fest:
            return None
            
        # Vérifier si le martyrologe existe et n'est pas vide
        mart_list = fest.get('martyrology')
        if not mart_list or not isinstance(mart_list, list) or len(mart_list) == 0:
            return None
            
        # Retourner le premier élément du martyrologe
        return mart_list[0]

    @lru_cache(maxsize=128)
    def office(self, country:str, diocese: str, congregation: str, day: datetime, cont=None):
        """
        Orders liturgical offices for a given date according to priority rules.
        
        Args:
            country: Country code (e.g., 'FR')
            diocese: Diocese code
            congregation: Congregation code
            day: Date of the service
            cont: Recursion check (internal)
            
        Returns:
            Dict containing the information for the ordered service
        """

        def norm(f: dict | None) -> dict | None:
            if not f:
                return None
            # Defensive defaults
            f = dict(f)
            f.setdefault('occ', '')
            f.setdefault('con', '')
            # Normalize codes (strip whitespace)
            f['occ'] = (str(f.get('occ') or '')).strip()
            f['con'] = (str(f.get('con') or '')).strip()
            return f
        
        # Gather candidates
        day_dioc = norm(self.diocese_ctrl.calendar_diocese(country, diocese, day)) if self.diocese_ctrl else None
        day_cong = norm(self.congregation_ctrl.calendar_congregation(congregation, day)) if self.congregation_ctrl else None
        day_temp = norm(self.temporal_ctrl.get_fest(day)) if self.temporal_ctrl else None
        day_sanct = norm(self.sanctoral_ctrl.get_fest(day)) if self.sanctoral_ctrl else None
        
        # Helper to merge two candidates using occurrence matrix
        def merge_with(current: dict | None, other: dict | None) -> dict | None:
            if not other:
                return current
            if current is None:
                return other
            # Décider uniquement via la matrice d'occurrence
            try:
                return self.occurence_ctrl.search(current, other)
            except Exception:
                # En cas d'erreur, conserver le courant
                return current
        
        # Commencer avec un dictionnaire vide
        fest = None
        
        # Liste des candidats dans l'ordre de priorité
        candidates = [day_temp, day_sanct, day_dioc, day_cong]
        # Fusionner les candidats
        for candidate in candidates:
            if candidate:
                fest = merge_with(fest, candidate)
        
        # look for the contents
        def get_contents(current_fest: dict | None) -> dict | None:
                if not current_fest:
                    return None
                
                try:
                    # Créer une copie profonde du jour actuel
                    fest_copy = {k: v for k, v in current_fest.items()}
                    
                    # Obtenir le jour suivant avec cont=1 pour éviter la récursion infinie
                    next_day = day + timedelta(days=1)
                    day1 = self.office(country, diocese, congregation, next_day, cont=1)
                    
                    # Si on a un jour suivant, faire une copie avant de l'utiliser
                    if day1.get('con') in ['F1', 'D2', 'D1']:
                        day1_copy = {k: v for k, v in day1.items()}
                        result = self.contents_ctrl.search(fest_copy, day1_copy)
                    # Retourner une copie du résultat si disponible, sinon retourner la copie originale
                    if result and isinstance(result, dict):
                        return {k: v for k, v in result.items()}
                
                # Retourner la copie originale si aucune condition n'est remplie
                    return fest_copy
                
                except Exception as e:
                    print(f"Erreur dans get_contents: {e}")
                # En cas d'erreur, retourner une copie du festival actuel
                return {k: v for k, v in current_fest.items()} if current_fest else {}
        
        # Get contents
        if cont is None:
            fest = get_contents(fest)
        
        # Add martyrology if not in contents
        if cont is None:
            # Sauvegarder le martyrologe avant toute modification ultérieure
            martyrology = self._extract_martirologe(day)
            
            # S'assurer que fest est un dictionnaire valide
            if not isinstance(fest, dict):
                fest = {}
                
            # Ajouter le martyrologe s'il existe
            if martyrology:
                fest['martyrology'] = [martyrology]
            
        # S'assurer que le dictionnaire contient au moins une entrée
        if not fest:
            fest = {}
            
        # Debug: Afficher le contenu final
        # print(f"=== DEBUG - Fest final: {fest}")
        
        # Retourner une copie du dictionnaire pour éviter les effets de bord
        return {k: v for k, v in fest.items()} if fest else {}
    
    def get_office_for_period(self, start_date: datetime, end_date: datetime, **kwargs):
        """
        Récupère les offices pour une période donnée avec optimisation des performances.
        
        Args:
            start_date: Date de début
            end_date: Date de fin
            **kwargs: Autres paramètres (country, diocese, congregation)
            
        Returns:
            Dict[datetime, Dict]: Offices indexés par date
        """
        if end_date < start_date:
            raise ValueError("La date de fin doit être postérieure à la date de début")
            
        if (end_date - start_date).days > 365:
            raise ValueError("La période ne peut pas dépasser un an")
            
        result = {}
        current_date = start_date
        while current_date <= end_date:
            result[current_date] = self.office(day=current_date, **kwargs)
            current_date += timedelta(days=1)
            
        return result
    
    def mass(self):
        pass
