#在open()中,mode為'b',檔案將以二進位模式開啟,此時讀取與寫入為byte ('t'為字串)
#example:
bin_data=bytes(range(0,256)) #產生256byte的值
len(bin_data)

#開啟檔案,以二進位模式,一次寫入所有資料:
fout=open('bin_file','wb') #step1: open()
fout.write(bin_data)       #step2: write()
fout.close()               #step3: close()
#
#也可以分段寫入二進位資料
fout2=open('bin_file_2','wb') #file bin_file_2,以二進位寫入
size=len(bin_data) #
offset =0
num2=100

while True:
    if offset > size:
        break
    fout2.write(bin_data[offset:offset+num2])
    offset+=num2  

fout2.close()
#--------------------------------------------------------
#
#用read()來讀取二進位檔案
fin2=open('bin_file_2','rb') #r:read, b:binary
bin_data_2=fin2.read() 
print(bin_data_2) #test
fin2.close()

#--------------------------------------------------------
#用with來自動關閉檔案
#Python具有 context managers
poem8=''
with open('relative2','rt') as fin3:
    poem8=fin3.read()
    print(poem8)
    
#-------------------------------------------------------
#seek(),更改位置--->未完待續...(2016/2/11)
        

