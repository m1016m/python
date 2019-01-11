# -*- coding: utf-8 -*-
"""
web_scraping_010b_Ajax.py
"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup

#叫用webdrier.PhantomJS class,需明確指定phantomjs.exe 所在路徑及位置(注意 \\ )
exe_path="E:\\phantomjs\\bin\\phantomjs" #明確指定phantomjs.exe 執行檔
driver=webdriver.PhantomJS(executable_path=exe_path)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3) #暫停3秒

#將取回資料轉成page sourese
pageSource=driver.page_source
#轉成 bs4 tree
bsObj=BeautifulSoup(pageSource,'lxml')
print(bsObj.find(id="content").get_text())
driver.close()