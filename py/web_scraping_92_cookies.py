# -*- coding: utf-8 -*-
"""
web_scraping_92_cookies.py
Created on Thu Jun 22 14:03:57 2017
@author: III
"""
import requests
params={'username':'Jack','password':'password'}
#將params POST 給 welcome.php
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)

r.cookies #檢視 cookies
print(r.cookies.get_dict()) #叫用 get_dict() method

#使用cookies 到profile.php
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
                 cookies=r.cookies)

print(r.text)
