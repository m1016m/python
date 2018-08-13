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

    # 僅當容器具有Metascore時才提取感興趣的數據點:
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

'''
如果您從一個英語不是主要語言的國家/地區運行代碼，您很可能會將某些電影名稱翻譯成該國家/地區的主要語言。

最有可能的是，這是因為服務器從您的IP地址推斷出您的位置。即使您位於以英語為主要語言的國家/地區，

您仍可以獲得翻譯內容。如果您在GET提出請求時使用VPN，則可能會發生這種情況。
'''

headers = {"Accept-Language": "en-US, en;q=0.5"} #該q參數表示我們偏好某種語言的程度。如果未指定，則1默認情況下將值設置

'''
我們將通過做三件事來構建我們的單頁腳本：

1.在循環中完成我們想要的所有請求。
2.控制循環的速率以避免使用請求轟炸服務器。
3.在循環運行時監視循環。
我們將在2000-2017的間隔期間刮掉每年的前4頁。這18年中每頁有4頁，總共72頁。每頁有50部電影，所以我們最多可以收集3600部電影的數據。
但並非所有的電影都有Metascore，所以這個數字會低於那個。即便如此，我們仍然很有可能獲得超過2000部電影的數據。

在我們提出請求時，我們只需要改變URL的兩個參數的值：release_date參數和page。讓我們為即將到來的循環準備我們需要的值。
在下一個代碼單元格中，我們將：
http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1
創建一個名為的列表pages，並使用與前4頁對應的字符串填充它。
創建一個名為的列表years_url，並使用與2000-2017年對應的字符串填充它
'''
pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]


start_time = time()
requests = 0
'''
控制爬行率
控制爬行速度對我們以及我們正在抓取的網站都是有益的。如果我們避免每秒數十次請求錘擊服務器，那麼我們就不太可能禁止我們的IP地址
。我們還通過允許服務器響應其他用戶的請求來避免破壞我們網站的活動。
我們將使用Python 模塊中的sleep() 函數來控制循環的速率。將暫停執行循環指定的秒數。time sleep()
'''
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
'''
對於我們的腳本，我們將使用此功能，並監視以下參數：

1.請求的頻率（速度），因此我們確保我們的程序不會使服務器超載。
2.該請求的數量，所以我們可以停止的情況下，超出預期的請求數量的循環。
3.我們的請求的狀態代碼，因此我們確保服務器發回適當的響應。
為了獲得頻率值，我們將請求數除以自第一次請求以來經過的時間。這類似於計算汽車的速度 - 

我們將距離除以覆蓋該距離所需的時間。讓我們首先以小規模試驗這種監測技術。在下面的代碼單元格中，我們將：

使用所設定的開始時間time() 函數從time 模塊，並分配值start_time。
將0分配給requests我們將用於計算請求數的變量。
開始循環，然後每次迭代：
模擬請求。
請求數增加1。
暫停循環8到15秒的時間間隔。
計算自第一個請求以來經過的時間，並將值賦給elapsed_time。
打印請求數和頻率。
'''

'''
1.循環遍歷years_url列表以更改release_dateURL 的參數。
2.對於每個元素years_url，循環遍歷pages列表以改變pageURL 的參數。
3.使GET該範圍內的請求pages環（並給出headers參數的權值，以確保我們得到的只有英文內容）。
4.暫停循環8到15秒的時間間隔。
5.如前所述監控每個請求。
6.對非200狀態代碼發出警告。
7.如果請求數大於預期，則中斷循環。
8.將responseHTML內容轉換為BeautifulSoup對象。
9.從此對BeautifulSoup像中提取所有影片容器。
10.循環遍歷所有這些容器。
11.如果容器具有Metascore，則提取數據。
'''
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
        clear_output(wait = True)#由於我們要發出72個請求，因此隨著輸出的累積，我們的工作看起來有些不整潔。
        #為避免這種情況，我們將在每次迭代後清除輸出，並將其替換為有關最新請求的信息。為此，我們將使用IPython 
        #模塊中的clear_output()函數

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:#只發出72個請求
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
'''
將數據合併到一隻熊貓中DataFrame。
打印有關新創建的一些信息DataFrame。
顯示前10個條目。
'''
movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'metascore': metascores,
                              'votes': votes})
print(movie_ratings.info())
movie_ratings.head(10)

'''
重新排序列。
清理year列並將值轉換為整數。
檢查極限額定值以確定所有額定值是否在預期的時間間隔內。
歸一化評級類型之一（或兩者）以生成比較直方圖。
'''
movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
movie_ratings.head()

'''
現在讓我們將year列中的所有值轉換為整數。

現在所有的值都屬於這種object類型。為避免ValueErrors轉換，我們希望值僅由0到9的數字組成。

我們來檢查year列的唯一值。這有助於我們了解我們可以做些什麼來實現我們想要的轉化。要查看所有唯一值，我們將使用以下unique()方法：
'''
movie_ratings['year'].unique()

'''
從最後開始計算，我們可以看到年份總是從第五個字符到第二個字符。我們將使用該.str() 方法僅選擇該間隔。
我們還將使用以下astype() 方法將結果轉換為整數：
'''
movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)#str[]通过索引获取字符串中字符
movie_ratings['year'].head(3)

'''
現在我們將檢查每種評級的最小值和最大值。我們可以使用pandas的describe() 方法快速完成這項工作。
'''
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

'''
從IMDB 直方圖開始，我們可以看到大多數收視率在6到8之間。評分大於8的電影很少，評分小於4時甚至更少。這表明非常好的電影和非常糟糕的電影很少見。

Metascore評級的分佈類似於正態分佈 - 大多數評級為平均值，峰值為50左右。從此峰值開始，頻率逐漸降低至極端評級值。根據這一分佈，確實有更少的非常好和非常糟糕的電影，但不像IMDB評級所表明的那麼少。

在比較圖表中，更明確的是IMDB分佈高度傾向於平均評級的較高部分，而Metascore評級似乎具有更均衡的分佈。

可能是IMDB分佈出現偏差的原因是什麼？一種假設是許多用戶傾向於使用二進制方法來評估電影。如果他們喜歡這部電影，他們會給它一個10.如果他們不喜歡這部電影，他們會給它一個非常小的評價，或者他們不打算給電影評分。這是一個值得探討的有趣問題。

接下來
從請求單個網頁的內容到分析超過2000部電影的評級，我們已經走了很長的路。您現在應該知道如何使用相同的HTML和URL結構來抓取許多網頁。

在我們學到的東西的基礎上，接下來要考慮以下幾個步驟：

刮取不同時間和頁面間隔的數據。
刪除有關電影的其他數據。
尋找一個不同的網站來蒐集您感興趣的內容。例如，您可以抓取有關筆記本電腦的數據，以了解價格如何隨時間變化。

Pandas 提供的資料結構
1.Series：用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。
2.DataFrame：用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等。
3.Panel：用來處理有資料及索引、列索引與欄標籤的三維資料集。
DataFrame 的操作 
❖ 資料描述查看 
可以透過下列方法查看目前資料的資訊
.shape
.describe()
.head()
.tail()
.columns
.index
.info()
print(select_df.shape) # 回傳列數與欄數  
print("---")  
print(select_df.describe()) # 回傳描述性統計  
print("---")  
print(select_df.head(3)) # 回傳前三筆觀測值  
print("---")  
print(select_df.tail(3)) # 回傳後三筆觀測值  
print("---")  
print(select_df.columns) # 回傳欄位名稱  
print("---")  
print(select_df.index) # 回傳 index  
print("---")  
print(select_df.info) # 回傳資料內容  
'''