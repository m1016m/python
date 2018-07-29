import numpy as np
import pandas as pd

table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])

B = df.groupby('class').mean()
A = df.groupby('class').sum()
p = pd.concat([B, A],axis = 1,join = 'outer')

print (A)
print(p)

#print (df.describe())
print (df.corr())

