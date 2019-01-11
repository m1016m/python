# -*- coding: utf-8 -*-
"""
web_scraping_0101_Firefox.py
"""
from selenium import webdriver
exec_path="C:\\Program Files (x86)\\Mozilla Firefox\\firefox"
web=webdriver.Firefox(executable_path=exec_path)
web.get('http://taipei.iiiedu.org.tw/')

