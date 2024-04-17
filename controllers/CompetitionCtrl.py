# -*- encoding:utf-8 -*-
import pandas as pd # type: ignore

"""
    test for the table of competition 
    determining the structure of the vepres based on the second vepres of the day and the first vepres of the following day.
"""
# For test 2 dict for 2 fests
festA = {'office':'office of A','rank':8500, 'occ':'F1U', 'con':'jio2'}
festB = {'office':'office of B','rank':150, 'occ':'D1', 'con':'F1'}

class CompetitionCtrl():
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

        # Affichage du DataFrame
        print(self._table_competition_)
        
    def search(self, fest1, fest2):
        # Determination of festivities on the x-axis and y-axis for self._table_competition_
        if fest1['con'] in self.__only__:
            first = fest1   # y-axis
            second = fest2  # x-axis
        elif fest2['con'] in self.__only__:
            first = fest2
            second = fest1 
        else:
            first = fest1
            second = fest2
            
        # Search competition : 
        x = first['con']
        y = second['con']
        competition = self._table_competition_.loc[x,y]
        print(competition)

        if competition == 1:
            pass
        elif competition == 2:
            pass
        elif competition == 3:
            pass
        else:
            pass

test = CompetitionCtrl()
test.search(festA, festB)