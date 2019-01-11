# -*- coding: utf-8 -*-
"""
05_panda_02a_20170125.py
DataFrame 中場練習
Created on Wed Jan 25 10:28:30 2017
@author: zzjack
"""
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------
#練習1:六都人口與土地面積 
#      字典 dict_city 建構成 DataFrame df_city
dict_city={'都':['臺北','新北','桃園','臺中','臺南','高雄'],
           '人口':[2695704,3979208,2147763,2767239,1886033,2779371],
           '土地':[271,2052,1220,2214,2191,2952]}

#練習2:增加市長column及值
mayor=['柯文哲','朱立倫','鄭文燦','林佳龍','賴清德','陳菊']

#練習3: reindex  df dict_city with column '都'
#       df2_city

#練習4:擷取 df2_city column'人口' 成 s_population Series
#      擷取 df2_city column'土地' 成 s_area Series

#練習5: 畫圖展示六都人口與土地
 





















        
#-------------------------------------------------------------------
#練習1 解答
df_city=DataFrame(dict_city,columns=['都','人口','土地'],
                  index=['Tpi','Ntc','Tao','Tcg','Tna','Kao']) 
df_city 

#練習2 解答
df_city['市長']=mayor  
df_city 

#練習3 解答     
df2_city=df_city.set_index('都')
df2_city

#練習4 解答
s_population=df2_city['人口']
s_area=df2_city['土地']
s_population
s_area

#練習5 解答
#%pylab
s_population.plot(kind='bar')
s_area.plot(kind='pie')



