#确认Scrapy已安装成功，首先在Python中测试能否导入Scrapy
import scrapy
scrapy.version_info

#然后，测试能否执行Scrapy这条命令
# scrapy

# 在专门供爬虫初学者训练爬虫技术的网站（http://books.toscrape.com）上爬取书籍信息,该网站中，这样的书籍列表页面一共有50页，每页有20本书，第
# 一个例子应尽量简单。我们下面仅爬取所有图书（1000本）的书名和价格信息
#首先，我们要创建一个Scrapy项目，在shell中使用scrapystartproject命令
#scrapy startproject example
#可使用tree命令查看项目目录下的文件  tree example
#分析页面
# 1．数据信息在Chrome浏览器中打开页面http://books.toscrape.com，选中其中任意一本书并右击，然后选择“檢查”，查看其HTML代码
#   可以看到，每一本书的信息包裹在<article class="product_pod">元素中：书名信息在其下h3 > a元素的title属性中，
#   如<a href="catalogue/a-light-in-theattic_1000/index.html"title="A Light in the Attic">A Light inthe...</a>
#  ；书价信息在其下<p class="price_color">元素的文本中，如<p class="price_color">£51.77</p>。
# 2．链接信息 单击next按钮访问下一页，选中页面下方的next按钮并右击，然后选择“檢查”可以发现，下一页的URL在ul.pager > li.next > a
#   元素的href属性中，是一个相对URL地址，如<li class="next"><ahref="catalogue/page-2.html">next</a></li>

# 实现Spider 实现爬虫的Python文件应位于exmaple/spiders目录下

import scrapy


class BooksSpider(scrapy.Spider):
    # 每一个爬虫的唯一标识
    name = 'books'

    # 定义爬虫爬取的起始点，起始点可以是多个，这里只有一个
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # 提取数据
        # 每一本书的信息在<article class="product_pod">中，我们使用
        # css()方法找到所有这样的 article 元素，并依次迭代
        #https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/selectors.html
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name': name,
                'price': price,
            }

        # 提取链接
        # 下一页的 url 在 ul.pager > li.next > a 里面
        # 例如：<li class="next"><a href="catelogue/page-2.html">next</a><li>
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            # 如果找到下一页的 URL，得到绝对路径，构造新的 Request 对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

# ● name属性
# 一个Scrapy项目中可能有多个爬虫，每个爬虫的name属性是其自身的唯一标识，在一个项目中不能有同名的爬虫，本例中的
# 爬虫取名为'books'。

# ●　start_urls属性
# 一个爬虫总要从某个（或某些）页面开始爬取，我们称这样的页面为起始爬取点，start_urls属性用来设置一个爬虫的起始
# 爬取点。在本例中只有一个起始爬取点'http://books.toscrape.com'。

# ●　parse方法
# 当一个页面下载完成后，Scrapy引擎会回调一个我们指定的页面解析函数（默认为parse方法）解析页面。一个页面解析函
# 数通常需要完成以下两个任务：
# 　提取页面中的数据（使用XPath或CSS选择器）。
# 　提取页面中的链接，并产生对链接页面的下载请求。

# HtmlResponse对象有很多属性，但最常用的是以下的3个方
# 法：
# ●　xpath(query)
# ●　css(query)
# ●　urljoin(url)
# 前两个方法用于提取数据，后一个方法用于构造绝对url

# 运行爬虫 scrapy crawl books -o books.csv

# 發生TypeError: 'float' object is not iterable的問題
# 卸载twisted重装

# pip uninstall twisted

# pip install twisted==16.6.0
