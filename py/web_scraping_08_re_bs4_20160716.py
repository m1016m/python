# -*- coding: utf-8 -*-
"""
web_scraping_08_re_bs4_20160716.py
Created on Sun Jun 11 14:43:06 2017
@author: zzjack
"""
#example page: "http://www.pythonscraping.com/pages/page3.html"
#there are many product images on the site, they take the following form:
#<img src="../img/gifts/img3.jpg">

#example 1: grab URLs to all of the product images
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,"lxml")

#找出所有 tag <img> 
img_list=bsObj.findAll("img")  
img_list #list 中的 img 包含logo,但我們不要

img_list=bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

for img in img_list:
    print(img["src"]) #img["src"] --> img tag, src attr.
    
#---------------------------------------------------------------
#練習:將上例,以串列生成式改寫:
img_list=bsObj.findAll("img")

i_list=[i["src"] for i in img_list if 
 re.search("\.\.\/img\/gifts\/img.*\.jpg",i["src"])]

for i in i_list:
    print(i)




