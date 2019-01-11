# -*- coding: utf-8 -*-
"""
web_scraping_23_getEmail_20161201.py
Created on Thu Dec 01 13:43:36 2016

@author: zzjack
"""
#以 re.findall() 萃取email address
import requests, re
regex=r"([a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+)"
url='http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm'
html=requests.get(url).text

emails=re.findall(regex,html)

for email in emails:
    print(email)
