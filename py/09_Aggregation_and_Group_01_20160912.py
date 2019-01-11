# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:36:59 2016
09_Aggregation_and_Group_01_20160912.py
@author: zzjack
"""
#資料準備好後, 分組統計(compute group statistics, groupby)或產生
#透視表(pivot tables for reporting or visualization purposes.)
#groupby:對資料分組，並對各組應用一個函數(聚合或轉換或apply函數)
#In this chapter, you will learn how to:
# 1. Split a pandas object into pieces using one or more keys (in the form of functions,
#    arrays, or DataFrame column names)
# 2. Computing group summary statistics, like count, mean, or standard deviation, or
#    a user-defined function
# 3. Apply a varying set of functions to each column of a DataFrame
# 4. Apply within-group transformations or other manipulations, like normalization,
#    linear regression, rank, or subset selection
# 5. Compute pivot tables and cross-tabulations
# 6. Perform quantile analysis (分位數分析) and other data-derived group analyses

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#GroupBy Mechanics

# example1: 
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab

#create a DataFrame object df
df=DataFrame({'key1':['a','a','b','b','a'],
              'key2':['one','two','one','two','one'],
              'data1':np.random.randn(5),
              'data2':np.random.randn(5)})

#display df
df

#compute the mean of the data1 column using the groups labels from key1
groupd=df['data1'].groupby(df['key1'])

type(groupd) #groupd--> pandas.core.groupby.SeriesGroupBy
#             This grouped variable is now a GroupBy object. 
#             It has not actually computed anything

#將分組物件(SeriesGroupBy) groupd 套用mean() 聚合函數
groupd.mean()

#或是:
groupd_mean=df['data1'].groupby(df['key1']).mean()

#display groupd_mean
groupd_mean

type(groupd_mean) #pandas.core.series.Series

#上例對應的SQL -->
#SELECT AVG(df['data1']) FROM df GROUP BY df['key1'] 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 2: we had passed multiple arrays as a list
means_2=df['data1'].groupby([df['key1'],df['key2']]).mean()

#display means_2, the resulting Series now has a hierarchical index
means_2

#上例對應的SQL --> (means_2)
#SELECT AVG(df['data1']) FROM df GROUP BY df['key1'],df['key2']

#我們可以unstack() 將具層次化索引的Series物件轉成DataFrame物件
us=means_2.unstack('key1')
us
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 4: 上述各例中，皆是以Series為分組鍵。
#           其實 group keys could be any arrays of the right length

#create two numpy.ndarray object: cities,years
cities=np.array(['高雄','台南','台南','高雄','高雄'])

years=np.array([2011,2011,2013,2013,2013])

#我們先修改一下DataFrame df 的值:
df['data1']=np.arange(10,60,10)
df['data2']=np.arange(2.0,12.0,2.0)
df

#將df['data1'] (Series) 值, group by cities 後 sum()
#SQL--> SELECT SUM(df['data1']) FROM df GROUP BY cities
df['data1'].groupby(cities).sum()

#將df['data2']值,group by years 後 mean()
#SQL--> SELECT AVG(df['data2']) FROM df GROUP BY years
df['data2'].groupby(years).mean()

#將df['data1'], group by [cities,year] 後 sum()
#SQL--> SELECT SUM(df['data1']) FROM df GROPY BY cities,years
dfcy=df['data1'].groupby([cities,years]).sum()

#為了方便,我們將cities,years 各作成一個欄位加到 df
df['cities']=cities
df['years']=years

df 

#上例可改寫為:
groupd_3=df['data1'].groupby([df['cities'],df['years']]).sum()

groupd_3
#再unstack('cities')
groupd_3.unstack('cities')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#nuisance column(麻煩列) 說明:
df #display df
df.groupby('key1').sum()

#我們對整個df,以key1欄位分組後加總。key2,cities欄位
#不是數值資料,我們稱為nuisance column(麻煩列),所以從結果中排除
#但請注意years欄位雖是數值資料也計算出結果,但是卻不具意義!

#以years欄位為分組鍵
df.groupby('years').sum()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Groupby 的 size() method
df

df.groupby([df['cities'],df['years']]).size()

df['data1'].groupby(df['years']).size()

























