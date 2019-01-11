# -*- coding: utf-8 -*-
"""
web_scraping_25_beautifulsoup4_20161201.py
Created on Thu Dec 01 16:30:25 2016
@author: zzjack
"""
#取得某一網頁的全部鏈結，並將這些鏈結的內容全部完整網址列出
from bs4 import BeautifulSoup
import requests
import sys

#檢查當執行本 script 時,如果未代一<<url>>當參數,提醒並終止程式
if len(sys.argv) < 2:  #len(sys.argv) < 2 -->就是不帶參數
    print("執行這個 py 程式要帶一個目標 url當參數") #
    exit(1)   #exit(0) means a clean exit without any errors / problems
              #exit(1) means there was some issue / error / problem and that is why the program is exiting.    

url=sys.argv[1] #將<<url>>參數指給變數 url

html=requests.get(url).text
bsObj=BeautifulSoup(html,'html.parser')

all_links=bsObj.find_all('a') #以find_all('a')擷取所有 tag <a>

for link in all_links:    #從list all_links逐一
    href=link.get('href') #取得tag中 href屬性值
    if href != None and href.startswith('http://'): 
        print(href)





#sys.argv[]是python獲取命令列參數的方法
#譬如我們在terminal中會輸入的指令
#ls -a
#-a就是命令列參數
#sys.argv[0] 代表了文件的檔案名稱本身
#意思就是ls 
#sys.argv[1] 就代表了-a  




