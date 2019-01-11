# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_07_20160925.py

@author: zzjack
"""
#Data Aggregation
#Apply: General split-apply-combine
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

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#以餐廳小費資料(tips.csv) 說明
#以pd.read_csv() 將tips.csv 讀入成一個 DataFrame
tips=pd.read_csv('tips.csv') 
tips #display DataFrame tips

#新增一個欄位 ['tip_pct']
tips['tip_pct']=tips['tip']/tips['total_bill']

tips[:6] #display 前五列

#apply splits the object being manipulated into pieces,
#invokes the passed function on each piece, then
#attempts to concatenate the pieces together

#example 1: tips

#定義一個top()函數, 依指定column 排序後取前 n row
def top(df, n=5, column='tip_pct'):
    return df.sort_index(by=column,ascending=False)[:n]

#叫用top(),測試
top(tips,n=5,column='tip_pct')
     
#group by smoker, and call apply(top)
tips.groupby('smoker').apply(top)
#group by sex, and call apply(top(tips,n=3,column='tip'))
tips.groupby('sex').apply(top,n=3,column='tip')

#example 2:
tips.groupby(['smoker','day']).apply(top,n=1,
             column='total_bill')

#+++++++++++++++++++++++++++++++++++++++++++++++
#example 2: describe() 說明:
result=tips.groupby('smoker')['tip_pct'].describe()

result

result.unstack('smoker')

#上述叫用 describe() 其實是下列兩行程式縮寫:
f= lambda x:x.describe()
result=tips.groupby('smoker')['tip_pct'].apply(f)





