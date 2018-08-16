import numpy
import scipy
import sklearn
from selenium import webdriver
import time

'''
Selenium提供利用瀏覽器對Web進行操作測試，

本篇利用Python來控制Chrome瀏覽器的操作。

 首先當然是必須已安裝好Chrome瀏覽器啦~

https://sites.google.com/a/chromium.org/chromedriver/downloads

（記得要選取您的作業系統的對應版本唷）

 下載完畢之後進行解壓縮，會有chromedriver.exe的執行檔，

 chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
 '''

from selenium import webdriver
import time

chrome_path = "./chromedriver" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(700,700) #瀏覽器大小
time.sleep(5)

web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
time.sleep(5)

web.close()


