# -*- coding: utf-8 -*-
"""
web_scraping_95_session2.py
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
sess01=requests.Session() #建一個session object sess01
params={'username':'zzjack','password':'xxxxxxx'}
#使用session.post() 
s=sess01.post("http://www.myav.com.tw/index.php", params)

s.cookies #檢視 cookies, session 會保持 cookies 資訊
print(s.cookies.get_dict()) #叫用 get_dict() method
#------------------------------------------------------
#使用session.get() 到http://www.myav.com.tw/, 不用附cookies
s = sess01.get("http://www.myav.com.tw/")
print(s.text)

#session object, 會追蹤session資訊，像是cookies、headers
