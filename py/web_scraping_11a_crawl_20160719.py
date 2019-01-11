# -*- coding: utf-8 -*-
"""
web_scraping_11a_crawl_20160719.py
Created on Wed Jun 14 10:39:46 2017
@author: III
"""
# A single function, getLinks, that takes in a Wikipedia article URL of the form
# /wiki/<Article_Name> and returns a list of all linked article URLs in the same form.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime #import datetime module (std. library)
import random #import random module (std. library)
import re #import re module (regular expresssions) 

#random.seed(datetime.datetime.now()) #seed(), Initialize the random number generator

#defined function getLinks() with argument 'articleUrl'
def getLinks(articleUrl):            #defined function getLinks() with argument 'articleUrl'
    html=urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj=BeautifulSoup(html,"lxml")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#回傳的是一個list(list of tag <a>)

arg=input("請輸入一個目標字串(e.g. Wu_Nien-jen):")
arg="/wiki/"+arg
#以"/wiki/+input string",叫用 getLinks()函數
links=getLinks(arg) #called getLinks, argument="/wiki/Kevin_Bacon",links是一個list of tag
while len(links) > 0:  #只要list links 有值
    newArticle=links[len(links)-1].attrs["href"]
    print(newArticle)
    links=getLinks(newArticle)