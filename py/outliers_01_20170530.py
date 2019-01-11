# -*- coding: utf-8 -*-
"""
outliers_01_20170530.py, 異常值 說明
Created on Tue May 30 09:31:48 2017

@author: zzjack
"""
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#series s1
list01=[0.1,0.15,0.2,0.25,0.35,0.4,0.45,0.5,5]
s1=Series(list01)

#使用quantile() method, 並指定 q=0.99 (99% 分位數)
s1.quantile(.99) #4.64

#使用布林陣列,移除 99%分位數外的值 (異常值)
s2=s1[s1 < s1.quantile(.99)]

#檢視 s2
s2 #




