# -*- coding: utf-8 -*-
"""
#web_scraping_28a_20170514.py
Created on Sat Jan 21 23:01:02 2017
#範例: 中油歷年油價(92,95,98)資料分析
@author: HP
"""
#中油油品歷史價格網頁
#http://new.cpc.com.tw/division/mb/oil-more4.aspx

#------------------------------------------------------------------
#step 1: 取得資料，從中油網站擷取中油歷年油價(92,95,98)資料
import requests #import requests module,用以擷取網頁資料 
#查詢 requests 說明及使用方法 requests?

#設定變數url指向字串物件 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'
url='http://new.cpc.com.tw/division/mb/oil-more4.aspx'

#叫用request.get() function,回傳是一個Response Object
html=requests.get(url).text #html 變數指向 Response的text屬性值 (str)

#------------------------------------------------------------------
#step 2: 初步資料處理, 將str Object 'html', 轉成BeautifulSoup物件
from bs4 import BeautifulSoup #從bs4 module, import BeautifulSoup
bsObj=BeautifulSoup(html,'html.parser') #轉成 bs Object
print(bsObj.prettify()) #以prettify() method檢視bsf Obj

#從bsObj(一個tree Obj) 中,以find_all() method
#find all <span> tag ,id=Showed
#find_all(),回傳的是一個 list (list of tag)
data=bsObj.find_all('span',{'id':'Showtd'}) 

#從data (list)中第一個元素(<span> tag)中
#以find_all() method 找出所有 <tr> tag
#回傳的仍是一個 list (list of <tr> tag)
rows=data[0].find_all('tr')

#-----------------------------------------------------------------
#step 3: Data Wrangling (資料重整,裁剪)
prices=list() #create empty list prices
for row in rows:        #逐一處理每一 <tr>...</tr>
    cols=row.find_all('td')
    if len(cols[1].text) > 0:   #這個範例只處理92,95,98 (cols[1],cols[2],cols[3]),
        item=[cols[0].text, cols[1].text, cols[2].text, cols[3].text]
        prices.append(item)    #將item加入list price
                               #所以只要cols[1] (92汽油)資料不是空的，就被認定有異動 

prices #檢視 list prices (list of lists)

#---------------------------------------------------------------------------
#step 4a: 展示成果 --> 單純列印
for p in prices: #以 for 疊代處理可疊代物件 prices
    print(p)
    
#---------------------------------------------------------------------------
#step 4b: 進階資料處理，轉換與視覺化展示(繪圖)
import pandas as pd #import pandas module
from pandas import DataFrame,Series

#將list 轉為DataFrame df1
df1=DataFrame(prices,columns=['date','92','95','98'])

#用 DataFrame set_index() method 將日期欄轉成 index
df2=df1.set_index('date')
df2 #檢視 df2

#目前df2中每個值 datatype 皆為 str
#無法直接計算或繪圖
#需先將 str 轉成 float

#1.建立將字串轉成float的lambda函數
str_to_float=lambda x:float(x)

#2.以DataFrame 的applymap() method使用lambda str_to_float
df3=df2.applymap(str_to_float)
#因為df2中有空白格 (1999/7前並無98汽油)
#我們須先做缺失值處理

#--------------------------------------------------------
#缺失值處理,DataFrame 過濾
df2=df2[df2['98']!='']

#檢視 df2, '98' 空白的row 已刪除
df2.tail(10)

#2.以DataFrame 的applymap() method使用lambda str_to_float
df3=df2.applymap(str_to_float) #這次可以了
df3 #檢視

#-----------------------------------------------------------
#繪圖
import matplotlib.pyplot as plt
#%pylab
df3.plot()

#----------------------------------------------------------
#將DataFrame df3 以dataframe.to_csv() method 後續使用
#寫至 'df3.csv' csv檔，
df3.to_csv('df3.csv')






