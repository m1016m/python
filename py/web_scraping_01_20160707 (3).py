# -*- coding: utf-8 -*-
"""
web_scraping_01_20160707.py
Created on Thu Oct 13 14:52:36 2016

@author: zzjack
"""
from urllib.request import urlopen #for python 3.x, if python 2.7 urllib2

html=urlopen("http://pythonscraping.com/pages/page1.html")

#type(html) #檢視變數html的物件類別, http.client.HTTPResponse

print(html.read()) #以read() method 讀取, b'--> byte string 說明

#urllib: std. library in python 
#https://docs.python.org/3/library/urllib.html#module-urllib
#urllib is a package that collects several modules for working with URLs

#urllib.request module / urlopen() function
