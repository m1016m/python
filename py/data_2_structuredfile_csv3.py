# -*- coding: utf-8 -*-
"""
#data_2_structuredfile_csv3.py
#範例: 中油歷年油價 csv
"""
#中油油品歷史價格網頁
#http://new.cpc.com.tw/division/mb/oil-more4.aspx

#------------------------------------------------------------------
#step 1: 取得資料，從中油網站擷取中油歷年油價(92,95,98)資料
from urllib.request import urlopen
from bs4 import BeautifulSoup #從bs4 module, import BeautifulSoup

#設定變數url指向字串物件 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'
url='http://new.cpc.com.tw/division/mb/oil-more4.aspx'

#叫用urlopen() function,回傳是一個HTTPResponse Object
html=urlopen(url) #html 變數,一個http.client.HTTPResponse

#------------------------------------------------------------------
#step 2: 初步資料處理, 將str Object 'html', 轉成BeautifulSoup物件
bsObj=BeautifulSoup(html,'lxml') #轉成 bs Object

#找找看有沒有 <table> tag:     
tableData=bsObj.findAll('table')  
len(tableData)  #2,有兩個 

#於是我們改以pandas.read_html() 函數來讀取url中的 <table> tag
import pandas as pd #先將 pandas import 進來
import html5lib  #html5lib 需先安裝, conda install html5lib

df1=pd.read_html(url) #df1 是一個 list of DataFrame
data=df1[0] #第一個DataFrame 就是我們要的油價表

#----------------------------------------------------------
#將DataFrame data 以dataframe.to_csv() method 
#寫至 'price_2017.csv' csv檔，後續使用
data.to_csv('price_2017.csv')






