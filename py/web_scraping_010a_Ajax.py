# -*- coding: utf-8 -*-
"""
web_scraping_010a_Ajax.py
"""
from selenium import webdriver
import time

#叫用webdrier.PhantomJS class,需明確指定phantomjs.exe 所在路徑及位置(注意 \\ )
exe_path="E:\\phantomjs\\bin\\phantomjs" #明確指定phantomjs.exe 執行檔
driver=webdriver.PhantomJS(executable_path=exe_path)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3) #暫停3秒
#Selenium Selector, find_element_by_id()
print(driver.find_element_by_id("content").text)
driver.close()