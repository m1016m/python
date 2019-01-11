# -*- coding: utf-8 -*-
"""
#web_scraping_09_attribute_20160717.py
Created on Mon Jun 12 10:41:44 2017
@author: III
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#資策會網站 "http://www.iiiedu.org.tw/south/"
html=urlopen("http://www.iiiedu.org.tw/south/")
bsObj=BeautifulSoup(html,"lxml")

myTag=bsObj.find("img") #找到的第一個 img tag <img>...
myTag #bs4.element.Tag

#使用 Tag.attrs() method 擷取Tag內的屬性
#回傳的是 dict. object 
myTag.attrs #myTag.attrs 回傳的是 Python dict. object 

#既然是字典物件,我們就用字典的存取方式
myTag.attrs['src'] #'https://www.facebook.com/tr?id=293389681044925&ev=PageView&noscript=1'
myTag.attrs['style'] #'display:none'

#-------------------------------------------------------------
#lambda expression
#example: 找出有三個 attribute 的 tag
bsObj.findAll(lambda tag: len(tag.attrs)==3)
