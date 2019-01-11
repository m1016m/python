# -*- coding: utf-8 -*-
"""
articleSpider2.py
"""
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor #sgml !!!
from wikiSpider.items import Article #這是我們剛寫的

#定義一個類別 ArticleSpider2,參數是 scrapy.CrawlSpider Object
class ArticleSpider2(CrawlSpider):
    name="article2" #crawl 時，呼叫的名稱
    allowed_domains = ["en.wikipedia.org"]
    #指定的url
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    #定義的規則 (regx--> '(/wiki/)((?!:).)*$')
    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback="parse_item", follow=True)]

    def parse_item(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title'] = title
        return item