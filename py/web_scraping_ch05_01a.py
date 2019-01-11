# -*- coding: utf-8 -*-
"""
web_scraping_ch05_01a.py
"""
#In Python 3.x, urllib.request.urlretrieve can be used to download files 
#from any remote URL:
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#"http://www.tse.com.tw/zh/page/trading/exchange/BFT41U.html"
html=urlopen("http://data.kcg.gov.tw/dataset")
bsObj=BeautifulSoup(html,'lxml')
bsObj.findAll("form")
#重點在這裡:

    
urlretrieve(target_url,"csv_od2.csv")
    
    
imageLocation=bsObj.find("a",{"id":"logo"}).find("img")["src"]
imageLocation #display imageLocation 
              #'http://www.pythonscraping.com/sites/default/files/lrg_0.jpg'
             
#以urlretrive() function, 將URL imageLocation抓取到現行目錄,並存為 'logo.jpg' 檔名
urlretrieve(imageLocation,"logo.jpg")