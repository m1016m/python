# -*- coding: utf-8 -*-
"""
web_scraping_90_forms.py
Created on Wed Jun 21 14:01:50 2017
@author: III
"""
import requests #http://www.python-requests.org
#POST 參數,dicts. params
params={'firstname':'Jack','lastname':'Huang'}
#交給action 程式, processing.php
r=requests.post('http://pythonscraping.com/files/processing.php',data=params)
print(r.text)
