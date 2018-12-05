# -*- coding: utf-8 -*-
"""
data_2_structuredfile_csv2.py
"""
#http://new.cpc.com.tw/division/mb/oil-more4.aspx
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://new.cpc.com.tw/division/mb/oil-more4.aspx")
bsObj = BeautifulSoup(html,'lxml')
#The main comparison table is currently the first table on the page
table = bsObj.findAll("table",{"summary":re.compile("牌價")})[0]
rows = table.findAll("tr")

#csvFile = open("price.csv", 'wt',newline='',encoding='utf-8')
csvFile = open("price.csv", 'wt')
writer = csv.writer(csvFile)
        
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()        

