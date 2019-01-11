# -*- coding: utf-8 -*-
"""
#web_scraping_04c_20170912.py
#範例: 中油歷年油價(92,95,98)資料分析
@author: HP
"""
#中油油品歷史價格網頁
#http://new.cpc.com.tw/division/mb/oil-more4.aspx

#------------------------------------------------------------------
#step 1: 取得資料，從中油網站擷取中油歷年油價(92,95,98)資料
from urllib.request import urlopen
from bs4 import BeautifulSoup #從bs4 module, import BeautifulSoup

#設定變數url指向字串物件 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'
#url='http://new.cpc.com.tw/division/mb/oil-more4.aspx'
url='file:///E://worspace//python//py//20180108.html'
#叫用urlopen() function,回傳是一個HTTPResponse Object
html=urlopen(url) #html 變數,一個http.client.HTTPResponse

#------------------------------------------------------------------
#step 2: 初步資料處理, 將str Object 'html', 轉成BeautifulSoup物件
bsObj=BeautifulSoup(html,'lxml') #轉成 bs Object
print(bsObj.prettify()) #以prettify() method檢視bsf Obj

#找找看有沒有 <table> tag:     
tableData=bsObj.findAll('table')  
len(tableData)  #2,有兩個 

#於是我們改以pandas.read_html() 函數來讀取url中的 <table> tag
import pandas as pd #先將 pandas import 進來
import html5lib  #html5lib 需先安裝, conda install html5lib
import bs4 #import bs4

df1=pd.read_html(url) #df1 是一個 list of DataFrame
data=df1[0] #第一個DataFrame 就是我們要的油價表

#將DataFrame 寫至 'cpp_data_2018.csv'
data.to_csv('cpp_data_2018.csv')
#如果已經有檔案,就可以直接用pd.read_csv()讀入
#data=pd.read_csv('cpp_data_2018.csv')

#-----------------------------------------------------------------
#step 3: Data Wrangling (資料重整,裁剪)
#使用DataFrame / 布林陣列

#step 3a:我們關心的是92/95/98及高柴,所以先裁前5欄位(含日期)
data=data.iloc[:,0:5]  #先裁1~5欄位(含日期)
title=data.iloc[0,:] #擷取第一列的資料當抬頭
data=data.iloc[1:,:] #把第一列裁掉
data.columns=title #columns 改成 title

#step 3b: 92/95/98/高柴 是連動的,所以我們只要找 92 有值的日期即可
#使用布林陣列 --> pd.notnull(data["無鉛汽油92"])
data=data[pd.notnull(data["無鉛汽油92"])] #92有值
#用 DataFrame set_index() method 將"調價日期"欄轉成 index
data=data.set_index("調價日期")

#step 3c: 轉換資料型別
#目前data中每個值 datatype 皆為 str
#無法直接計算或繪圖
#需先將 str 轉成 float
#3c1.建立將字串轉成float的lambda函數
str_to_float=lambda x:float(x)

#3c2.以DataFrame 的applymap() method使用lambda str_to_float
data=data.applymap(str_to_float)
#因為data中有空白格 (1999/7前並無98汽油)
#所以我們須先做缺失值處理    
#缺失值處理,DataFrame 過濾
data=data[pd.notnull(data["無鉛汽油98"])]
#檢視 data, "無鉛汽油98" 空白的row 已刪除
data.tail(10)

#2.以DataFrame 的applymap() method使用lambda str_to_float
data=data.applymap(str_to_float) #這次可以了
#---------------------------------------------------------------------------
#step 4b: 進階資料處理，轉換與視覺化展示(繪圖)
#繪圖
import matplotlib.pyplot as plt
#%pylab
data.plot()








