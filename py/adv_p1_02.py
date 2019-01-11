# -*- coding: utf-8 -*-
"""
adv_p1_02.py
@author: III
"""
#可變與不可變物件
list01=[2,4,6,8,10] #list object 'list01',是可變物件
tuple01=(2,4,6,8,10) #tuple object 'tuple01',是不可變物件

list01[2] #取 list 'list01' 的第3個元素
tuple01[2] #取 tuple 'tuple01' 的第3個元素

list01[2] = 60 #將 'list01' 第3個元素值設為 60
               #-->list01[2] 指向 int object 60
list01 #display list 'list01'
#-------------------------------------------------------
tuple01[2] = 60 #TypeError: 'tuple' object does not support item assignment
                #tuple01[2] 是終端節點, 物件本身