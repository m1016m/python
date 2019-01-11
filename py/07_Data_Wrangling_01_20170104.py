# -*- coding: utf-8 -*-
"""
07_Data_Wrangling_01_20170104.py
Created on Wed Jan  4 09:41:01 2017
@author: zzjack
"""
#Import Conventions
import pandas as pd
from pandas import DataFrame

#Database-style DataFrame Merges, merge, join
df1=DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],  \
                         'data1': range(7)})

df2=DataFrame({'key':['a','b','d'],'data2':range(3)})

#merge df1,df2 pd.merge(df1,df2)
#SQL--> join on df1.key=df2.key
pd.merge(df1,df2) #未指名合併列, merge以重疊列 (這裡是 key )當合併鍵
pd.merge(df1,df2,on='key') #最好還是清楚指名
pd.merge(df1,df2,on='key',how='inner') #預設是inner join 

#If the column names are different in each object,
#you can specify them separately:
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], \
                 'data1': range(7)})
                 
df4 = DataFrame({'rkey': ['a', 'b', 'd'],'data2': range(3)})  

pd.merge(df3,df4,left_on='lkey',right_on='rkey') #指定兩邊的合併鍵  

#----------------------------------------------------------------
#outer join
df1 #display df1 #key 有 ('a','b','c')
df2 #display df2 #key 有 ('a','b','d')

pd.merge(df1,df2,on='key',how='inner')  #inner join, c,d 不會出現

pd.merge(df1,df2,on='key',how='left') #left outer join, 顯示左邊背景 c   

pd.merge(df1,df2,on='key',how='right') #right outer join, 顯示右邊背景 d    

pd.merge(df1,df2,on='key',how='outer') #full outer join, 顯示兩邊背景 c,d 
                 
#------------------------------------------------------------------------
#To merge with multiple keys, pass a list of column names:
df5 = DataFrame({'key1': ['高雄', '高雄', '台南'], \
                 'key2': ['one', 'two', 'one'],   \
                 'lval': [1, 2, 3]})
                 
df6 = DataFrame({'key1': ['高雄', '高雄', '台南', '台南'], \
                 'key2': ['one', 'one', 'one', 'two'],    \
                 'rval': [4, 5, 6, 7]})

pd.merge(df5,df6,on=['key1','key2'],how='inner') #以['key1','key2']為join鍵,inner join

pd.merge(df5,df6,on=['key1','key2'],how='outer') #以['key1','key2']為join鍵,outer join

#-------------------------------------------------------------------------
#the treatment of overlapping column names. -->suffixes
pd.merge(df5,df6,on='key1',how='inner') #key2 重複列名
pd.merge(df5,df6,on='key1',how='inner',suffixes=('_df5','_df6')) #suffixes







                 
                 
                 