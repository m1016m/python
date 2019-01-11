# -*- coding: utf-8 -*-
"""
web_scraping_22a_getWebPage_20161221.py
Created on Thu Dec 21 16:06:56 2016

@author: zzjack
"""
#Python requests module
import requests
url='http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm'
#以splitlines() 切割成一行一行字串
html=requests.get(url).text.splitlines()

#列印前15行
for i in range(0,15):
    #content=bytes(html[i],'utf-8')   
    content=html[i].encode('utf-8').decode()
    print(content)