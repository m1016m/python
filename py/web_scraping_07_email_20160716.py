# coding: utf-8
#web_scraping_07_email_20160716

# 資策會 "http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm"
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re

html=urlopen("http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm")
bsObj=BeautifulSoup(html,"lxml") #轉成 BeautifulSoup Object
print(bsObj.prettify())
list_a=bsObj.findAll("a") #找出所有的 tag <a>

for la in list_a: #所有 tag <a> 的內容 get_text() 
    print(la.get_text())

#regular string " [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net) "

for la in list_a:
    if re.search("[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)",la.get_text()):
        print(la.get_text())

#上例,以串列生成式改寫:

mail_list=[la.get_text() for la in list_a if 
re.search("[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)",la.get_text())]

for m in mail_list:
    print(m)



