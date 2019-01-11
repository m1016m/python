# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field #import Item and Field type

class Article(Item): #定義一個 Article 類別, 傳入參數是 scrapy.Item
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field() 
    content = Field()
#每個 Scrapy 的 Item 物件都代表網站上的單一page
#你可以視需求,定義頁面中想蒐集的欄位,本例中定義了 title及content 兩個欄位

