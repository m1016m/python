# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:13:53 2018
fs717_ch09_01_noTry.py
@author: zzjack
"""
#計算圓形面積
#定義常數 PI,或使用 math.pi
import math

#輸入
r=eval(input("請輸入圓半徑 (數值,cm):"))
#計算
area=math.pi*r*r
#輸出 格式化輸出 
print("半徑: {0:<10} --> 面積: {1:10.2f}".format(r,area))

