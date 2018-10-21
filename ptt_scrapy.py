'''
url:https://www.ptt.cc/bbs/Gossiping/index.html
看板內容需要滿18歲才可以瀏覽 set-cookie : over18 = 1;
所需文章資料
 每一篇文章 : <div class = "r-ent">
 標題 : <a>text
 網址 :<a href = >
 推文數 : <div class = "nrec">
 日期 : <div class = "date">
 上一頁按鈕所在 : <div class = "btn-group btn-group-pagin">
 流程：
   從最新頁面進入
   取得此頁所有今日文章和上一頁超連結
   若此頁包含今日文章,則暫存起來之後連到上一頁,進行步驟2
   顯示熱門文章,儲存所有文章

import requests
import time
import json
from bs4 import BeautifulSoup
PTT_URL = 'https://www.ptt.cc'

#取得網頁文件的function
def get_web_page(url):
    resp = requests.get(url = url,cookies = {'over18' : '1'})#跟網頁溝通
    if resp.status_code != 200 :
        print ('Invalid url',resp.url)
        return None
    else :
        return resp.text#如果網站正常回應的話就回傳

def get_articles(dom , date):
    soup = BeautifulSoup(dom , 'html5lib')
    #取得上一頁的連結
    paging_div = soup.find('div','btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []#儲存取得的文章資料
    divs = soup.find_all('div','r-ent')
    for d in divs :
        if d.find('div','date').text.strip() == date :#發文日期正確
            #取得推文數
            push_count =0
            push_str = d.find('div' ,'nrec').text
            if push_str :
                try :
                    push_count = int(push_str)#轉換字串為數字
                except ValueError :
                    #若轉換失敗則可能是'爆'或'X1'或'X2'.......
                    #若不是不做任何事情 push_count 保持0
                    #推文數有可能是'爆'或'空白'或'x'x就是噓
                    if push_str == '爆':
                        push_count = 99#把字串轉成數值
                    elif push_str.startswith('X') :
                        push_count = -10#把字串轉成數值
            #取得文章的連結和標題
            if d.find('a') :#有超連結表示文章存在未被刪除
                href = d.find('a')['href']
                title = d.find('a').text
                author = ''
                articles.append({'title':title ,
                                'href':href,
                                'push_count':push_count,
                                'author':author
                                })
    return articles,prev_url#回傳這一頁的文章和上一頁

def get_author_ids(posts , pattern):
    ids = set()
    for post in posts :
        if pattern in post['author']:
            ids.add(post['author'])
    return ids

if __name__ == '__main__':
    current_page = get_web_page(PTT_URL+'/bbs/Gossiping/index.html')
    if current_page :
        articles = []#全部的今日文章
        today = time.strftime('%m/%d').lstrip('0')#今天日期去掉開頭0符合PTT網站格式
        current_articles,prev_url = get_articles(current_page,today)#目前頁面的今日文章
        while current_articles:#若目前頁面有今日文章就加入articles,並回到上一頁繼續尋找是否有今日文章
            articles+=current_articles
            current_page = get_web_page(PTT_URL+prev_url)
            current_articles,prev_url = get_articles(current_page,today)
        
        #印出所有不同的5566 id
        #print (get_author_ids(articles , '5566'))
        #儲存或處理文章資訊
        print ('今天有',len(articles),'篇文章')
        threshold = 50
        print ('熱門文章 (> %d  推) :'%(threshold))
        for a in articles:
            if int(a['push_count']) > threshold:
                print (a)
        with open('gossiping.json','w',encoding = 'utf-8') as f :
            json.dump(articles , f , indent =2, sort_keys=True , ensure_ascii=False)
'''

import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json


PTT_URL = 'https://www.ptt.cc'

#取得網頁文件的function
def get_web_page(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html.parser')

    # 取得上一頁的連結
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []  # 儲存取得的文章資料
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        if d.find('div', 'date').string.strip() == date:  # 發文日期正確
            # 取得推文數
            push_count = 0
            if d.find('div', 'nrec').string:
                try:
                    push_count = int(d.find('div', 'nrec').string)  # 轉換字串為數字
                except ValueError:  # 若轉換失敗，不做任何事，push_count 保持為 0
                    pass

            # 取得文章連結及標題
            if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count
                })
    return articles, prev_url#回傳這一頁的文章和上一頁


def parse(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    links = soup.find(id='main-content').find_all('a')
    img_urls = []
    for link in links:
        if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
            img_urls.append(link['href'])
    return img_urls


def save(img_urls, title):
    if img_urls:
        try:
            dname = title.strip()  # 用 strip() 去除字串前後的空白
            os.makedirs(dname)
            for img_url in img_urls:
                if img_url.split('//')[1].startswith('m.'):
                    img_url = img_url.replace('//m.', '//i.')
                if not img_url.split('//')[1].startswith('i.'):
                    img_url = img_url.split('//')[0] + '//i.' + img_url.split('//')[1]
                if not img_url.endswith('.jpg'):
                    img_url += '.jpg'
                fname = img_url.split('/')[-1]
                urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    current_page = get_web_page(PTT_URL + '/bbs/Beauty/index.html')
    if current_page:
        articles = []  # 全部的今日文章
        date = time.strftime("%m/%d").lstrip('0')  # 今天日期, 去掉開頭的 '0' 以符合 PTT 網站格式
        current_articles, prev_url = get_articles(current_page, date)  # 目前頁面的今日文章
        while current_articles:  # 若目前頁面有今日文章則加入 articles，並回到上一頁繼續尋找是否有今日文章
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, date)

        # 已取得文章列表，開始進入各文章讀圖
        for article in articles:
            print('Processing', article)
            page = get_web_page(PTT_URL + article['href'])
            if page:
                img_urls = parse(page)
                save(img_urls, article['title'])
                article['num_image'] = len(img_urls)

        # 儲存文章資訊
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)

'''
json.loads()是将str转化成dict格式，json.dumps()是将dict转化成str格式。
json.load()和json.dump()也是类似的功能，只是与文件操作结合起来了。
join()： 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key
ensure_ascii：默认值True，如果dict内含有non-ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示
indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json
separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。
encoding：默认是UTF-8，设置json数据的编码方式。
sort_keys：将数据根据keys的值进行排序。(a-z)
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

'''






