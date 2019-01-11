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
#
fout=open('relative','wt') #呼叫open(), filename:relative, t:文字, w:寫入
fout.write(poem) #將相對論打油詩寫到file relative
fout.close() #關閉檔案
#以記事本開啟file relative 驗證
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
#上例中,read()將一次取出整個檔案放在MM中,1GB的file就會用掉1GB的MM
#使用read(num),來限制每次回傳的數量為num
poem2='' #宣告一個空字串poem2
fin2=open('relative','rt') #file handler fin2, r:read
num=100 #設定每次讀取字數

while True:                  #每次讀100個字,加到poem2
    fragment = fin2.read(num)
    if not fragment:         #當讀到結尾read()會回傳空字串'',它會被視為False    
        break
    poem2+=fragment

fin2.close() #關閉檔案
print('分次讀取:')
print(poem2)
#
#-------------------------------------------------------------------------
#使用一個迭代器一次傳回一行,重作上例:
poem3=''
fin3=open('relative','rt')

for line in fin3:
    poem3+=line

fin3.close()

print('以迭代器逐行讀取:')
print(poem3)
#
#---------------------------------------------------------------------
#練習1: 將poem與poem2相加為 poem4, 將 poem4 寫至file relative2
#                  poem4=poem+poem2
#                  fout2=open('relative2','wt')
#                  fout2.write(poem4)
#                  fout2.close()

#練習2: 將 file relative2 逐行讀出到字串 poem6
#                  poem6=''
#                  fin6=open('relative2','rt')
#                  for line in fin6:
#                      poem6+=line
#                  fin6.close()
#                  print(poem6)




