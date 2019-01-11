# -*- coding: utf-8 -*-
"""
web_scraping_ch05_02.py
Created on Wed Nov  9 15:57:33 2016

@author: zzjack
"""
#The following will download all internal files, linked to by any tag’s src
#attribute, from the home page of http://pythonscraping.com
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory="downloaded"
baseUrl="http://pythonscraping.com"

#定義函數 getAbsoluteURL()
def getAbsoluteURL(baseUrl,source):
    if source.startswith("http://www."): #如果開頭是"http://www."
        url="http://"+source[11:]        #url從"http://www."之後接上
    elif source.startswith("http://"):   #如果開頭是"http://"
        url=source                       #url=source
    elif source.startswith("www."):      #如果開頭是"www." 
#        url=source[4:]                  #原書程式碼有誤?
#        url="http://"+source
        url="http://"+source[4:] 
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:               
        return None
    return url

#定義一個 getDownloadPath() function
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path
    directory = os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    return path
#
html=urlopen("http://pythonscraping.com")
bsObj=BeautifulSoup(html,"lxml")
downloadList=bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))














    

