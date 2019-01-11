# -*- coding: utf-8 -*-
"""
data_7_MySQL_4.py
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re
conn=pymysql.connect(user='root', password='jack321', host='127.0.0.1',
                     database='mysql',charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())

#defined function store()
def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")",
                (title, content))
    cur.connection.commit()
    
#defined function getLinks()
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,'lxml')
    title = bsObj.find("h1").find("span").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((?!:).)*$"))
#以"/wiki/Kevin_Bacon" 為引數 呼叫 getLink() function
links = getLinks("/wiki/Kevin_Bacon")

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
