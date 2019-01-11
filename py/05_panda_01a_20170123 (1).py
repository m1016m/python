# -*- coding: utf-8 -*-
"""
05_panda_01a_20170123.py
中場練習:篩選95油價低於20元的調整日期
Created on Mon Jan 23 16:20:31 2017
@author: zzjack
"""
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------------
#讀取資料
#以pd.read_csv() 讀取 df3.csv
df3=pd.read_csv('df3.csv')
df3 #檢視DataFrame df3

#--------------------------------------------------
#用 DataFrame set_index() method 將日期欄轉成 index
df4=df3.set_index('date')
df4 #檢視 DataFrame df4

#--------------------------------------------------
#從 DataFrame df4 擷取 95 欄位成一個 Series Object s95
s95=df4['95']
s95 #檢視s95














#解答:
s95[s95 < 20.0]
