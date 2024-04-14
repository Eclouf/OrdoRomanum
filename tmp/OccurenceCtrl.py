# -*- encoding:utf-8 -*-
import pandas as pd

"""
    test for the table of occurence 
"""

ordinate = ['F1U', 'F1P', 'F2U', 'F2P', 'F3U', 'F3P', 'V2', 'V3']
abcissa = ['O2', 'O1', 'F3P', 'F3U', 'F2P', 'F2U', 'F1P', 'F1U', 'V2', 'V1', 'f3C', 'f3A', 'f2', 'f1', 'D2', 'D1']
data = [
    [3, 7, 1, 1, 1, 1, 6, 8, 1, 7, 3, 3, 3, 7, 3, 7],
    [3, 7, 1, 1, 1, 1, 8, 7, 1, 7, 3, 3, 3, 7, 3, 7],
    [3, 2, 4, 4, 4, 0, 2, 2, 4, 2, 3, 3, 3, 2, 5, 2],
    [0, 2, 4, 4, 9, 5, 2, 2, 4, 2, 3, 3, 5, 2, 5, 2],
    [0, 2, 5, 0, 5, 5, 2, 2, 5, 2, 5, 3, 5, 2, 2, 2],
    [0, 2, 9, 4, 5, 5, 2, 2, 5, 2, 5, 3, 5, 2, 2, 2],
    [0, 0, 4, 4, 5, 5, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 5, 0, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0]
]

# Creat table of occurence
table_occurence = pd.DataFrame(data, index=ordinate, columns=abcissa)

# Affichage du DataFrame
print(table_occurence)

# Search occurence : 
x = 'F1P'
y = 'f3C'
occurence = table_occurence.loc[x,y]
print(occurence)

# Tyoes of occurence :
# 8 types
