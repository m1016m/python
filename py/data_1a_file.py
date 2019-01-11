#data_1a_file.py
#data storage: 1.flat file, 2.structured file, 3.database
#flat file, 一個byte序列, python處理file是以unix風格
#step1: 讀取或寫入file前,你必須先開啟它: fileobj=open(filename,mode)
#step2: 呼叫函數來讀取或寫入資料
#step3: 關閉檔案

#example:
poem='''There was a young lady named Bright,   
Whose speed was far faster then light;
She started one day
In a relative way,
And returned on the previous night.'''       #宣告一首相對論打油詩

print('相對論打油詩長度為:',len(poem)) 
#
#開啟(建立)file relative,並將poem寫入後關閉檔案,write()
#open(filename,mode), mode--> t:文字檔 / b:二進為檔 ; w:寫 / r:讀
fout=open('relative','wt') #呼叫open(), filename:relative, t:文字, w:寫入
fout.write(poem) #將相對論打油詩寫到file relative
fout.close() #關閉檔案
#以記事本開啟file relative 驗證, 或 !type relative
#-----------------------------------------------------------------------
#
#讀取文字檔,read(),readline(),readlines()
#read(),一次取出整個檔案
fin=open('relative','rt') #file handler 'fin', 開啟 relative
poem_r=fin.read()         #讀取整個relative file
fin.close()               #關閉檔案 
print('以下是測試結果:')
print(poem_r) #測試
#
#---------------------------------------------------------------
#用 with 來自動關閉檔案
ppapData='''I have a pen, I have a apple  Uh! Apple-Pen! 
I have a pen, I have pineapple Uh! Pineapple-Pen!'''

with open('pico','wt') as fout:
    fout.write(ppapData)
    
with open('pico','rt') as fin:
    pdata=fin.read()*3
    
print(pdata)    

#---------------------------------------------------------------------
#練習1: 將poem與ppapData相加為 poem4, 將 poem4 寫至file relative2
#                  poem4=poem+ppapData
#                  with open('relative2','wt') as fout2:
#                     fout2.write(poem4)


#練習2: 將 file relative2 逐行讀出到字串 poem6
#                  poem6=''
#
#                  with open('relative2','rt') as fin2:
#                     for line in fin2:
#                        poem6+=line
#
#                  print(poem6)




