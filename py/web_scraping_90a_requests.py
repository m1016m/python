# -*- coding: utf-8 -*-
"""
web_scraping_90a_requests.py
Created on Wed Jun 21 14:59:52 2017
@author: III
"""
import requests
#requests.get
r = requests.get('https://api.github.com/events')
#Response object called r. 
#We can get all the information we need from this object.
type(r) #requests.models.Response
