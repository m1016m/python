# -*- coding: utf-8 -*-
"""
web_scraping_10a_crawl_20160718.py
Created on Tue Jun 13 15:06:48 2017
@author: III
"""
#a script that retrieves an arbitrary
#Wikipedia page and produces a list of links on that page:
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#以Wikipedia 中 Wu_Nien-jen (吳念真) page 為例: 
html=urlopen("http://en.wikipedia.org/wiki/Wu_Nien-jen") #吳念真

bsObj=BeautifulSoup(html,"lxml") #轉一個 bs4 object bsObj
for l in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in l.attrs:
        print(l.attrs['href'])
        
#以上會傳回 "Wu_Nien-jen (吳念真)"這篇Wikipedia 文章中，所有連結到其他文章的URL 
     






