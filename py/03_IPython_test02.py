# -*- coding: utf-8 -*-
"""
03_IPython_test02.py
Created on Fri Jan  6 09:27:47 2017
@author: zzjack
"""
import sys
def myfun01(x,y,z):
    return x+y+z

if len(sys.argv) < 2: #len小於2也就是不帶參數啦
    print('執行此程式，需要三個參數')
    sys.exit()

#叫用function myfun01()
result=myfun01(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
print(result)    


