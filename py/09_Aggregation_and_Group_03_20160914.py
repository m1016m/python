# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_03_20160912.py
Created on Wed Sep 14 21:10:23 2016

@author: zzjack
"""
#Grouping with Dicts and Series
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab

#create a DataFrame prople
people=DataFrame(np.random.randn(5,5),
                 columns=['a','b','c','d','e'],
                 index=['Jack','Angel','Sean','Sabrina','Joe'])

#display DataFrame people
people

#添加一些NA值
people.ix[2:3,['b','c']]=np.nan

people

#+++++++++++++++++++++++++++++++++++++++++++++++
#example 1: 
#suppose I have a group correspondence for the columns and want to sum together
#the columns by group:
#dict mapping
mapping={'a':'red','b':'red','c':'blue',
         'd':'blue','e':'red','f':'orange'}

#將dict mapping 傳給groupby, axis=1--> 以y軸動作
by_column=people.groupby(mapping,axis=1)

by_column.sum()

#++++++++++++++++++++++++++++++++++++++++++++++++
#example 2:
#The same functionality holds for Series:
map_series=Series(mapping)

map_series

people.groupby(map_series,axis=1).count()

#++++++++++++++++++++++++++++++++++++++++++++++++++++
#Grouping with Functions
#Any function passed as a group key will be called once
#per index value, with the return values being used as the group names.
#example 3:
people

#groupby(len)-->依index長度(姓名長度分組),套用函數為max()
people.groupby(len).max() 

#Mixing functions with arrays, dicts, or Series is not a problem as everything gets converted
#to arrays internally:         
#example 4:
#先新增 one row 到 people
people2=DataFrame(data=np.random.randn(1,5),
                  columns=['a','b','c','d','e'],
                  index=['sun'])
people=people.append(people2) #將people2 append 到 people

people #display DataFrame people


key_list=['one','one','two','two','two','two'] #list key_list

people.groupby(len).min()
people.groupby(key_list).min()

people.groupby([len,key_list]).min()









