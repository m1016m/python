#web_scraping_04_20160709
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj=BeautifulSoup(html.read(),"lxml")
iii_html=urlopen("http://www.iiiedu.org.tw/south/")
iii_bsObj=BeautifulSoup(iii_html.read().decode(),"lxml")

#findAll() function
bsObj.findAll("h1") #從bsObj中，找出所有 <h1> tag
iii_bsObj.findAll("meta") #從iii_bsObj中,找出所有 <meta> tag              
                          #結果是list of tags

iii_bsObj.findAll("meta")[0:2] #切前面兩個元素
iii_bsObj

iii_bsObj.findAll("body")[0] #雖然 <body> tag 只有一個,但findALL() 回傳是list object
                             #故仍需以 list 存取方式存取

iii_bsObj.findAll("body")[0].findAll("a") #從<body> tag 中找出所有 <a> tag
                                          #回傳仍是 list of tags

iii_bsObj.findAll("body")[0].findAll("a")[0].findAll("img") #......

#example 2 :"http://www.pythonscraping.com/pages/warandpeace.html"
html2=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj2=BeautifulSoup(html2,"lxml") #將html2轉成BeautifulSoup 物件
bsObj2

namelist=bsObj2.findAll("span",{"class":"green"})
                       #所有 tag 為 span 且 Attribute class="green"  

namelist[0:2] #第一、二個元素
print(namelist[0].get_text()) #list namelist 第一個元素的內容
print(namelist[1].get_text()) #list namelist 第二個元素的內容

for name in namelist:       #印出namelist 每一個 tag 的內容
    print(name.get_text())

namelist2=bsObj2.findAll("span",{"class":"green","class":"red"})
                        # tag 為<span>, attribute class="green" or "red"   

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

