# -*- coding: utf-8 -*-
"""
05_panda_02b_20170126.py
The column returned when indexing a DataFrame is a view on the 
underlying data, not a copy. Thus, any in-place modifications to
the Series will be reflected in the DataFrame.
The column can be explicitly copied using the Series’s copy method.
Created on Thu Jan 26 22:09:37 2017

@author: HP
"""
import pandas as pd
from pandas import DataFrame,Series
import numpy as np

dict_city={'都':['臺北','新北','桃園','臺中','臺南','高雄'],
           '人口':[2695704,3979208,2147763,2767239,1886033,2779371],
           '土地':[271,2052,1220,2214,2191,2952]}
df=DataFrame(dict_city)
df

s1=df.ix[1]

