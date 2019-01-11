# -*- coding: utf-8 -*-
"""
adv_p1_04.py, Iterables vs. Iterators vs. Generators
@author: III
"""
#----------------string------------------------
str01='abcdef' #string str01 是 Iterable
for s in str01: #以 for 做迭代處理
    print(s)
#-----------------list-------------------------
list01=[2,4,6,8,10] #list list01 是 Iterable
for l in list01: #以 for 做迭代處理
    print(l*10)
#----------------dict.-------------------------
dict01={'a':100,'b':200,'c':300}
for dk in dict01.keys():
    print(dk)

for dv in dict01.values():
    print(dv+10)
    
for dk,dv in dict01.items():
    print('key=' +dk +', value='+str(dv))
#---------------range()-----------------------
for r in range(10,21): #range() 可以用 for 迭代處理
    print(r)

type(range(10,21)) #range, 序列產生器, Iterator 

range(10,21) #序列產生器，直接使用無意義!   
    
    
    
    
    
    
    
    
    