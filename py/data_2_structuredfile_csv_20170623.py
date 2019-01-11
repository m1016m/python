#結構化檔案,CSV
#使用標準(Python)csv模組
#1.分隔符號可能是: ',', '|', 'tab(\t)'
#2.資料內容有分隔符號,Escape處理
#3.分行字元(行尾字元): Unix--> '\n', Microsoft--> '\r \n', Apple --> '\n'
#4.第一行可能會是欄位名稱
#example1:
import csv #import csv模組
fin=open('2016072630_process.csv','r') #open csv file
for row in csv.reader(fin): #逐行讀取 csv file 並列印
    print(row)  
fin.close()

#------------------------------------------------------------------------------------
#example2: csv.csv.DictReader()
fin2=open('2016072630_process.csv','r')
for row in csv.DictReader(fin2):  #把資料parsing成dictionary的格式(csv.DictReader())，
    print(row['成交金額'])        #使用第一列當作dictionary的key。 
fin2.close()

#------------------------------------------------------------------------------------
#example3: 將list 資料寫入csv file
add_data=[['6883','精工','82','3','2,032','24.8','24.8','1,803','25.15','1,461'],
          ['6888','花王','82','3','2,032','24.8','24.8','1,803','25.15','1,461'],]

fout=open('2016072630_process.csv','a') #以a,appending to the end of the file if it exists
w=csv.writer(fout) #csv.writer
w.writerows(add_data) #writerows(多行),writerow(單行)
fout.close()





