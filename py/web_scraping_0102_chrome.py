# -*- coding: utf-8 -*-
"""
web_scraping_0102_chrome.py
"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup
chrome_path="c:\\selenium_chrome\\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑 
web=webdriver.Chrome(chrome_path)
web.get('http://www.cwb.gov.tw/V7/') #中央氣象局

web.set_window_position(0,0) #設定瀏覽器位置
web.set_window_size(600,600) #設定瀏覽器大小

#停個5秒讓scrapter 看起來像個人
time.sleep(5)

#使用 find_element_by_link_text() 選擇器 找到 '國際都市' 鏈結  
web.find_element_by_link_text('國際都市').click() #點擊'國際都市'鏈結

#在等個5秒
time.sleep(5)

#找 '生活氣象' 鏈結, 點擊鏈結後 將資料取回
web.find_element_by_link_text('生活氣象').click()
pageSouce=web.page_source

bsObj=BeautifulSoup(pageSouce,'lxml')
