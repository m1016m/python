# -*- coding: utf-8 -*-
"""
web_scraping_41_text_20161221.py
Created on Wed Dec 21 15:19:23 2016
@author: zzjack
"""
#Encodings in action
#"http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt"
from urllib.request import urlopen
textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(textPage.read())
