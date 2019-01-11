# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_02_20160912.py
Created on Mon Sep 12 10:04:47 2016
@author: zzjack
"""
#Iterating Over Groups
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The GroupBy object supports iteration, generating a sequence of 2-tuples containing
#the group name along with the chunk of data.
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab

#create a DataFrame df
df=DataFrame({'key1':['a','a','b','b','c','a'],
              'key2':['甲','甲','丙','丙','甲','乙'],
              'data1':np.arange(110.0,170.0,10),
              'data2':np.random.randn(6)})
              
#display DataFrame df
df

#df 加上 years,cities 欄位及值
years=np.array([2012,2013,2012,2014,2013,2013]) #numpy.ndarray

cities=np.array(['高雄','高雄','台北','台南','高雄','台北']) #numpy.ndarray

df['years']=years #df 加上 'years' column

df['cities']=cities #df 加上 'cities' column

df #display df

#++++++++++++++++++++++++++++++++++++++++++++++++++
#In the case of multiple keys, the first element in the tuple will be a tuple of key values:
#example 1: 以for對Groupby object 做迭代,回傳的是一組2元tuple
for g_name,group in df.groupby('key1'):
    print(g_name)
    print(group)
    
#example 2: 多重鍵分組, groupby(['key1','key2'])
for (k1,k2),group in df.groupby(['key1','key2']):
    print(k1,k2)
    print(group)

#多重鍵分組, groupby(['years','cities'])
for (y,c),group in df.groupby(['years','cities']):
    print(y,c)
    print(group)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 3: 將Groupby object, 作成字典:
dict_groupby=dict(list(df.groupby('cities')))

dict_groupby #display dict dict_groupby

dict_groupby['台北'] #在 dict dict_froupby 中,以key ['台北'] 取值(一個DataFrame Object)

#++++++++++++++++++++++++++++++++++++++++++++++++++++
#By default groupby groups on axis=0,but you can group on any of the other axes.
grouped=df.groupby(df.dtypes,axis=1)

dict(list(grouped))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Selecting a Column or Subset of Columns

#Indexing a GroupBy object created from a DataFrame with a column name or array of
#column names has the effect of selecting those columns for aggregation.

#example 1:
#以('key1')對df分組後,以column name ['data1'] 為索引 (group by 對象縮減為 df['data1'])
#aggregate function 為sum()
df.groupby('key1')['data1'].sum()

#等同於(syntactic sugar for:)
df['data1'].groupby(df['key1']).sum()

#example 1a:
#以('years')作分組鍵對df分組後,以column name['data2']為索引,聚合函數為mean()
df.groupby('years')['data2'].mean()

#練習: syntactic sugar for:
df['data2'].groupby(df['years']).mean()

#example 1b:
#以(['years','cities'])作階層分組鍵對df分組後,
#以column name['data1']為索引,聚合函數為sum()
df.groupby(['years','cities'])['data2'].sum()

#example 1c:
#以(['years','cities'])作階層分組鍵對df分組後,
#以column name[['data1','data2']]為索引,聚合函數為sum()

df.groupby(['years','cities'])[['data1','data2']].sum()

#這種索引操作回傳的是:
#1.a grouped DataFrame --> if a list or array is passed
#2.a grouped Series --> if just a single column name that is passed as a scalar

s_grouped=df.groupby(['key1','key2'])['data2']

type(s_grouped)

s_grouped.mean()










