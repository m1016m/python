# -*- coding: utf-8 -*-
"""
Example4_tips.py

@author: zzjack
"""
#Data Aggregation
#any data transformation that produces scalar values from arrays.
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt
# %pylab


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#高級聚合功能說明: 以餐廳小費資料(tips.csv) 說明
#以pd.read_csv() 將tips.csv 讀入成一個 DataFrame
tips=pd.read_csv('tips.csv') 
tips #display DataFrame tips

#新增一個欄位 ['tip_pct']
tips['tip_pct']=tips['tip']/tips['total_bill']

tips[:6] #display 前五列

#Column-wise and Multiple Function Application:
#example 3: 對不同的column使用不同的聚合函數-->
grouped_02=tips.groupby(['sex','smoker']) 

grouped_pct=grouped_02['tip_pct'] #pandas.core.groupby.SeriesGroupBy object
grouped_pct.agg('mean') #or grouped_pct.mean() 

#上述程式碼可合併為:
tips.groupby(['sex','smoker'])['tip_pct'].mean()
#對應的SQL: select avg(tip_pct) from tips group by sex,smoker;

#example 3: 一次應用多個函數(peak_to_peak 是自訂函數)
def peak_to_peak(arr):           #定義一個函數 peak_to_peak()
    return arr.max()-arr.min()
    
grouped_pct.agg(['mean','std',peak_to_peak]) #一次應用多個函數

#example 4: 一次應用多個函數,並自行對結果column命名, (二元tuple形式)
grouped_pct.agg([('平均','mean'),('標準差','std'),('峰值',peak_to_peak)])

#example 5:
grouped_tip=grouped_02['tip'] #只對小費tip column 動作
grouped_tip.agg([('最高小費','max'),('平均小費','mean')])

#example 6: compute the same three statistics for the tip_pct and total_bill columns:
functions=['count','mean','max'] #定義一個list 
result=grouped_02['tip_pct','total_bill'].agg(functions)

result #display result

result['tip_pct'] #display result['tip_pct']

#example 7: a list of tuples with custom names can be passed:
ftuples=[('平均值','mean'),('變異值',np.var)]
result=grouped_02['tip_pct','total_bill'].agg(ftuples)

result

result['tip_pct']

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 8: 要對不同的column應用不同的函數, 做法是叫用agg時
#           傳入一個從column name 映射到函數的字典

grouped_02.agg({'tip':np.max,'size':'mean'}) 

grouped_02.agg({'tip':['min','max','mean','std'],
                'size':'mean'})
                
#example 9: 傳回不具索引的結果, as_index=False
tips.groupby(['sex','smoker'],as_index=False).mean()

#比較
tips.groupby(['sex','smoker']).mean()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#make a cross-tabulation (交叉分析) by day and party size:
tips #先看原始資料
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




