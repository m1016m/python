# coding: utf-8
#web_scraping_03_20160708.py
#Connecting Reliably
from urllib.request import urlopen
#from urllib.error module import HTTPError object
from urllib.error import HTTPError 
from bs4 import BeautifulSoup

def getTitle(url): #defined function getTitle()
    try:                   #第一段 try...except
        html=urlopen(url)
    except HTTPError as e: #如果是 404,500 等錯誤
        return None        #return None
    try:                   #第二段 try...except
        bsObj=BeautifulSoup(html.read(),"lxml")
        title=bsObj.body.h1
    except AttributeError as e:  #如果我們要找的tag不存在 
        return None              #回傳 None
    return title           #如果找得到,傳回

title=getTitle("http://www.pythonscraping.com/pages/page1.html")

if title==None: #有例外發生
    print("Title could not be found")
else:
    print(title)

#練習1:資策會南區網址,"http://www.iiiedu.org.tw/south/"

def iii_getTitle(url): #重新定義一個函數 iii_getTitle()
    try: #第一段 try
        html=urlopen(url)
    except HTTPError as e: #第一段 exception
        return None
    try: #第二段 try
        bsObj=BeautifulSoup(html.read().decode())
        title=bsObj.body.h1
    except AttributeError as e: #第二段 exception
        return None
    return title

title=iii_getTitle("http://www.iiiedu.org.tw/south/")
if title == None:
    print("Title could not be found")
else:
    print(title)

#看看資策會南區網頁內容
iii_html=urlopen("http://www.iiiedu.org.tw/south/")
iii_bsObj=BeautifulSoup(iii_html.read().decode(),'lxml')
print(iii_bsObj.prettify())
print(iii_bsObj.body.h1) #html 中沒有tag h1



