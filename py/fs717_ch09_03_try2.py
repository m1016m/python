# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:08:44 2018
fs717_ch09_03_try2.py
@author: zzjack
"""
#計算圓形面積
#定義常數 PI,或使用 math.pi
import math,sys

#輸入
try:
    r=eval(input("請輸入圓半徑 (數值,cm):"))

except NameError:
    print("別鬧了,請輸入數值")
    sys.exit(0)
except Exception as e1: #捕捉其他類型 Exception
    print(e1.args)

#計算
area=math.pi*r*r
#輸出 格式化輸出 
print("半徑: {0:<10} --> 面積: {1:10.2f}".format(r,area))
