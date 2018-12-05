#coding: utf-8
#web_scraping_05_20160715.py, Navigating Trees
#以 page "http://www.pythonscraping.com/pages/page3.html"
#在HTML tree 中,不僅是只能向下單一方向巡航(navigation),也可以向左右、向上

from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page3.html") 
bsObj=BeautifulSoup(html,"lxml") #轉成html tree

print(bsObj.prettify())

#navigating a BeautifulSoup tree in a single direction:
#example 1: single direction, bsObj.tag.SubTag.anotherTag 
bsObj.html.body.div.h1 #<h1>Totally Normal Gifts</h1>

bsObj.body.table.tr
print(bsObj.body.table.tr.prettify()) #排漂亮
#---------------------------------------------------------------
#處理子代(children)及子孫代(descendants)
#BeautifulSoup 預設是處理 descendants
bsObj.body.h1 #selects the first h1 tag that is a
              #descendant of the body tag.


bsObj.div.findAll("img") #find the first div tag in the document,
                         #then retrieve a list of all img tags 
                         #that are descendants of that div tag.

#如果你只要處理子代,-->使用 childred method 
count=0 #設一個計數器, 因為 .children 是產生器,無法直接計數
for c in bsObj.find("table",{"id":"giftList"}).children: #.children
    print(c) 
    count+=1
print('子代數為:',count)

#如果是子孫代(包含子代):
count=0
for c2 in bsObj.find("table",{"id":"giftList"}).descendants: #.descendants
    print(c2)
    count+=1
print('子孫代數為:',count)

#----------------------------------------------------------------
#處理平輩節點(siblings) --> netxt_siblings method,
#.next_siblings 不包含 object 本身, 所以第一個 <tr><th>Item Title... 不包含 
count=0 #設一個計數器
for s in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(s)
    count+=1
print('平輩數為:',count)

#------------------------------------------------------------------------------
#處理親代節點(parents)

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

#分解動作:
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}))

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent)

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling)

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())




