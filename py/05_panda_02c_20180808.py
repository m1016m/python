# -*- coding: utf-8 -*-
"""
05_panda_02c_20180808.py
Created on Sun Aug 13 20:21:00 2017
@author: zzjack
"""
import pandas as pd
appleDf=pd.read_csv('apple2017.csv') #以pandas.read_csv()讀取
appleDf=appleDf.set_index('Date')    #set index
s_Close=appleDf['Close']
type(s_Close)
s_Close

s_Volume_2016=appleDf['Volume']['2016-01-01':'2016-12-31']
type(s_Volume_2016)
s_Volume_2016
