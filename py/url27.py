# -*- coding: utf-8 -*-
# Fetching URLs
# for python 2.7
import requests #import 非標準程式庫模組(外部Python套件) requests
response=requests.get("http://www.iiiedu.org.tw/south/")
txt=response.text
print(txt)