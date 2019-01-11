# coding: utf-8
#p3_example2, 可變物件與不可變物件
#不可變物件, 基本資料型別物件 (int, float, string), tuple 
12     # int 物件, 常數

'abc' #string 物件 

t1=(12,24,46) #tuple 物件

t1[0] #tuple t1 的第一個元素

t1[0]=120 #試圖更改 tuple t1 第一個元素的值, 失敗! tuple 是不可變物件 

#可變物件, 以 list 為例
list01=[12,24,36] #list object list01

list01[0] #list01 第一個元素值 

list01[0]=120 #指定 list01 第一個元素值為 120

list01 #display list01
