# -*- coding: utf-8 -*-
"""
web_scraping_10_crawl_20160718.py
Created on Tue Jun 13 15:06:48 2017
@author: III
"""
#a script that retrieves an arbitrary
#Wikipedia page and produces a list of links on that page:
from urllib.request import urlopen
from bs4 import BeautifulSoup
#以Wikipedia 中 Kevin_Bacon page 為例: 
html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")  #Kevin_Bacon
html2=urlopen("http://en.wikipedia.org/wiki/Wu_Nien-jen") #吳念真
bsObj=BeautifulSoup(html,"lxml") #轉成bs Object
        
for l in bsObj.findAll("a"):    #找出所有tag <a>
    if 'href' in l.attrs:       #檢查 <a> 有無 attribute 'href'
        print(l.attrs['href'])  #如果有就把 屬性 'href' 的值印出

#練習: 將上例以 list comprehension 改寫
link_list=[l.attrs['href'] for l in bsObj.findAll("a") if 'href' in l.attrs] 
for ln in link_list:
    print(ln)
#--------------------------------------------------------------       
#這些link中有些我們並不感興趣,如 /wiki/Wikipedia:Protection_policy
#wikipedia 上 article page 皆有三個共通點:
# 1. They reside within the div with the id set to bodyContent
# 2. The URLs do not contain semicolons
# 3. The URLs begin with /wiki/
# 2.3.-->　regular expression --> "^(/wiki/)((?!:).)*$"　
#改寫, 用 regular expression "^(/wiki/)((?!:).)*$"
import re
html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")  #Kevin_Bacon
bsObj=BeautifulSoup(html,"lxml") #轉一個 bs4 object bsObj
for l in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in l.attrs:
        print(l.attrs['href'])
        
#以上會傳回 "Kevin Bacom"這篇Wikipedia 文章中，所有連結到其他文章的URL     






