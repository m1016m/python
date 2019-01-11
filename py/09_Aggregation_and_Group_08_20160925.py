# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_08_20160925.py

@author: zzjack
"""
#Quantile and Bucket Analysis

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#將 cut, qcut 與groupby結合-->實作 bucket or quantile 分析

#example 1: 

#create DataFrame 
frame=DataFrame({'data1':np.random.randn(1000),
                 'data2':np.random.randn(1000)})
                 
frame #display

#以pandas.cut()將frame.data1 分為四等第
factor=pd.cut(frame.data1, 4, labels=['甲','乙','丙','丁']) #pandas.cut()

factor[:10] #display

#+++++++++++++++++++++++++++++++++++++++++++++++++++
#example of pd.cut() pd.qcut()
#pd.cut()
pd.cut(np.array([1, 2, 3, 4, 5, 6, 7, 11]), 3)  #沒labels

pd.cut(np.array([1, 2, 3, 4, 5, 6, 7, 11]), 3,
                labels=['甲','乙','丙'])    #加labels 

#pd.qcut() #Quantile-based discretization function.
#Quantile, 常用的有中位數（即二分位數）、四分位數、百分位數等
pd.qcut(np.array([1, 2, 3, 4, 5, 6, 7, 11]), 4)  #沒labels

pd.qcut(np.array([1, 2, 3, 4, 5, 6, 7, 11]), 4,
                labels=['甲','乙','丙','丁'])    #加labels 

#+++++++++++++++++++++++++++++++++++++++++++++++++++

type(factor) #factor 是 Series Object

#由cut()傳回的factor可以直接用於groupby:
#定義函數 get_stats()
def get_stats(g):    #定義函數 get_stats()
    return {'最小':g.min(),'最大':g.max(),
            '計數':g.count(),'平均':g.mean()}

#將frame.data2 以 factor 作groupby
grouped=frame.data2.groupby(factor)

#將grouped (SeriesGroupBy Object) 以apply()叫用 get_stats()
get_grouped=grouped.apply(get_stats)

#將get_grouped 用unstack()摺回來
get_grouped.unstack()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 2: pandas.qcut()
            
grouping=pd.qcut(frame.data1, 10, labels=False)
grouped=frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()



          
            



