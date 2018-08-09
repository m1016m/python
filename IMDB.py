from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output
from warnings import warn
import matplotlib.pyplot as plt
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

'''
投票數包含在<span>標籤中。它的獨特標誌是name具有價值的屬性nv。
該name屬性與class屬性不同。使用BeautifulSoup，我們可以通過任何屬性訪問元素。
該find()和find_all()功能有一個名為參數attrs。為此，我們可以將我們搜索的屬性和值傳遞為字典：
'''
first_votes = first_movie.find('span', attrs = {'name':'nv'})
print (first_votes.text)
print ("投票數 : " +first_votes['data-value'])#int
'''
我們可以使用.text符號來訪問<span>標籤的內容。如果我們訪問data-value屬性的值會更好。

這樣我們就可以將提取的數據點轉換為一個int而不必刪除逗號。

您可以Tag像對待字典一樣對待對象。HTML屬性是字典的鍵。HTML屬性的值是字典鍵的值。

這是我們如何訪問data-value屬性的值：
'''

names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Extract data from individual movie container
for container in movie_containers:

    # If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:

        # The name
        name = container.h3.a.text
        names.append(name)

        # The year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)

        # The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # The Metascore
        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))

        # The number of votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))


test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       'imdb': imdb_ratings,
                       'metascore': metascores,
                       'votes': votes})
print(test_df.info())


pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]


start_time = time()
requests = 0

for _ in range(5):
    # A request would go here
    requests += 1
    sleep(randint(1,3))
    current_time = time()
    elapsed_time = current_time - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

warn("Warning Simulation")
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

# For every year in the interval 2000-2017
for year_url in years_url:

    # For every page in the interval 1-4
    for page in pages:

        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + year_url + 
        '&sort=num_votes,desc&page=' + page)

        # Pause the loop
        sleep(randint(8,15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')  
            break 

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_ = 'ratings-metascore') is not None:

                # Scrape the name
                name = container.h3.a.text
                names.append(name)

                # Scrape the year 
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                # Scrape the Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                # Scrape the number of votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))
movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'metascore': metascores,
                              'votes': votes})
print(movie_ratings.info())
movie_ratings.head(10)
movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
movie_ratings.head()
movie_ratings['year'].unique()
movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
movie_ratings['year'].head(3)
movie_ratings.describe().loc[['min', 'max'], ['imdb', 'metascore']]
movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
movie_ratings.head(3)
movie_ratings.to_csv('movie_ratings.csv')

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes

ax1.hist(movie_ratings['imdb'], bins = 10, range = (0,10)) # bin range = 1
ax1.set_title('IMDB rating')

ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) # bin range = 10
ax2.set_title('Metascore')

ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
ax3.legend(loc = 'upper left')
ax3.set_title('The Two Normalized Distributions')

for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.show()