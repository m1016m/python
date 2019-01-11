# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:09:54 2018
behindScenes01.py
@author: zzjack
"""
#原始download file "iris.data"
#https://archive.ics.uci.edu/ml/datasets/iris
#!dir iris.data

#1. "iris_withTitle.csv" 製作過程
import pandas as pd
#準備 title list
title=['sepal_length','sepal_width','petal_length','petal_width','class']
#以pd.read_csv() 讀取 'iris.data', 以參數names=title 指定 column name
df1=pd.read_csv('iris.data',names=title)
#以pd.to_csv()將DataFrame 'df1' 寫至 file 'iris_withTitle.csv'
#注意! index不要 (index=None)
df1.to_csv('iris_withTitle.csv',index=None)
#!type iris_withTitle.csv

#2. "iris_noTitle.csv" 製作過程
#以pd.read_csv() 讀取 'iris.data', 
#參數 header=None --> 不要將第一行當欄位
df2=pd.read_csv('iris.data',header=None)
#以pd.to_csv() 將df2存成 file 'iris_noTitle.csv'
#index=None, header=None --> index及header都不要
df2.to_csv('iris_noTitle.csv',index=None,header=None)
#!type iris_noTitle.csv

#3. "iris_newId.csv" 製作過程
import numpy as np
df3=pd.read_csv('iris_withTitle.csv')
df3['newid']=np.arange(1000,1150)
df3.head(5)
df3.to_csv('iris_newId.csv',index=None,header=None)



