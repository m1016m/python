# -*- coding: utf-8 -*-
"""
web_scraping_ch05_01b.py
http://taipei.iiiedu.org.tw/ , 資策會台北中心
"""
#In Python 3.x, urllib.request.urlretrieve can be used to download files 
#from any remote URL:
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#"http://taipei.iiiedu.org.tw/"
html=urlopen("http://taipei.iiiedu.org.tw/")
bsObj=BeautifulSoup(html,'lxml')
#找出所有含有*.jpg檔的 <img> tag (<img src='*.jpg'>)
img=bsObj.find_all('img',attrs={'src':re.compile('\.jpg')})

#先把*.jpg檔名印出來看看 (i['src']-->每個img tag, src 屬性的值)
for i in img:
    print(i['src'])
    
#把url開頭為'http'的檔案全抓下來:
count=1
for item in img:
    if re.search('^http',item['src']):
        imageLocation=item['src']
        fileName=str(count)+'.jpg'
        #以urlretrive() function, 將URL imageLocation抓取到現行目錄,並存為'count.jpg' 檔名
        urlretrieve(imageLocation,fileName)          
        count+=1
