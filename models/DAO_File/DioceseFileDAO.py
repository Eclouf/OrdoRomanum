# -*- encoding:utf-8 -*-
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from .AbstractFileDAO import AbstractFileDAO
from models.utils.file_parsers import parse_kv_document


@dataclass
class DioceseFiche:
    title: str = ''
    category: Optional[int] = None
    color: Optional[int] = None
    office: Optional[int] = None
    matins: Optional[int] = None
    lauds: Optional[int] = None
    prime: Optional[int] = None
    little_hours: Optional[int] = None
    vespers: Optional[int] = None
    compline: Optional[int] = None
    mass: Optional[Dict[str, Any]] = None
    com: str = ''
    note: str = ''
    degree: Optional[int] = None
    rank: Optional[int] = None
    occ: Optional[str] = None
    con: Optional[str] = None
    martyrology: Optional[List[str]] = None


class DioceseFileDAO(AbstractFileDAO):
    def __init__(self, model_manager) -> None:
        super().__init__(model_manager)
        self.locale_root = os.path.join(self.models_root, 'fr')  # Base pour les pays
        self.cache = {}  # Cache pour les fichiers déjà chargés

    def _find_file_for(self, path: str, month: int, day: int) -> Optional[str]:
        """
        Recherche un fichier dans la hiérarchie spécifiée
        
        Args:
            path: Chemin relatif (ex: 'it' ou 'it/diocese/florence')
            month: Mois (1-12)
            day: Jour (1-31)
            
        Returns:
            Chemin complet du fichier ou None si non trouvé
        """
        # Construire le chemin complet
        base_path = os.path.join(self.locale_root, path)
        mdir = os.path.join(base_path, f"{month:02d}")
        filename = f"{month:02d}-{day:02d}.txt"
        file_path = os.path.join(mdir, filename)
        
        return file_path if os.path.isfile(file_path) else None

    def get_by_id(self, path: str, month: int, day: int) -> Optional[DioceseFiche]:
        """
        Récupère une fête par son chemin et sa date
        
        Args:
            path: Chemin relatif (ex: 'it' ou 'it/diocese/florence')
            month: Mois (1-12)
            day: Jour (1-31)
            
        Returns:
            Objet DioceseFiche ou None si non trouvé
        """
        cache_key = f"{path}/{month:02d}-{day:02d}"
        if cache_key in self.cache:
            return self.cache[cache_key]
            
        file_path = self._find_file_for(path, month, day)
        if not file_path:
            return None
            
        fest = self._parse_file(file_path)
        self.cache[cache_key] = fest
        return fest

    def _parse_file(self, file_path: str) -> DioceseFiche:
        """Parse un fichier de fête diocésaine"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        data = parse_kv_document(content)
        fest = DioceseFiche()
        
        # Mapper les champs de base
        fest.title = data.get('title', '')
        fest.category = int(data.get('category', 0)) if data.get('category') else None
        fest.color = int(data.get('color', 0)) if data.get('color') else None
        fest.degree = int(data.get('degree', 0)) if data.get('degree') else None
        fest.rank = int(data.get('rank', 0)) if data.get('rank') else None
        fest.occ = data.get('occ')
        fest.con = data.get('con')
        
        # Gérer l'office et la messe
        if 'office' in data:
            office_data = data['office']
            if isinstance(office_data, dict):
                fest.office = office_data.get('common')
                fest.matins = office_data.get('matins')
                fest.lauds = office_data.get('lauds')
                fest.prime = office_data.get('prime')
                fest.little_hours = office_data.get('terce')
                fest.little_hours += '\n' + office_data.get('sext')
                fest.little_hours += '\n' + office_data.get('none')
                fest.vespers = office_data.get('vespers')
                fest.compline = office_data.get('compline')
            else:
                fest.office = office_data
                
        fest.mass = data.get('mass')
        fest.com = data.get('com', '')
        fest.note = data.get('note', '')
        
        # Martirologe
        if 'martyrology' in data:
            martyrology = data['martyrology']
            if isinstance(martyrology, str):
                fest.martyrology = [m.strip() for m in martyrology.split('\n') if m.strip()]
            elif isinstance(martyrology, list):
                fest.martyrology = martyrology
                
        return fest