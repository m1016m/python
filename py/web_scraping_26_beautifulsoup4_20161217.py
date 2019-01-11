# -*- coding: utf-8 -*-
"""
web_scraping_26_beautifulsoup4_20161217.py
Created on Sat Dec 17 11:13:23 2016

@author: HP
"""
#擷取網頁圖形檔鏈結
from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urlparse #urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)

#檢查當執行本 script 時,如果未代一<<url>>當參數,提醒並終止程式
if len(sys.argv) < 2:  #len(sys.argv) < 2 -->就是不帶參數
    print("執行這個 py 程式要帶一個目標 url當參數") 
    exit(1) 

url=sys.argv[1]
domain="{}://{}".format(urlparse(url).scheme, urlparse(url).hostname) #說明-->web_scraping_26_explan.ipynb
html=requests.get(url).text
bsObj=BeautifulSoup(html,'html.parser') #'html.parser', 'lxml', 'html5lib',...
all_links=bsObj.find_all(['a','img']) #find all tag <a> and tag <img>

#for 迭代
for link in all_links:
    src=link.get('src') #get src 屬性值
    href=link.get('href') #get href 屬性值
    targets=[src,href]
    for t in targets:
        if t !=None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                print(t)
            else:
                print(domain+t)
    
    
    
    
    
    
    
    
    
    
