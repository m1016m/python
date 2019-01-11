# -*- coding: utf-8 -*-
"""
07_Data_Wrangling_03_20170104.py
Created on Wed Jan  4 15:32:16 2017
@author: zzjack
"""
#Import Conventions
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from pandas import DataFrame,Series

#Merging on Index 
#pass left_index=True or right_index=True (or both) to indicate that the
#index should be used as the merge key:
df1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
df2 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

df1
df2

pd.merge(df1,df2,left_on='key',right_index=True) #left_on, right_index, inner join
pd.merge(df1,df2,left_on='key',right_index=True,how='outer') #outer join

#-----------------------------------------------------------------------------
#hierarchically-indexed data, 層次化索引
df3 = DataFrame({'city': ['高雄', '高雄', '高雄', '台南', '台南'],
                 'year': [2010, 2011, 2011, 2011, 2012],
                 'data': np.arange(5.)})
                
df4 = DataFrame(np.arange(12).reshape((6, 2)),
                index=[['台南', '台南', '高雄', '高雄', '高雄', '高雄'],
                [2011, 2010, 2010, 2010, 2011, 2012]], #第二層索引
                columns=['event1', 'event2'])
                
#In this case, you have to indicate multiple columns to merge on as a list
#inner join
pd.merge(df3,df4,left_on=['city','year'],right_index=True,how='inner')
#outer join
pd.merge(df3,df4,left_on=['city','year'],right_index=True,how='outer')

#DataFrame_obj.join() method
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
                  
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])

left2.join(right2,how='outer')







