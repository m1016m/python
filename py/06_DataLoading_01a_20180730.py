# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:21:25 2018
06_DataLoading_01a_20180730.py
@author: zzjack
"""
import pandas as pd

# 檢視 'twseJuly_t.csv' 
# !type twseJuly_t.csv

#以pd.read_csv() 讀取 file 成為 DataFrame
df=pd.read_csv('twseJuly_t.csv',skiprows=[0,23,24,25])

#檢視 df 
df

#將不要的column 'Unnamed: 6' drop
df=df.drop(columns='Unnamed: 6')
df

#以set_index() 將 column '日期' 設成 index
df=df.set_index('日期')
df

#目前 df 中除了 df['漲跌點數'] 為 float 其餘皆為 str
type(df['成交股數']['107/07/02']) #str
type(df['漲跌點數']['107/07/11']) #numpy.float64

#將 str 轉成 float
#先將 str 中 ',' 刪除
fun=lambda s:s.replace(',','') 
df1=df[['成交股數', '成交金額', '成交筆數', 
       '發行量加權股價指數']].applymap(fun)
#再將 str 轉成 float
fun2=lambda s:float(s)
df2=df1[['成交股數', '成交金額', '成交筆數', 
       '發行量加權股價指數']].applymap(fun2)
df2['漲跌點數']=df['漲跌點數'] #將'漲跌點數' 加回來

#繪圖
#%pylab
df2['成交股數'].plot()

