# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:24:46 2018
fs717_ch03_07_strSlice.py
@author: zzjack
"""
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

base+='目前庫存: '

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

#練習1: len('letters')
#練習2: 將字串倒轉為 "zyxwvuysrqponmlkjihgfedcba"

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