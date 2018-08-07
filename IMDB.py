from requests import get
from bs4 import BeautifulSoup
'''
讓我們通過請求這個單一網頁的內容開始編寫腳本
：http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1。
在下面的代碼單元格中，我們將：

get()從requests模塊導入功能。
將網頁的地址分配給名為的變量url。
通過使用請求服務器網頁的內容get()，並將服務器的響應存儲在變量中response。
response通過訪問其.text屬性（response現在是Response對象）打印一小部分內容。
'''
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)
print(response.text[:500])

'''
response.text通過創建BeautifulSoup對象進行解析，
並將此對象指定給html_soup。該'html.parser'參數表明我們希望使用Python的內置HTML解析器進行解析。
'''
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))
'''
我們可以使用列表表示法訪問第一個容器，其中包含有關單個電影的信息movie_containers。
'''
first_movie = movie_containers[0]#movie message
print (first_movie.div)
print (first_movie.h3.a)
first_name = first_movie.h3.a.text
print (first_name)