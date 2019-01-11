# -*- coding: utf-8 -*-
"""
iiiSpider.py
Created on Fri Jun 16 15:48:09 2017
@author: zzjack
"""
from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article #這是我們剛寫的

#定義一個類別 iiiSpider,參數是 scrapy.Spider Object
class iiiSpider(Spider):
    name="iiiInfo" #執行時呼叫此名稱
    allowed_domains = ["www.iii.org.tw"]
    #指定的url清單 (list of url)
    start_urls = ["http://www.iii.org.tw/Info/ClassList.aspx?fm_sqno=38"]
    def parse(self, response): #定義parse() function
        item = Article() #new 一個 Article 物件,(我們在樣板 items.py 中定義)
        content = response.xpath('//h3[@class="mcate-item-hd"]/span/a/text()')[0].extract()
        print("content: "+content)
        item['content'] = content
        return item
    
#學習xpath: https://www.w3schools.com/xml/xpath_intro.asp    