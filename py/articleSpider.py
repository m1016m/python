# -*- coding: utf-8 -*-
"""
articleSpider.py
Created on Fri Jun 16 15:48:09 2017
@author: zzjack
"""
from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article #這是我們剛寫的

#定義一個類別 ArticleSpider,參數是 scrapy.Spider Object
class ArticleSpider(Spider):
    name="article" #執行時呼叫此名稱
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    def parse(self, response): #定義parse() function
        item = Article() #new 一個 Article 物件,(我們在樣板 items.py 中定義)
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item