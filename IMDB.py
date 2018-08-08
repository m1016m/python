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
print ("電影名稱 : " ,first_movie.h3.a.text)
'''
點表示法只能訪問第一個span元素。我們將通過第二個的獨特標記進行搜索<span>。我們將使用的find() 

方法幾乎是一樣的find_all()，但它僅返回第一個匹配。實際上，find()相當於find_all(limit = 1)。

的limit 參數限制了輸出到第一匹配。區分標記由lister-item-year text-muted unbold分配給class

屬性的值組成。所以我們<span>在<h3>標籤中尋找帶有這些值的第一個：

'''
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year = first_year.text
print ("發行年份 : " , first_year)
first_imdb = float(first_movie.strong.text)
print ("IMDB評級 : " , first_imdb)

'''
我們最好使用class屬性（metascore favorable）的獨特值。
請注意，如果從DevTools選項卡中復制粘貼這些值，則metascore和之間將有兩個空格字符favorable。
將值作為參數傳遞給class_參數時，請確保只有一個空格字符。否則，find()什麼都找不到。
'''
first_mscore = first_movie.find('span', class_ = 'metascore favorable')
print(type(first_mscore))
first_mscore = int(first_mscore.text)
print("Metascore 評分 :" , first_mscore)