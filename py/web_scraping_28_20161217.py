# -*- coding: utf-8 -*-
"""
web_scraping_28_20161217.py
Created on Sun Dec 18 11:47:30 2016
@author: jack huang
"""
#進階分析網頁內容
from bs4 import BeautifulSoup
import requests
url='http://new.cpc.com.tw/division/mb/oil-more4.aspx' #中油油品歷史價格

html=requests.get(url).text
bsObj=BeautifulSoup(html,'html.parser') #以 'html.parser' 轉成 bs Object
data=bsObj.find_all('span',{'id':'Showtd'}) #find all <span> tag ,id=Showed
rows=data[0].find_all('tr')

prices=list() #create empty list prices
for row in rows:        #逐一處理每一 <tr>...</tr>
    cols=row.find_all('td')
    if len(cols[1].text) > 0:   #這個範例只處理92,95,98 (cols[1],cols[2],cols[3])
        item=[cols[0].text, cols[1].text, cols[2].text, cols[3].text]
        prices.append(item)    #將item加入list price
for p in prices:
    print(p)

#所以只要cols[1] (92汽油)資料不是空的，就被認定有異動    
