# -*- coding: utf-8 -*-
"""
web_scraping_20_urlparse_2016120.py
Created on Mon Jun 12 11:55:44 2017

@author: III
"""
#urllib.parse module, urlparse() function, 
#將url 'https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg=4' 拆解
from urllib.parse import urlparse
uc=urlparse('https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg=4')

#檢視:
type(uc) #urllib.parse.ParseResult
uc       #ParseResult(scheme='https', netloc='tw.stock.yahoo.com', 
         #path='/news_list/url/d/e/N1.html', params='', query='q=&pg=4', fragment='')

uc.scheme #檢視 uc 的schema (protocol) --> 'https'
uc.netloc #檢視 uc 的netloc (網域名稱) --> 'tw.stock.yahoo.com'
uc.path #檢視 uc 的path (網頁所在位置與網頁檔案) -->'/news_list/url/d/e/N1.html'
uc.query #檢視 uc 的query (查詢,GET 參數) --> 'q=&pg=4'