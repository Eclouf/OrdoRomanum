# -*- encoding:utf-8 -*-
import pandas as pd
from models.ModelManager import ModelManager


"""
    test for the table of occurence 
    determination of feast celebrated
"""

class OccurenceCtrl:
    def __init__(self, model: ModelManager):
        self.dao = model.get_exceptions_dao()
        self.__only__ = ['O2', 'O1', 'V1', 'f3C', 'f3A', 'f2', 'f1', 'D2', 'D1']
        self.__ordinate__ = ['F1U', 'F1P', 'F2U', 'F2P', 'F3U', 'F3P', 'V2', 'V3']
        self.__abcissa__ = ['O2', 'O1', 'F3P', 'F3U', 'F2P', 'F2U', 'F1P', 'F1U', 'V2', 'V1', 'f3C', 'f3A', 'f2', 'f1', 'D2', 'D1']
        self.__data__ = [
            [0, 7, 1, 1, 1, 1, 6, 8, 1, 7, 3, 3, 3, 7, 3, 7],
            [3, 7, 1, 1, 1, 1, 8, 7, 1, 7, 3, 3, 3, 7, 3, 7],
            [3, 2, 4, 4, 4, 0, 2, 2, 4, 2, 3, 3, 3, 2, 5, 2],
            [0, 2, 4, 4, 9, 5, 2, 2, 4, 2, 3, 3, 5, 2, 5, 2],
            [0, 2, 5, 0, 5, 5, 2, 2, 5, 2, 5, 3, 5, 2, 2, 2],
            [0, 2, 9, 4, 5, 5, 2, 2, 5, 2, 5, 3, 5, 2, 2, 2],
            [0, 0, 4, 4, 5, 5, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 5, 0, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0]
        ]

        # Creat table of occurence
        self._table_occurence_ = pd.DataFrame(self.__data__, index=self.__ordinate__, columns=self.__abcissa__)
          
    def search(self, fest1: dict, fest2: dict):
        
        # Determination of festivities on the x-axis and y-axis for self._table_occurence_
        if fest1['occ'] in self.__only__:
            first = fest2   # y-axis
            second = fest1  # x-axis
        elif fest2['occ'] in self.__only__:
            first = fest1
            second = fest2 
        else:
            first = fest1
            second = fest2
            
        # Search occurence : normalize codes and guard against unknowns
        x = (str(first.get('occ') or '')).strip()
        y = (str(second.get('occ') or '')).strip()
        if x not in self._table_occurence_.index:
            raise ValueError(f"Occurrence inconnue (ligne): {x}; attendues: {list(self._table_occurence_.index)}")
        if y not in self._table_occurence_.columns:
            raise ValueError(f"Occurrence inconnue (colonne): {y}; attendues: {list(self._table_occurence_.columns)}")
        occurence = self._table_occurence_.loc[x, y]

        # Safe access to exception texts (may be missing if DB not configured)
        def _exc(idx: int) -> str:
            try:
                row = self.dao.get_by_id(idx) if hasattr(self, 'dao') and self.dao else None
                return (getattr(row, 'exception', '') or '')
            except Exception:
                return ''

        if occurence == 1:
            result = first
        
        elif occurence == 2:
            result = second
            
        elif occurence == 3:
            result = first
            result['lauds'] = (result.get('lauds') or '') + _exc(1) + second['title'] # exception
            result['vespers'] = (result.get('vespers') or '') + _exc(0) + second['title'] # exception
            
        elif occurence == 4:
            result = first
            result['lauds'] = (result.get('lauds') or '') + _exc(1) + second['title'] # exception
            
        elif occurence == 5:
            result = second
            result['lauds'] = (result.get('lauds') or '') + _exc(1) + first['title'] # exception

        elif occurence == 6:
            result = first
            # translation of second
            
        elif occurence == 7:
            result = second
            # translation of first
            
        elif occurence == 8:
            # Use rank only for this occurrence; safe default
            get_rank = lambda f: (f.get('rank') or -1)
            result = max([first, second], key=get_rank)
            lower = min([first, second], key=get_rank)
            # translation of lower
            
        elif occurence == 9:
            # Use rank only for this occurrence; safe default
            get_rank = lambda f: (f.get('rank') or -1)
            result = max([first, second], key=get_rank)
            lower = min([first, second], key=get_rank)
            # translation of lower
            
        else:
            pass
        return result
    