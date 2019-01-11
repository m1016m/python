# -*- coding: utf-8 -*-
"""
05_panda_11_20170127.py
Created on Fri Jan 27 15:14:46 2017
pandas-datareader
pandas-datareader.readthedocs.io/en/latest/
@author: zzjack
"""
import pandas as pd
from pandas import DataFrame,Series
import numpy as np

#usage pandas-datareader
from pandas_datareader import data as web
import pandas_datareader as pdr

#Remote Data Access
#example 1: Yahoo! Finance
import datetime
start=datetime.datetime(2010,1,1)
end=datetime.datetime(2017,1,1)
f = web.DataReader("F", 'yahoo', start, end)
type(f) #pandas.core.frame.DataFrame
f.columns #檢視 DataFrame f 的column
f.index #index 為日期
#擷取2016年資料
f_2016=f.ix['2016-01-01':'2017-01-01'] 
f_2016.tail(10) #檢視最後10筆

#擷取交易量(Volume)為Series sv_2016
s_2016=f_2016['Volume']

#繪圖展示2016年 Volume
import matplotlib.pyplot as plt
#%pylab
s_2016.plot(kind='line')

#example 2: Google Finance, apple 股價
f2 = web.DataReader("AAPL", 'google', start, end)
f2_2016=f2.ix['2016-01-01':'2017-01-01']
f2_2016.head(10) #顯示前10筆

#繪圖展示2016年收盤價
f2_2016['Close'].plot(kind='bar')





