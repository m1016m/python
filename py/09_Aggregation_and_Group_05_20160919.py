# -*- coding: utf-8 -*-
"""
09_Aggregation_and_Group_05_20160919.py

@author: zzjack
"""
#Data Aggregation
#any data transformation that produces scalar values from arrays.
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

#groupdy('key1)
grouped=df.groupby('key1')

type(grouped) #pandas.core.groupby.DataFrameGroupBy

grouped.quantile(0.9) #quantile() 

grouped['data1'].min() #只對 ['data1'] 欄位

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#To use your own aggregation functions, pass any function that aggregates an array to
#the aggregate or agg method:

#example 1:
def peak_to_peak(arr):           #定義一個函數 peak_to_peak()
    return arr.max()-arr.min()

#DataFrameGroupBy Object grouped 以agg叫用自訂函數peak_to_peak
grouped.agg(peak_to_peak)

grouped.aggregate(peak_to_peak) #aggregate 也可以

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#有些函數嚴格來講並非聚合函數，(像describe)但仍適用:
#example 2:
grouped.describe()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#高級聚合功能說明: 以餐廳小費資料(tips.csv) 說明
#以pd.read_csv() 將tips.csv 讀入成一個 DataFrame
tips=pd.read_csv('tips.csv') 
tips #display DataFrame tips

#新增一個欄位 ['tip_pct']
tips['tip_pct']=tips['tip']/tips['total_bill']

tips[:6] #display 前五列

#Column-wise and Multiple Function Application:
#example 3a: 對不同的column使用不同的聚合函數-->
grouped_02=tips.groupby(['sex','smoker']) 

grouped_pct=grouped_02['tip_pct'] #pandas.core.groupby.SeriesGroupBy object
grouped_pct.agg('mean') #or grouped_pct.mean() 

#縮短(改寫)example 3a:
tips['tip_pct'].groupby([tips['sex'],tips['smoker']]).mean()

#-------------------------------------------------------------------------
#example 3: 一次應用多個函數
grouped_pct.agg(['mean','std',peak_to_peak])
#縮短(改寫)example 3:
tips['tip_pct'].groupby([tips['sex'],tips['smoker']]).agg(['mean','std',peak_to_peak])

#---------------------------------------------------------------------------
#example 4: 一次應用多個函數,並自行對結果column命名, (二元tuple形式)
grouped_pct.agg([('平均','mean'),('標準差','std'),('峰值',peak_to_peak)])
#縮短(改寫)example 4:
tips['tip_pct'].groupby([tips['sex'],tips['smoker']]).agg([('平均','mean'),('標準差','std'),('峰值',peak_to_peak)])

#--------------------------------------------------------------------
#example 5:
grouped_tip=grouped_02['tip'] #只對小費tip column 動作
grouped_tip.agg([('最高小費','max'),('平均小費','mean')])
#縮短(改寫)example 5:
tips['tip'].groupby([tips['sex'],tips['smoker']]).agg([('最高小費','max'),('平均小費','mean')])


#-----------------------------------------------------------------
#example 6: compute the same three statistics for the tip_pct and total_bill columns:
functions=['count','mean','max'] #定義一個list 
result=grouped_02['tip_pct','total_bill'].agg(functions)

result #display result

result['tip_pct'] #display result['tip_pct']

#----------------------------------------------------------------
#example 7: a list of tuples with custom names can be passed:
ftuples=[('平均值','mean'),('變異值',np.var)]
result=grouped_02['tip_pct','total_bill'].agg(ftuples)

result

result['tip_pct']

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 8: 要對不同的column應用不同的函數, 做法是叫用agg時
#           傳入一個從column name 映射到函數的字典

grouped_02.agg({'tip':np.max,'size':'sum'}) 

grouped_02.agg({'tip_pct':['min','max','mean','std'],
                'size':'sum'})
                
#example 9: 傳回不具索引的結果, as_index=False
tips.groupby(['sex','smoker'],as_index=False).mean()

#比較
tips.groupby(['sex','smoker']).mean()






