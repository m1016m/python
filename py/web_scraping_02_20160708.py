# -*- coding: utf-8 -*-
"""
web_scraping_02_20160708.py ,BeautifulSoup
Created on Thu Jun  8 14:40:23 2017

@author: III
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup #from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page1.html")

bsObj=BeautifulSoup(html.read(),"lxml") #叫用BeautifulSoup() 將html.read() 
                                        #轉成 bs4.BeautifulSoup object
#bsObj? #是一個 BeautifulSoup object
print(bsObj.h1)
bsObj
print(bsObj.prettify()) #叫用 prettify() method
print(bsObj.html.body.h1) #完整的描述
print(bsObj.body.h1) #這樣也可以
print(bsObj.h1) #這樣就可以了
#---------------------------------------------------------------
#練習1: 資策會南區網址"http://www.iiiedu.org.tw/south/"
html_iii=urlopen("http://www.iiiedu.org.tw/south/")
iii_bsObj=BeautifulSoup(html_iii.read().decode(),"lxml") #記得 decode()

print(iii_bsObj.prettify())
print(iii_bsObj.title.prettify())
print(iii_bsObj.body.prettify())
print(iii_bsObj.body.img)


                                       
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
