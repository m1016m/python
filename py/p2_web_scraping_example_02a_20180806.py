# coding: utf-8
#p2_web_scraping_example_02a_20180806

#方法1: 使用 requests module
import requests
from bs4 import BeautifulSoup
url="http://www.pythonscraping.com/pages/page1.html"
iii_url="http://www.iiiedu.org.tw/south/"
#  使用requests.get(),以HTTP GET 方法送出一個(Request)
#  到遠端的Server, Server回應(Response)內容 
html=requests.get(url) 
iii_html=requests.get(iii_url)
# 設定正確的編碼 "utf-8"
html.encoding="utf-8"
iii_html.encoding="utf-8"
# 以BeautifulSoup() 將html.text 轉成 bs tree "bsObj"
bsObj=BeautifulSoup(html.text,"lxml")
iii_bsObj=BeautifulSoup(iii_html.text,"lxml")
# 檢視 bsObj/iii_bsObj, prettify() method --> 美化排版
print(bsObj.prettify())
print(iii_bsObj.prettify())

#====================================================
#方法2: 使用 urllib.request module
# from urllib.request import urlopen #from urllib.request import urlopen() function
# from bs4 import BeautifulSoup #from bs4 module import BeautifulSoup() function
# html=urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj=BeautifulSoup(html.read(),"lxml")
# iii_html=urlopen("http://www.iiiedu.org.tw/south/")
# iii_bsObj=BeautifulSoup(iii_html.read().decode(),"lxml") #有中文,必須decode()

#==========================================================
#findAll() function
bsObj.findAll("h1") #從bsObj中，找出所有 <h1> tag
iii_bsObj.findAll("meta") #從iii_bsObj中,找出所有 <meta> tag              
                          #結果是list of tags
iii_bsObj.findAll("meta")[0:2] #切前面兩個元素
iii_bsObj
iii_bsObj.findAll("body")[0] #findAll() 回傳的是 list
iii_bsObj.findAll("body")[0].findAll("a")
iii_bsObj.findAll("body")[0].findAll("a")[0].findAll("img")

#=====================================================================
#example 2 :"http://www.pythonscraping.com/pages/warandpeace.html"
url2="http://www.pythonscraping.com/pages/warandpeace.html"
html2=requests.get(url2)
html2.encoding="utl-8"
bsObj2=BeautifulSoup(html2.text,"lxml") #將html2轉成BeautifulSoup 物件
print(bsObj2.prettify())

# 所有 tag 為 span 且 Attribute class="green", findAll() 回傳一個 list
# list of tags, "namelist"
namelist=bsObj2.findAll("span",{"class":"green"})
                      
namelist[0:2] #第一、二個元素
print(namelist[0].get_text()) #list namelist 第一個元素的內容
print(namelist[1].get_text()) #list namelist 第二個元素的內容

#印出namelist 每一個 tag 的內容
for name in namelist:       
    print(name.get_text())

#tag 為<span>, attribute class="green" or "red"
namelist2=bsObj2.findAll("span",{"class":"green","class":"red"})

namelist2[1] #namelist2 第二個元素
namelist2[1].get_text()

#findAll(), 多個 tag <h1>, <h2>, <h3>, <h4>
h_tag_list=bsObj2.findAll({"h1","h2","h3","h4"}) 
h_tag_list

#findAll(), 只以 Attribute 做搜尋
bsObj2.findAll("",{"class":"green"}) #不管 tag, 只要Attribute class="green"

#find() 與 findAll()
bsObj2.find("span",{"class":"green"})  #找到第一個
bsObj2.findAll("span",{"class":"green"}) #找到所有

#BeautifulSoup Objects:
#1. BeautifulSoup Objects
#2. Tag Objects
#3. NavigableString Objects
#4. The Comment Objects
bsObj.html.body.h1 #BeautifulSoup Objects
bsObj2.findAll("span")[0:2] #Tag Objects, list of tag
