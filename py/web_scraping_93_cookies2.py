# -*- coding: utf-8 -*-
"""
web_scraping_93_cookies2.py
@author: III
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen('http://www.myav.com.tw/')
bsObj=BeautifulSoup(html,"lxml")

#找出有屬性 'name':'password' 的form
form_list=bsObj.findAll('form') #先找出所有的 form
#找出form_list 中有屬性 'name':'password' 的form  
for fm in form_list:
    if fm.find(attrs={'name':'password'}):
        print(fm)
#-------------------------------------------------------
import requests
params={'username':'zzjack','password':'xxxxxxx'}
#將params POST 給 index.php
r = requests.post("http://www.myav.com.tw/index.php"
                  , data=params)

r.cookies #檢視 cookies
print(r.cookies.get_dict()) #叫用 get_dict() method
#------------------------------------------------------
#使用cookies 到./bbs/member.php
r = requests.get("http://www.myav.com.tw/",
                 cookies=r.cookies)
print(r.text)
