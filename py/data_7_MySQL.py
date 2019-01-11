#example of mysql, by jack huang 2016.2.21 
#MySQL(http://www.mysql.com)
#與SQLite不同,他是一個伺服器
#MySQL驅動程式: 
#MySQL Connector/Python Developer Guide(http://dev.mysql.com/doc/connector-python/en/)
#Connector/Python Installation:(http://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)

#***
#conda 安裝: c:>conda install pymysql 
import pymysql #import module pymysql
#使用 connect() 連接到 MySQL, DB=test
conn=pymysql.connect(user='root', password='jack321', host='127.0.0.1',database='test')
curs=conn.cursor() #使用cursor()

#如果zoo已經建立,先將table drop 
curs.execute('DROP TABLE zoo')

#使用execute(),執行SQL DDL 指令, 建立 table zoo 
curs.execute('''CREATE TABLE zoo 
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damages FLOAT)''')

#insert 
curs.execute('INSERT INTO zoo VALUES("duck",5,0.0)')
curs.execute('INSERT INTO zoo VALUES("bear",2,1000.0)') 
curs.execute('INSERT INTO zoo VALUES("weasel",1,2000.0)')

#*******************************************************************
#實際寫入資料庫 connect.commit(),mysql不會auto commit 必須強制 commit
conn.commit()

#select
curs.execute('SELECT * FROM zoo')
rows=curs.fetchall() #使用 fetchall() 從cursor中取出資料
print(rows) #print rows

#select, order by count
curs.execute('SELECT * FROM zoo ORDER BY count')
print(curs.fetchall())

#select, order by count desc
curs.execute('SELECT * FROM zoo ORDER BY count DESC')
print(curs.fetchall()) 

#select, 子查詢
curs.execute('''SELECT * FROM zoo WHERE
damages = (SELECT MAX(damages) FROM zoo)''')
print(curs.fetchall())

curs.close() #結束 cursor
conn.close() #結束 connection



