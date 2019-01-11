# coding: utf-8
#Crawling an Entire Site
#web_scraping_13a_20160804.py
from urllib.request import urlopen #from urllib.request import urlopen
from bs4 import BeautifulSoup #from bs4 import BeautifulSoup
import re #import reqular expression

pages=set()                          #create a set name pages
def getLink(pageUrl):                #defined function getlink()
    global pages                     #宣告全域(global)變數 pages
    html=urlopen(pageUrl)
    bsObj=BeautifulSoup(html,'lxml')
    for link in bsObj.findAll("a",href=re.compile("^http")): #放寬條件,只要http開頭
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: #如果這個鏈結不在清單(set pages)中
                newPage=link.attrs['href'] 
                print(newPage)       #印出這個鏈結
                pages.add(newPage)   #將這個鏈結加到 set 中,記住
                getLink(newPage)     #以這個鏈結 recursive 呼叫 getLink
#主程式開始:
urlStr=input("請輸入一個首頁網址,(例如:http://www.iii.org.tw/):")
getLink(urlStr) #一開始以輸入網址呼叫 getLink() 



