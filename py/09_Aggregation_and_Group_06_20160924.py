# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_06_20160924.py

@author: zzjack
"""
#Data Aggregation
#Group-wise Operations and Transformations

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#create DataFrame df
dict_01={'data1':np.random.randn(5),
         'data2':np.random.randn(5),
         'key1':['a','a','b','b','a'],
         'key2':['one','two','one','two','one']}

df=DataFrame(dict_01)

df

#+++++++++++++++++++++++++++++++++++++++++++++++++++
#example 1: add a column to a DataFrame containing group means for each index.
#           One way to do this is to aggregate, then merge:


#第一種作法, step 1: 先分組聚合
df.groupby('key1').mean() #以'key1'分組,聚合函數為mean()
df.groupby('key1').mean().add_prefix('mean_') #加上前置字串
k1_means=df.groupby('key1').mean().add_prefix('mean_')

k1_means

#第一種作法, step 2:再以merge() 合併
pd.merge(df, k1_means, left_on='key1',right_index=True)

#example 2: transform

#create DataFrame people
people=DataFrame(np.random.randn(5,5),
                 columns=['a','b','c','d','e'],
                 index=['Jack','Mary','Joe','Jim','Smith'])
                 
people #display 

key=['one','two','one','two','one'] #list key

people.groupby(key).max()

people.groupby(key).transform(np.max)

people.groupby(key).mean()

people.groupby(key).transform(np.mean)

#定義一個 demeaning function
def demean(arr):
    return arr-arr.mean()
    
demeaned=people.groupby(key).transform(demean)

demeaned

demeaned.groupby(key).mean()







