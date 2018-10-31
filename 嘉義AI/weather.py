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

plt.hist(heights)
plt.title('Height Distribution of is US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
