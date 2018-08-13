from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]#選擇過的網頁將它抽取出來,再進行下一次的爬取,-1就是抽出最後一個

for i in range(20):
    # dealing with Chinese symbols
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])# 非重置抽樣，不會抽到相同的元素random.sample(sub_urls, 1)
    else:
        # no valid sub link found
        his.pop()

'''
重置抽樣、非重置抽樣
Sampling with replacement: 從總體抽出一個元素後，會將該元素放回總體。接著重新抽取，因此有機會抽取到相同的元素。
Sampling without replacement: 從總體抽出一個元素後，不會將該元素放回總體。因此不會在次抽到已抽到的元素。

random.choices(seq, k=3)  # 重置抽樣，有機會抽到相同的元素
'''
