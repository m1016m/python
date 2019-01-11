# -*- coding: utf-8 -*-
"""
web_scraping_10_Ajax.py
@author: zzjack
"""
from urllib.request import urlopen #for python 3.x, if python 2.7 urllib2
from bs4 import BeautifulSoup #from bs4 import BeautifulSoup
html=urlopen("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
bsObj=BeautifulSoup(html.read(),"lxml")

print(bsObj.prettify())

