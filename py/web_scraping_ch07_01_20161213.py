# -*- coding: utf-8 -*-
"""
web_scraping_ch07_01_20161213.py
Created on Tue Dec 13 16:13:21 2016

@author: zzjack
"""
#The following will return a list of 2-grams found in the Wikipedia article on the
#Python programming language:

from urllib.request import urlopen #python 2.7 --> import urllib2 / response = urllib2.urlopen('http://python.org/')
from bs4 import BeautifulSoup

#定義函數 getNgrams
def getNgrams(input, n):
    input=input.split(' ') #以 ' ' 空白,作split
    output = []            #空list output
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

#以urlopen 開啟 url "http://en.wikipedia.org/wiki/Python_(programming_language)"
html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj=BeautifulSoup(html,'lxml')