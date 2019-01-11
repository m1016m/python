# -*- coding: utf-8 -*-
"""
05_panda_11_fixed.py
pandas-datareader
pandas-datareader.readthedocs.io/en/latest/
@author: zzjack
"""
#usage pandas-datareader
from pandas_datareader import data as web

#Remote Data Access
#example 1: google Finance
import datetime
start=datetime.datetime(2017,1,1)
end=datetime.datetime(2017,6,30)
f = web.DataReader("F", 'google', start, end)
type(f) #pandas.core.frame.DataFrame
f.columns #檢視 DataFrame f 的column
f.index #index 為日期
#擷取2017年6月資料
f_201706=f.loc['2017-06-01':'2017-06-30'] 
f_201706.tail(10) #檢視最後10筆

#擷取交易量(Volume)為Series sv_201706
sv_201706=f_201706['Volume']

#繪圖展示2017年6月 Volume
#%pylab
sv_201706.plot(kind='line')

#example 2: Google Finance, apple 股價
f2 = web.DataReader("AAPL", 'google', start, end)
f2_201706=f2.loc['2017-06-01':'2017-06-30']
f2_201706.head(10) #顯示前10筆

#繪圖展示2017年6月收盤價
f2_201706['Close'].plot(kind='bar')





