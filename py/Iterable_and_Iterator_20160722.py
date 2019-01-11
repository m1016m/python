# coding: utf-8
#Iterable(可迭代者) and Iterator(迭代器) 
from collections.abc import * #Sequence, MutableSequence, Iterable
                              #等抽象類別被放在 collections.abc module
li=[0,1,2,3] #list li
tu=(2,5) #tuple tu

type(li) 
isinstance(li,list) #li object 是一個 list class 的 instance
isinstance(li,MutableSequence) #li 也是MutableSequence 的 instance,
                               #MutableSequence-->可變Sequence
                               #MutableSequence繼承Sequence
isinstance(li,Sequence) #li 也是 Sequence 的 instance,
                        #因為list 繼承自Sequence
isinstance(tu,tuple) #tu 是 tuple 的一個instance
isinstance(tu,Sequence) #tu 也是 Sequence
isinstance(tu,MutableSequence) #tu 不是 MutableSequence
                               #tuple 不可變

#Iterable(可迭代者) 與 Iterator(迭代器)
isinstance(li,Iterable) #li, list 物件 也是 Iterable(可迭代者)
isinstance(li,Iterator) #但Li不是 Iterator(迭代器)

lit01=iter(li) #以內建函數iter(),將list li 轉為 list_iterator(串列迭代器)
type(lit01)
isinstance(lit01,Iterator) #lit01 是 Iterator 的一個 instance

next(lit01)
next(lit01)
next(lit01)
next(lit01)

next(lit01) #已到迭代器的最後

tit01=iter(tu) #將tuple tu 轉為 tuple_iterator
type(tit01)
next(tit01) #Python2.x -->tit01.next()



