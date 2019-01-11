# -*- coding: utf-8 -*-
"""
web_scraping_22_getWebPage_20161201.py
Created on Thu Dec 01 11:49:56 2016

@author: zzjack
"""
#Python requests module
import requests
url='http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm'
#以splitlines() 切割成一行一行字串
html=requests.get(url).text.splitlines()

#列印前15行
for i in range(0,15):
    print(html[i])