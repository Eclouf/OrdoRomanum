# -*- encoding:utf-8 -*-
import pandas as pd # type: ignore


"""
    test for the table of contents 
    determining the structure of the vepres based on the second vepres of the day and the first vepres of the following day.
"""

class ContentsCtrl:
    def __init__(self):
        self.__only__ = ['f1', 'f2', 'f3', 'f4', 'F2', 'F3', 'jio2']
        self.__ordinate__ = ['D1', 'D2', 'f1', 'f2', 'f3', 'f4', 'F1', 'F2', 'F3', 'jio2']
        self.__abcissa__ = ['F1', 'D2', 'D1']
        self.__data__ = [
            [1,0,0],
            [2,0,0],
            [1,0,0],
            [2,0,0],
            [2,0,0],
            [3,0,0],
            [1,1,1],
            [3,1,3],
            [3,3,3],
            [2,3,0]
        ]

        # Creat table of competition
        self._table_competition_ = pd.DataFrame(self.__data__, index=self.__ordinate__, columns=self.__abcissa__)

        
    def search(self, day0, day1):
        # Determination of festivities on the x-axis and y-axis for self._table_competition_
        if day0['con'] in self.__only__:
            first = day0   # y-axis
            second = day1  # x-axis
        elif day1['con'] in self.__only__:
            first = day0
            second = day1 
        else:
            first = day0
            second = day1
            
        # Search competition : 
        x = first['con']
        y = second['con']
        competition = self._table_competition_.loc[x,y]
    
        if competition == 1:
            print(competition)
            result = day0
            result['office'] += f"commemoraison aux vêpres des premières vêpres de {day1['title']}" # exception
            
        elif competition == 2:
            print(competition)
            result = day0
            result['office'] += f"première vêpres de {day1['title']} et commémoraison de {day0['title']}" # exception
            
        elif competition == 3:
            print(competition)
            result = day0
            result['office'] += f"première vêpres : {day1['title']}" # exception
            
        else:
            pass
        
        return result
    