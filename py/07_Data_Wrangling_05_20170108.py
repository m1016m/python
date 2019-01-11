# -*- coding: utf-8 -*-
"""
07_Data_Wrangling_05_20170108.py
Created on Sun Jan  8 11:01:29 2017
@author: zzjack
"""
#Import Conventions
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from pandas import DataFrame,Series

#concatenate data, DataFrame Object, pd.concat()
df1=DataFrame(np.arange(6).reshape(3,2),index=['a','b','c']
              ,columns=['甲','乙'])

df2=DataFrame(2*np.arange(4).reshape(2,2),index=['a','c']
              ,columns=['丙','丁'])

df1
df2

#axis=1, join='outer'/join='inner'
pd.concat([df1,df2],axis=1) #沿軸1(-->),預設為 join='outer', like SQL outer join
pd.concat([df1,df2],axis=1,join='outer')
pd.concat([df1,df2],axis=1,join='inner') #改為 join='inner', like SQL inner join

#axis=0, join='outer' /join='inner'
pd.concat([df1,df2],axis=0) #沿軸0, 預設為 outer join
pd.concat([df1,df2],axis=0,join='outer')
pd.concat([df1,df2],axis=0,join='inner') #沿軸0, inner join

#如果參數是字典而不是list
pd.concat({'level1':df1,'level2':df2},axis=1)
pd.concat({'level1':df1,'level2':df2},axis=1,join='inner')

#ignore_index
df3=DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df4=DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
pd.concat([df3, df4], ignore_index=True)










