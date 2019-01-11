# -*- coding: utf-8 -*-
"""
web_scraping_ch05_04.py
Created on Fri Nov 11 14:57:23 2016

@author: zzjack
"""
import pymysql #import pymysql module
conn=pymysql.connect(host='127.0.0.1',user='root',password='jack321',db='world') #建立connection object, conn
cur=conn.cursor() #建立 cursor object cur

#執行SQL指令
cur.execute("USE world")
cur.execute("SELECT * FROM city ORDER BY Name limit 3")

#取得cursor 內容, cur.fetchall()並 print
for c in cur.fetchall():
    print(c)
    
cur.close()   #關閉cursor
conn.close()  #關閉連線

