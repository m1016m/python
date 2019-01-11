# -*- coding: utf-8 -*-
"""
web_scraping_21_urlparse_20161201.py
Created on Thu Dec 01 11:18:05 2016

@author: zzjack
"""
#科技部網站求才訊息網頁
#https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&l=ch&view_mode=listView
from urllib.parse import urlparse
url='https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&l=ch&view_mode=listView'

uc=urlparse(url) #urlparse()
print("NetLoc(網域):",uc.netloc)
print("Path(路徑與檔案):",uc.path)

#以split('&') 切割 ?Query 參數
q_comds=uc.query.split('&')
print("Query Commands(查詢參數):")
for cmd in q_comds:
    print(cmd)