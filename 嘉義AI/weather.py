# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

#計算美國總統的平均身高
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print (heights)
#聚合運算
print ("Mean height :        ",heights.mean())#平均數
print ('Standard deviation : ',heights.std())#標準差
print ('Variation deviation : ',heights.var())#變異量
print ('Minimum height :     ',heights.min())
print ('Maximun height :     ',heights.max())

#計算出中位數 百分位數
print ('25th percentile :    ',np.percentile(heights , 25))
print ('Median :             ',np.median(heights))
print ('75th percentile :    ',np.percentile(heights , 75))

import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import seaborn as sns

plt.hist(heights)
plt.title('Height Distribution of is US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
numpy的聚合函式
np.sum
np.prod 計算乘積可以透過axis指定軸向
np.mean 均值
np.std  標準差
np.var  變異量
np.min  
np.max
np.argmin 最小值的索引
np.argmax
np.median  中位數
np.percentile 排名統計
np.any        當陣列中有任一值是True or not 0 時傳回True
np.all        當陣列中有所有值是True or not 0 時傳回True


set_style( )  set( )

set_style( )是用来设置主题的，Seaborn有五个预设好的主题： darkgrid , whitegrid , dark , white ,和 ticks  默认： darkgrid
sns.set_style("whitegrid")

set( )通过设置参数可以用来设置背景，调色板等，更加常用
sns.set(style="white", palette="muted", color_codes=True)     #set( )设置主题，调色板更常用

