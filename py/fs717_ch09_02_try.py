# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:36:50 2018
fs717_ch09_02_try.py
@author: zzjack
"""
#計算圓形面積
#定義常數 PI,或使用 math.pi
import math,sys

#輸入, 將有可能發生例外的部分"包起來"
try:
    r=eval(input("請輸入圓半徑 (數值,cm):"))
except NameError:
    print("別鬧了,請輸入數值")
    sys.exit(0) #終止 python script 程式執行

#計算
area=math.pi*r*r
#輸出 格式化輸出 
print("半徑: {0:<10} --> 面積: {1:10.2f}".format(r,area))
