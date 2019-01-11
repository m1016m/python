# -*- coding: utf-8 -*-
"""
05_panda_90_2018.py
Dataframe Selection
Created on Mon Mar 12 13:53:44 2018
@author: zzjack
"""
#以 UCI adult.data dataset 為例
#https://archive.ics.uci.edu/ml/datasets/adult

#step 1: 讀取 adult.data,以 pandas.read_csv()
import pandas as pd

#step 1.1 建立adult dataset 欄位名稱 list, a_list
a_list=['age','workclass','fnlwgt','education','education-num',
        'marital-status','occupation','relationship','race','gender',
        'capital-gain','capital-loss','hours-per-week','native-country','income']
        
#step 1.2 以pandas.read_csv()讀取adult.data, 成為DataFrame df1  
df1=pd.read_csv("adult.data",header=None,names=a_list)

#step 1.3 檢視 Dataframe df1 前5筆資料
df1.head(5)

#===========================================================
#1. getting 
#Selecting a single column, which yields a Series, equivalent to df1.age
df1['age'] #df1.age
