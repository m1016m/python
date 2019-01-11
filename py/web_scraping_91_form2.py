# -*- coding: utf-8 -*-
"""
web_scraping_91_form2.py
Created on Wed Jun 21 16:08:20 2017
@author: III
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen('http://www.myav.com.tw/')
bsObj=BeautifulSoup(html,"lxml")
bsObj.findAll('form')