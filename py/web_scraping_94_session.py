# -*- coding: utf-8 -*-
"""
web_scraping_94_session.py
Created on Thu Jun 22 16:05:28 2017
@author: III
"""
import requests
sess01=requests.Session() #建一個session object sess01
params={'username':'Jack','password':'password'} 
#使用session.post() 
s=sess01.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
s.cookies #檢視 cookies
print(s.cookies.get_dict()) #叫用 get_dict() method
#----------------------------------------------------------------------
#使用session.get() 到profile.php, 不用附cookies
s = sess01.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

#session object, 會追蹤session資訊，像是cookies、headers 
