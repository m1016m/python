# -*- coding: utf-8 -*-
"""
web_scraping_ch05_01.py
Created on Tue Nov  8 15:54:14 2016

@author: zzjack
"""
#In Python 3.x, urllib.request.urlretrieve can be used to download files 
#from any remote URL:
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

#"http://www.pythonscraping.com"
html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html,'lxml')
imageLocation=bsObj.find("a",{"id":"logo"}).find("img")["src"]
imageLocation #display imageLocation 
              #'http://www.pythonscraping.com/sites/default/files/lrg_0.jpg'
             
#以urlretrive() function, 將URL imageLocation抓取到現行目錄,並存為 'logo.jpg' 檔名
urlretrieve(imageLocation,"logo.jpg")