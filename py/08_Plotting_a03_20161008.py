# -*- coding: utf-8 -*-
"""
08_Plotting_a03_20161008.py

@author: zzjack
"""
#Plotting and Visualization
#Plotting Maps: Visualizing Haiti Earthquake Crisis Data

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
#%pylab 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#讀取資料
data=pd.read_csv('D:\workspace\python\data\Haiti.csv')

#檢視資料
data
data.columns
data.index

#Each row represents a report sent from someone’s mobile phone indicating
#an emergency or some other problem. Each has an associated timestamp and 
#a location as latitude and longitude:
data[['INCIDENT DATE', 'LATITUDE', 'LONGITUDE']][:10]  

#The CATEGORY field contains a comma-separated list of codes indicating 
#the type of message: 
data['CATEGORY'][:6]
    
# 缺失資料處理:
# 1.some of the categories are missing, so we
#   might want to drop these data points.
# 2.calling describe shows that there
#   are some aberrant locations:
data.describe()

# 缺失資料處理:
# Cleaning the bad locations and removing the missing categories    
# 從data.describe() 判讀合理的經緯度, 並將CATEGORY 為NULL的資料排除
data=data[(data.LATITUDE > 18) & (data.LATITUDE < 20)
          & (data.LONGITUDE > -75) & (data.LONGITUDE < -72)
          & data.CATEGORY.notnull()]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# wrangling data, 字串處理
# function to_cat_list(),
# 將字串以split() method 分隔成字串list後
# 以strip() method 將前後空白刪掉
def to_cat_list(catstr):
    stripped=(x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]

#The method strip() returns a copy of the string in which all 
#chars have been stripped from the beginning and the end of 
#the string (default whitespace characters).

# function get_all_categories(cat_series),
# 以set()函數將to_cat_list(x)處理過的list轉成set (cat_sets)
# 再將cat_sets, union後,排序
def get_all_categories(cat_series):
    cat_sets=(set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
    
# function get_english(cat)
def get_english(cat):
    code, names = cat.split('.')
    if '|' in names:
        names=names.split('|')[1] #如果names中有'|',取後者
    return code,names.strip()
    
# 測試get_english()
get_english('2. Urgences logistiques | Vital Lines')
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#make a dict mapping code to name:
all_cats=get_all_categories(data.CATEGORY)  

all_cats #檢視重整過的 data.CATEGORY

# Generator expression 
english_mapping=dict(get_english(x) for x in all_cats)

english_mapping #檢視dict english_mapping
english_mapping['2a']
english_mapping['6c']
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#first extract the unique category codes and construct a 
#DataFrame of zeros having those as its columns and the same 
#index as data:

#定義函數get_code()    
def get_code(seq):
    return [x.split('.')[0] for x in seq if x]

#以函數get_code()取出code list --> all_code             
all_codes=get_code(all_cats)    

#檢視 list all_code (code list)
all_codes

#將all_codes以pd.Index()轉成Index Object, code_index
code_index=pd.Index(np.unique(all_codes))
type(code_index)
code_index #檢視Index Object, code_index

#construct a DataFrame of zeros having those as its 
#columns and the same index as data:
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))),
index=data.index, columns=code_index)

#檢視dummy_frame
dummy_frame.ix[:,:6]
dummy_frame.ix[:6,:6]
dummy_frame
dummy_frame.columns
dummy_frame.index

#set the appropriate entries of each row to 1:
for row, cat in zip(data.index, data.CATEGORY):
    codes=get_code(to_cat_list(cat))
    dummy_frame.ix[row, codes]=1

dummy_frame.ix[:,:6] #檢視新的dummy_frame

#lastly joining this with data:
data=data.join(dummy_frame.add_prefix('category_'))

#檢視重構的data
data.ix[:,:5]
data.ix[:,10:15]

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#資料重塑完成,準備開始繪圖
#因為是經緯度資料(data[['LATITUDE','LONGITUDE']]),
#我們使用basemap toolkit:
from mpl_toolkits.basemap import Basemap

def basic_haiti_map(ax=None,lllat=17.25,urlat=20.25,
lllon=-75, urlon=-71):
    m = Basemap(ax=ax, projection='stere',
        lon_0=(urlon + lllon) / 2,
        lat_0=(urlat + lllat) / 2,
        llcrnrlat=lllat, urcrnrlat=urlat,
        llcrnrlon=lllon, urcrnrlon=urlon,
        resolution='f')
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    return m
    
#
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

fig.subplots_adjust(hspace=0.05, wspace=0.05)

to_plot = ['2a', '1', '3c', '7a']

lllat=17.25; urlat=20.25; lllon=-75; urlon=-71

for code, ax in zip(to_plot, axes.flat):
    m = basic_haiti_map(ax, lllat=lllat, urlat=urlat,
        lllon=lllon, urlon=urlon)
    cat_data = data[data['category_%s' % code] == 1]
    # compute map proj coordinates.
    x, y = m(cat_data.LONGITUDE, cat_data.LATITUDE)
    m.plot(x, y, 'k.', alpha=0.5)
    ax.set_title('%s: %s' % (code, english_mapping[code]))


   




            
            
            
            
            
            
            
            
            
            
            
            
            




