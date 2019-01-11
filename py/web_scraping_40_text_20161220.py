# -*- coding: utf-8 -*-
"""
web_scraping_40_text_20161220.py
Created on Tue Dec 20 14:56:16 2016
@author: zzjack
"""
from urlllib.request import urlopen
textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())

