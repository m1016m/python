# -*- coding: utf-8 -*-
"""
05_panda_02b_20170813.py
Created on Sun Aug 13 20:00:42 2017
@author: zzjack
"""
from pandas import DataFrame,Series #import DataFrame(), Series()
from pandas_datareader import data as web  #pandas Remote Data Access
        #http://pandas.pydata.org/pandas-docs/stable/remote_data.html
        #conda install pandas-datareader

#step 1: 資料取得 (Interacting with the outside world)
all_data={} #create a new dict object and named it all_data
for ticker in ['AAPL','IBM','MSFT','GOOG']: 
    all_data[ticker]=web.get_data_google(ticker,start='2010-01-01', end='2017-06-30')
#以 for指令 對 list['AAPL','IBM','MSFT','GOOG'] 做迭代(iterating)
#迭代工作為叫用 pandas_datareader.data module 的 get_data_google() API
#到 google 依指定日期取得交易股價資料,並將此資料(DatFrame Object)
#構成字典(dict) all_data (dict of Dataframe)

all_data #dict of DataFrame, key:value (value 資料型別為 DataFrame)

appleDf=all_data['AAPL'] #DataFrame appleDf

appleDf.to_csv('apple2017.csv') #將DataFrame 'appleDf' 轉成csv檔案 'apple2017.csv' 


