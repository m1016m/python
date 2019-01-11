# -*- coding: utf-8 -*-
"""
web_scraping_27_storage_20161217.py
Created on Sat Dec 17 16:51:31 2016

@author: jack huang
"""
#將擷取的資料存檔
from bs4 import BeautifulSoup
import requests
import sys, os
from urllib.parse import urlparse
from urllib.request import urlopen

#檢查當執行本 script 時,如果未代一<<url>>當參數,提醒並終止程式
if len(sys.argv) < 2:  #len(sys.argv) < 2 -->就是不帶參數
    print("執行這個 py 程式要帶一個目標 url當參數") 
    exit(1) 
    
url=sys.argv[1]
domain="{}://{}".format(urlparse(url).scheme, urlparse(url).hostname) #說明-->web_scraping_26_explan.ipynb
html=requests.get(url).text
bsObj=BeautifulSoup(html,'html.parser') #'html.parser' 
all_links=bsObj.find_all(['a','img'])

for link in all_links:
    src=link.get('src')
    href=link.get('href')
    targets=[src,href]
    for t in targets:
        if t !=None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'): full_path=t 
            else:  full_path=domain+t
            print(full_path)
            image_dir=url.split('/')[-1] #
            if not os.path.exists(image_dir): os.mkdir(image_dir) #如果目錄不存在就建一個
            filename=full_path.split('/')[-1] #拆出full_path最後一段為filename
            ext=filename.split('.')[-1]  #拆出 *.ext
            filename=filename.split('.')[-2] #拆出 filename.*
            if 'jpg' in ext: filename=filename+'.jpg'
            else:            filename=filename+'.png'
            image=urlopen(full_path)
            fp=open(os.path.join(image_dir,filename),'wb') #'wb', write bytes
            fp.write(image.read())
            fp.close()
            
            
    
    
    
    
    
    
    
    
    
