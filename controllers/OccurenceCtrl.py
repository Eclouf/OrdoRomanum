# -*- encoding:utf-8 -*-
import pandas as pd


"""
    test for the table of occurence 
    determination of feast celebrated
"""

class OccurenceCtrl:
    def __init__(self):
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
            
        # Search occurence : 
        x = first['occ']
        y = second['occ']
        occurence = self._table_occurence_.loc[x,y]

        if occurence == 1:
            print(f"Occurence N°{occurence}")
            result = first
        
        elif occurence == 2:
            print(f"Occurence N°{occurence}")
            result = second
            
        elif occurence == 3:
            print(f"Occurence N°{occurence}")
            result = first
            result['office'] += f" commemoraison à laude et à vêpres : {second['title']}" # exception
            
        elif occurence == 4:
            print(f"Occurence N°{occurence}")
            result = first
            result['office'] += f" commemoraison à laude : {second['title']}" # exception
            
        elif occurence == 5:
            print(f"Occurence N°{occurence}")
            result = second
            result['office'] += f" commemoraison à laude : {first['title']}" # exception

        elif occurence == 6:
            print(f"Occurence N°{occurence}")
            result = first
            # translation of second
            
        elif occurence == 7:
            print(f"Occurence N°{occurence}")
            result = second
            # translation of first
            
        elif occurence == 8:
            print(f"Occurence N°{occurence}")
            result = max(first, second, key=lambda x: x["rank"])
            lower = min(first, second, key=lambda x: x["rank"])
            # translation of lower
            
        elif occurence == 9:
            print(f"Occurence N°{occurence}")
            result = max(first, second, key=lambda x: x["rank"])
            lower = min(first, second, key=lambda x: x["rank"])
            # translation of lower
            
        else:
            pass
        
        return result
    