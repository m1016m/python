# -*- coding: utf-8 -*-
"""
web_scraping_96_auth.py
Created on Thu Jun 22 18:04:16 2017
@author: III
"""
import requests
#The Requests package contains an auth module specifically designed to handle
#HTTP authentication
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

#create a HTTPBasicAuth Objct auth01,輸入值為 'jack','password'
auth01=HTTPBasicAuth('jack','password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", 
                  auth=auth01) #以requests.post(), 帶入 HTTPBasicAuth auth01
print(r.text)