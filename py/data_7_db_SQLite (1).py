#DB-API (http://bit.ly/db-api) 是Python的標準API,功用是存取關聯式資料庫。
#使用DB-API,你只要編寫一個程式就可以使用各式各樣的RDB,而不需為每一個資料庫個別編寫程式。
#它的主要函式有:
#1.connect(): 連結到DB,可以傳入帳號、密碼、伺服器地址等引數。
#2.cursor(): 建立一個cursor物件。
#3.execute(), executemany(): 對DB執行一個或多個SQL指令。
#4.fetchone(), fetchmanny(), fetchall(): 取得execute的結果。

#SQLite (http://www.sqlite.org)
# --是Python標準程式庫,並將資料庫存在一般的檔案裡。
# --step1: 用connect() 連結要使用或建立的local SQLite資料庫檔案
# --       (特殊字串 ':memory:',只會在記憶體中建立資料庫)
# --step2: 建立資料庫--> enterprise.db, 在資料庫中建資料表 zoo
import sqlite3 #import standard liberary sqlite3
conn=sqlite3.connect('enterprise.db') #使用connect() 建立或使用DB enterprise.db
curs=conn.cursor() #使用cursor()

#使用execute(),執行SQL DDL 指令, 建立 table zoo 
curs.execute('''CREATE TABLE zoo 
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damages FLOAT)''')

#insert 
curs.execute('INSERT INTO zoo VALUES("duck",5,0.0)')
curs.execute('INSERT INTO zoo VALUES("bear",2,1000.0)') 
#另一種 insert 的方法:(可防止 SQL injection)
ins_string='INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)'
curs.execute(ins_string, ('weasel',1,2000.0))

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

