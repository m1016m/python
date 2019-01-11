# -*- coding: utf-8 -*-
#產生器(generator)
#是一種python序列建立物件
#產生器通常是迭代器的資料來源
#python 2 --> xrange(), python 3 --> range()

#example 1: generator--> range(), iterator --> sum()
print('將1+2+3+...+99+100, sum(range(1,101)=',sum(range(1,101))) 

#自訂產生器函數，一種一般函數，用yield來回傳值而不是return
#example 2: 自訂產生器函數 my_range()
def my_range(first=0,last=10,step=1):
    number=first
    while number < last:
        yield number
        number += step

myrange=my_range(1,6) #此函數會回傳一個產生器物件 (myrange):

for x in myrange: #用for來迭代此產生器物件
    print(x)

#my_range
#Out[9]: <function __main__.my_range>

#myrange
#Out[10]: <generator object my_range at 0x000000000A609CA8>



#----------------------------------------------------------
#如果只是一般標準產生器range()
print('--如果只是一般標準產生器range()--')
for y in range(1,6,1):
    print(y)
