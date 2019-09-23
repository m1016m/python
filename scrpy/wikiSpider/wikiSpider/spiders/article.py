# 輸入後會自動建立一些文件和設定，資料結構如下：
# scrapy startproject wikiSpider
# scrapy.cfg：基礎設置
# items.py：抓取條目的結構定義
# middlewares.py：中間件定義
# pipelines.py：管道定義，用於抓取數據後的處理
# settings.py：全局設置
# spiders\ptt.py：爬蟲主體，定義如何抓取需要的數據
# 此範例為擷取定義的URL
import scrapy
class ArticleSpider(scrapy.Spider):
    name='article'
    def start_requests(self):
        urls = [
            'http://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=url, callback=self.parse)
        for url in urls]
    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))


# 運行Scrapy爬蟲
# 返回terminal 命令行進入項目目錄，輸入命令即可運行：

# scrapy crawl ptt
# 如果需要對抓取的結果進行保存，只需要在命令行加參數 -o {filename} 即可：

# scrapy crawl ptt -o output.json # 輸出為JSON文件
# scrapy crawl ptt -o output.csv # 輸出為CSV文件

