from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchelementException
from selenium.webdriver.common.keys import keys
import time
from bs4 import BeautifulSoup

chrome_path = "./chromedriver" #chromedriver.exe執行檔所存在的路徑
browser = webdriver.Chrome(chrome_path)

browser.get('https://www.agoda.com/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?znrid=82c43b6a-a9bb-43c0-bcb0-62c1206ed269&city=4951&recommendedIndex=6&languageId=20&userId=bc9c4ef6-ed9f-4832-9b6d-e19bc2591015&pageTypeId=1&origin=TW&locale=zh-TW&cid=1732642&tag=41460a09-3e65-d173-1233-629e2428d88e&gclid=EAIaIQobChMIxKCv3Kf23AIVVXRgCh2wywWAEAAYASAAEgKy8vD_BwE&aid=81837&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=bc9c4ef6-ed9f-4832-9b6d-e19bc2591015&prid=0&checkIn=2018-08-25&checkOut=2018-08-26&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&productType=-1&sort=agodaRecommended')
browser.find_element_by_link_text('下一頁').click()
