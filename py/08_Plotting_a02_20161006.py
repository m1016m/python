# -*- coding: utf-8 -*-
"""
08_Plotting_a02_20161006.py
Created on Mon Oct  3 08:58:54 2016

@author: zzjack
"""
#Plotting and Visualization
#Plotting Functions in pandas

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
#%pylab 

#pandas has an increasing number of high-level plotting methods for creating standard 
#visualizations that take advantage of how data is organized in DataFrame objects.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Line Plots

#Series and DataFrame each have a plot method for making many different plot types.
#By default, they make line plots

#example 1: Series.plot()
s=Series(np.random.randn(10).cumsum(), #create Series Object s
         index=np.arange(0,100,10))

s #display

s.plot() 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 2: DataFrame.plot()
df=DataFrame(np.random.randn(10,4).cumsum(0),
             columns=['A','B','C','D'],
             index=np.arange(0,100,10)) #create a DataFrame Object df

df #display   

df.plot()  

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Bar Plots
#example 3: Series.plot()
fig, axes=plt.subplots(2,1)

s_data=Series(np.random.rand(16),   #Series Object s_data
              index=list('abcdefghijklmnop'))   

s_data #display
#kind='bar'
s_data.plot(kind='bar', ax=axes[0], color='r', alpha=0.7)
#kind='barh'
s_data.plot(kind='barh',ax=axes[1], color='g',alpha=0.3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 4: DataFrame.plot()
df=DataFrame(np.random.rand(6,4),
             index=['one','two','three','four','five','six'],
             columns=pd.Index(['A','B','C','D'],
             name='Genus'))

df #display

df.plot(kind='bar') 

#example 5: stacked=True
df.plot(kind='barh',stacked='True',alpha=0.5)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#以餐廳小費資料(tips.csv) 說明
#以pd.read_csv() 將tips.csv 讀入成一個 DataFrame
tips=pd.read_csv('tips.csv') 

#新增一個欄位 ['tip_pct']
tips['tip_pct']=tips['tip']/tips['total_bill']

tips[:6] #display DataFrame tips

#make a cross-tabulation by day and party size:
party_counts=pd.crosstab(tips['day'], tips['size'])

party_counts # display

#normalize so that each row sums to 1
party_pcts=party_counts.div(party_counts.sum(1).astype(float),axis=0)

party_pcts #display

party_pcts.plot(kind='bar',stacked=True) #plot party_pcts

party_counts.plot(kind='bar',stacked=True) #plot party_counts

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Histograms and Density Plots
#example 5: 小費百分比 histgram / KDE(Kernel Density Estimate)
tips[:6] #display tips

tips['tip_pct'].hist(bins=50) #histgram

tips['tip_pct'].plot(kind='kde') #小費百分比的密度圖

#example 6: 雙峰分佈
comp1=np.random.normal(0,1, size=200) 
comp2=np.random.normal(10,2,size=200) 
values=Series(np.concatenate([comp1,comp2]))
values.hist(bins=100,alpha=0.3, color='g',normed=True)
values.plot(kind='kde',style='k--')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Scatter Plots
#Scatter plots are a useful way of examining the relationship 
#between two one-dimensional data series.

#example 7: Statsmodels macrodata.csv
#Statsmodels is a Python module that allows users to explore data,
#estimate statistical models, and perform statistical tests.

#讀取 macrodata.csv
macro=pd.read_csv('D:\workspace\python\data\macrodata.csv')

macro.head(10) #檢視前10筆

data=macro[['cpi','m1','tbilrate','unemp']] #擷取這些欄

trans_data=np.log(data).diff().dropna() #計算對數差

trans_data.tail(5) #檢視後5筆

plt.scatter(trans_data['m1'],trans_data['unemp'])

#scatter_matrix()
pd.scatter_matrix(trans_data, diagonal='kde',alpha=0.3)



























