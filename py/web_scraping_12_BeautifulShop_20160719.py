# coding: utf-8
#web_scraping_12_BeautifulShop_20160719

#Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying
#the parse tree. 

from urllib.request import urlopen #from urllib.request import urlopen() function
from bs4 import BeautifulSoup #from bs4 library import BeautifulSoup

html=urlopen("http://www.iiiedu.org.tw/south/") #取得資策會高雄網站首頁 html file
bsObj=BeautifulSoup(html,'lxml') #以BeautifulSoup() 將html 轉成 BeautifulSoup object bsObj
bsObj #直接看 bs object

#prettify() functin, 排版美化
print(bsObj.prettify()) #使用bs object prettify() 排版美化

#navigate that data structure (bs tree) 
bsObj.html.head.title #tag <title>
bsObj.title #這樣也可以

bsObj.title.name #tag <title> 的name
bsObj.title.string #tag <title> 的內容字串
bsObj.head.findAll("meta") #tag <head> 內,所有 tag <meta> --> 以Python list 傳回

meta_list=bsObj.head.findAll("meta") #存成list meta_list
meta_list[2] #meta_list 第三個元素
meta_list[2].attrs #meta_list[2] 的屬性(attrs) -->以Python dict. 傳回
meta_list[2].attrs["content"] #"content"屬性的值 -->以Python str 傳回

#findAll()  / find() 
bsObj.findAll("a") #找所有 tag <a> -->以Python list 傳回
bsObj.find(alt="Google PageRank查詢") #找第一個屬性 alt="Google PageRank查詢" 的 tag --> bs4.element.Tag

#get()
for link in bsObj.findAll("a"): #將每個 tag <a> 中,屬性 href 的值
    print(link.get('href'))     #以 get() 取出 

#練習: 將上式以 list comprehension 改寫:

[link.get('href') for link in bsObj.findAll("a")]

#get_text()
print(bsObj.title.get_text()) #tag <title> 的 text
print(bsObj.get_text()) #所有 tag 的 text



