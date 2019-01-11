# -*- coding: utf-8 -*-
"""
Example3_USDA.py
Created on Wed Oct 19 13:48:19 2016

@author: zzjack
"""
from pandas import Series, DataFrame #import Series,DataFrame
import pandas as pd #慣例
import numpy as np #import numpy as np
import matplotlib.pyplot as plt
import json #import json module
#%pylab

#讀取資料 json.load(),USDA Food Database
db=json.load(open('foods-2011-10-03.txt'))

#檢視資料 db 
type(db) #db is a list
type(db[0]) #db is a list of dict
db[0] #Each entry in db is a dict containing all the data for a single food.
db[0].keys() #看看dict. 的 key --> keys() method
len(db) #6636 個 items

#Each entry in db is a dict containing all the data for a single food.
#nutrients(營養素),The 'nutrients' field
#is a list of dicts, one for each nutrient:
db[0]['nutrients'][0] #1 of 162  
db[0]['nutrients'][1] #2 of 162

#將db中的第一個項目db[0]的'nutrients' key,-->
#db[0]['nutrients'] (list of dict, 162個entry)
#以DataFrame() 轉成DataFrame Object, nutrients
nutrients=DataFrame(db[0]['nutrients'])
type(nutrients) #pandas.core.frame.DataFrame 
nutrients[:7] #檢視DataFrame nutrients 前7列

#++++++++++++++++++++++++++++++++++++++++++++++
#重新檢視 db, db 是一個list of dict,
#使用DataFrame(list_of_dict,colmns=cols)

#step 01:定義一個list: info_keys
info_keys=['description','group','id','manufacturer']

#step 02:使用DataFrame(db,info_keys), db中每個元素的nutrients不要
#        只擷取 ['description','group','id','manufacturer']
info=DataFrame(db,columns=info_keys) 

#檢視DataFrame info 前5列
info[:5]

#檢視整個 DataFrame info
info #[6636 rows x 4 columns]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#pandas.vaule_counts(Series Object) 函數 or
#Series_Object.vaule_counts() method 
#統計Series Object 出現次數
#以pd.vaule_counts()統計食物類別(group)的分布情形:
pd.value_counts(info['group']) #or info.group
#or
info.group.value_counts() #or info['group']

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#再回頭看db元素中的'nutrients',我們想將每個食物的營養素整合
#到一個大表中,分成幾個步驟完成:

#step 1. 建一個空串列 nutrients
nutrients=[]

#step 2. 
for rec in db:        #對db中每個元素做迭代, (db--> list of dict),每次迭代的對象皆為dict
    fnuts=DataFrame(rec['nutrients']) #回顧程式碼34行
    fnuts['id']=rec['id'] #新增一個column 'id' 到DataFrame fnuts,值是擷取該元素的'id'欄位
    nutrients.append(fnuts) #把這個帶'id'的DataFrame加到list nutrients

#step 3. 檢視目前的 nutrients list, (list of DataFrame, 6636個元素)
len(nutrients)
type(nutrients[0])

#step 4. 以pandas.concat() 將nutrients list 中的6636個DataFrame 合併成一個DataFrame
nutrients=pd.concat(nutrients,ignore_index=True)

#step 5. 檢視加工完成的DataFrame nutrients
nutrients.head(10) #檢視前10列
nutrients #[389355 rows x 5 columns]

#+++++++++++++++++++++++++++++++++++++++++++++++++++
#使用DataFrame.duplicated() 檢查重複項,並以sum() 加總True項
nutrients.duplicated().sum() #14179個重複項

#以DataFrame.drop_duplicate(), drop duplicate item
nutrients=nutrients.drop_duplicates()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#現在,我們有兩個 DataFrame: info, nutrients
#檢視兩個DataFrame的columns
info.columns
nutrients.columns
#兩者皆有'description','group' 欄位,為了明確分辨
#我們對它們進行重命名: DataFrame.rename()
col_mapping={'description':'food',
             'group':'fgroup'}

info=info.rename(columns=col_mapping,copy=False)

col_mapping={'description':'nutrient',
             'group':'nutgroup'}

nutrients=nutrients.rename(columns=col_mapping,copy=False)

#再次檢視
info.columns
nutrients.columns

#最後, 以pandas.merge() 將info,nutrients 兩個DataFrame合併
ndata=pd.merge(nutrients,info, on='id',how='outer')

#檢視 DataFrame ndata
ndata
ndata.head(10)
ndata.ix[3000] #第3001列

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++中途站++++,我們把辛苦得來的DataFrame ndata 存檔
#pandas.DataFrame.to_json() method, Convert the object to a JSON string.
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html
ndata.to_json('ndata2016.json')

#檢視 'ndata2016.json' 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++終於,我們有了漂亮完美的資料格式,可以開始 "資料分析"了!
#pandas.read_json() 讀資料
perfect_data=pd.read_json('ndata2016.json') 

#檢視DataFrame perfect_data 前5列
perfect_data.head(5)

#example 1: groupby and quantile()
ex1_result=perfect_data.groupby(['nutrient','fgroup'])['value'].quantile(0.5)
ex1_result['Zinc, Zn'].order().plot(kind='barh')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#example 2: groupby 分組 and 聚合函數 (mean,max,min,count)
#step 0: 檢視部分欄位的前5列
perfect_data[['fgroup','food',
             'nutgroup','nutrient','value']][0:5]  

#step 1: groupby ['nutgroup','nutrient'], 聚合對象欄位 'value',
#        聚合函數 mean()
ex2=perfect_data.groupby(['nutgroup','nutrient'])['value'].mean()
ex2.plot(kind='bar') #畫圖看看












  