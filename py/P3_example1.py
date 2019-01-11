# coding: utf-8
#P3_example1
a=7 #變數名稱 a 指向整數物件 7, 整數物件是不可變 

print(a) #列印 a 所指向的 int 物件 7

b=a #將變數名稱 b 指向名稱 a 所指的物件 (int 7)  

print(b) #列印名稱(變數) b 所指 的物件 (int 7) 

type(a) #名稱 a 所指向的物件 (int 7) 資料型別 (data type) 為 int

type(b) #名稱 b 與 a 指向同一物件 (int 7),資料型別亦為 int

a=11 #變數 a 移情別戀指向 int 11

print('a=',a,'b=',b) #b 仍指向 int 7, a 指向 int 11

#練習1: b=14 #如果 b 也移情別戀 轉指向 int 14, int物件 7 會怎樣?

type(11) #物件 int 11 的data type 當然是 int

type(99.9) #物件 99.9 的data type 為 float

type('abc') #物件 'abc' 的data type 為 string

#數字物件
#整數
5
0

05 #0不可以放在其他數字前面

123

+123

-123

5+9

100-7

4-6

5+9+7

4+3-2+5

6*7

6*7*2*2

#除法, 分辨 /, //, %

9/5 # / 浮點數除法

9//5 # // 整數除法

9%5 # % mod, 取餘數

# 5/0, 5//0, 5%0 除以零例外

#上述皆為常數運算,以下為變數與常數運算式

a=95

a-3

a #變數 a 所指向的物件 int 95 並未改變

a=a-3 #取出 a 的值(95) - 3 = 92, 指定給 a

a

a+=2 #a=a+2

a

#練習: a=a*2,      --> a*=2

9%5 #取餘數

divmod(9,5) #dimmod() 函數, 同時取得商及餘數, 
            #結果是一個 tuple object

type(divmod(9,5)) #結果是一個 tuple object

#運算優先順序

2+3*4

(2+3)*4

#基數

10 #十進位, 預設

0b1000 #二進位 0b or 0B

0o11 #八進位 0o

0x11 #16進位 0x

#類型轉換
#將其他Python Data type 轉成整數--> int() function, 
#保留整數,捨棄小數

int(True) #布林轉int True-->1, False--0,

int(98.99) #float 轉 int ,只取整數部分

int(1.0e4)

int('234') #只含數字的字串,可以轉成數值

int('+234')

int('-234') #轉成負數

int('123a') #不可以, 字串裡包含不是數字

int('196.3') #不可以, 比較 int(196.3) ,可以 

#練習: int('0123') #是否可以?

4+7.0 #Python 會自動型別轉換

a=4+7.0 #變數 a 指向右式結果

type(a)

type(4+7.0)

#int 有多大?

google=10**100

google

12+True #將boolean值 True 轉成 int 1

#浮點數 ,float()

float(True) #將布林值轉為 float, float() function

float(12) #將int 12 轉為 float

float('12.02') #這樣ok, 字串 '12.02'

float('12.0a') #還是不可以

#字串, str object 是不可變物件

'Snap' #可以用單引號

"雙引號" #雙引號也可以

"'Nay,'said the naysayer." 

'A "two by four" is'

#’’’ ’’’,””” ”””, 三個單引號或雙引號建立多行字串

poem='''There was a Youg Lady of Norway,
        who casually sat in a doorway;
        when the door squeezed her flat
        She exclaimed,"What of that?"
        This courageous Youg Lady of Norway.'''

poem

print(poem) #print()的輸出與 python 直譯器自動回應不同

'' #空字串

""

''''''

""""""

#example of string

bottles=99 

base='' #變數名稱 base 指向一個空字串物件

base+='current inventory: '

base+=str(bottles) #str() 函數將bottles所指的 int 99
                   #轉成 '99'

base #display base

#str(),將其他Python資料類型轉成字串 

str(99.8) #str() 將 float 轉成 string

str(True) #將布林轉成 string

#逸出字元 (escape) \

ppop='I have an Apple,\nI have a pen,\nUn! \nApplePen!' #\n newline

print(ppop)

print('\tApple,\tPen,\tApplePen') #\t tab

#Escape character, 逸出字元 \

print('\', \", \\ ') # ', ", \ 

#字串運算, 用+來結合

'I have a pen, '+'I have an apple' #使用 +

"I have a pen, " "I have an apple" #這樣也可以

a='piko'

c='太郎!'

a+c

print(a,c)

#字串運算, 用*來複製

str1='新聞,'

str2='哇!  '

str3=str1+str2*3

print(str3)

str4=(str1+str2*3+'\n')*3

print(str4)

#用[]來擷取字元 

letters='abcdefghijklmnopqrsyuvwxyz'

letters[0] #第一個元素, 位移值(offset)為0

letters[1] #第二個元素, 位移值(offset)為1

letters[-1] #最後一個元素, 位移值(offset)為-1

letters[-3] #倒數第三個元素, 位移值(offset)為-3

letters[100] #超過字串長度 NG

#字串是不可變的物件

name='Henny'

name[0]

name[0]='P' #字串是不可變的, NG

name.replace('H','P') #用replace() 產生一個新字串,
                      #name所指物件仍然未變

name #name所指物件仍然未變

'P'+name[1:] #產生一個新字串, Slice [開始:結束:間隔] 

name #name所指物件仍然未變

#字串 Slice [start:end:step] 

letters='abcdefghijklmnopqrstuvwxyz'

letters[:] #[:] 擷取整個序列

letters[2:] #從第三個(c) 到最後

letters[:24] #從開始到end (24) 減一

letters[2:24]  #從第三個(c) 到end (24) 減一

letters[2:24:2] #step 為 2

letters[2:-2] #倒數第二個(y)止

letters[::2] #step 為 2

#len() 取得字串長度

len(letters)

#練習: len('letters')

len(letters[2:-1:2])

#split() method, 是str object 的 method

todos='關緊 門窗,堆 沙包,去 全聯採購,開 車'

todo_list=todos.split(',') #split(), 使用','當分隔字元,return a list

todo_list

todo_list[0] #list 是一個sequence物件

todo_list[0:2] #slice 可以用

len(todo_list) #len() 可以用

#join method() ,將字串串列結合成字串

todos2=''.join(todo_list) #''空字串.join() 

todos2




