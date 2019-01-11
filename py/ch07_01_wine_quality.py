# -*- coding: utf-8 -*-
"""
ch07_01_wine_quality.py
Created on Tue Feb 21 14:47:59 2017

@author: zzjack
"""
import numpy as np
import pandas as pd
import seaborn as sns 
#Seaborn: statistical data visualization
#需先安裝 conda install seaborn
import matplotlib.pylab as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

#---------------------------------------------
#以pd.read_csv() 將csv讀入-->Dataframe
#分隔符號為 ',', 欄位標題在第一列(header=0)
wine=pd.read_csv('winequality-both.csv',sep=',',header=0)

#檢視 dataframe wine 的 column
wine.columns

#使用 StringMethod str.replace(), 將column的空白置換為'_'
wine.columns=wine.columns.str.replace(' ','_')

#再次檢視 column
wine.columns

#檢視前5筆資料
wine.head(5)

#檢視所有變數的描述性統計, describe()
wine.describe()

#檢視quality欄位
wine.quality #or wine['quality']

#找出quality不重複值,並排序 (SQL: select distinct quality from wine order by quality)
sorted(wine.quality.unique())

#計算quality值出現頻率
wine.quality.value_counts()

#===============================================
#分組、色階分布圖與t檢定
#0. 檢視DataFrame wine
wine

#1. 檢視DataFrame wine 'type'及'quality' column
wine[['type','quality']]

#2. pandas DataFrameGroupBy object, 按 'type' 欄位 group by
wine.groupby('type') 

#3. 將上述GroupBy作用在 'quality' 欄位以describe()作為聚合函數
wine.groupby('type')[['quality']].describe() 

#4. 將3. 的結果，依'type' unstack()
wine.groupby('type')[['quality']].describe().unstack('type')

#5. 將4. describe() 改為 quantile([0.25,0.75])
#   顯示特定品質0.25,0.75分位數
wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type')

#6. DataFrame.loc[] --> ch07_01a_wine_quality.py
#   依'type' 檢視 'quality'
red_wine=wine.loc[wine['type']=='red','quality']
white_wine=wine.loc[wine['type']=='white','quality']

sns.set_style("dark") #seaborn.set_stype() Set the aesthetic style of the plots.
sns.distplot(red_wine, norm_hist=True, kde=False,
             color="red",label="Red wine",axlabel="Quality Score")

sns.distplot(white_wine, norm_hist=True, kde=False,
             color="white",label="White wine",axlabel="Quality Score")
          



