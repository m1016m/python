# -*- coding: utf-8 -*-
"""
web_scraping_ch05_03.py
Created on Fri Nov 11 09:46:01 2016

@author: zzjack
"""
import csv #import csv module
from urllib.request import urlopen
from bs4 import BeautifulSoup

#以urlopen() 開啟Wikipedia’s Comparison of Text Editors 
html=urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html,"lxml")
# type(bsObj.prettify()) #檢視 BeautifulSoup tree
#以 BeautifulSoup.findAll() 找出所有的 <table> tag (屬性class=wiketable)
# bsObj.findAll("table",{"class":"wikitable"}) #回傳是list of table tag

#The main comparison table 在findAll() 回傳list的第一個元素
table=bsObj.findAll("table",{"class":"wikitable"})[0] 
# print(table.prettify()) #檢視 

# find all <tr> tag in table
rows=table.findAll("tr") #list of tag <tr>

#-----------------------------------------------------------------------
#在現行目錄下,ch05FilesDir目錄內(需先建立),開啟'wt'模式的file 'editors.csv'
csvFile=open("ch05FilesDir/editors.csv","wt",newline='',encoding='utf-8')
writer=csv.writer(csvFile)
try:
    for row in rows:     #逐行處理rows (list of tag <tr>)
        csvRow=[]        #建一空串列csvRow
        for cell in row.findAll(['td','th']):  #以get_text()逐一取出 row 中 <th> or <td> 內容
            csvRow.append(cell.get_text())     #並append() 至list csvRow
        writer.writerow(csvRow)                #將csvRow寫至file
finally:
    csvFile.close()



