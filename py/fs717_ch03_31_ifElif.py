# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 12:25:33 2018
fs717_ch03_31_ifElif.py
@author: zzjack
"""
while True:
    try:
        #輸入
        age=eval(input("請誠實的輸入年齡:"))
        #if ... elif ..else 判斷流程
        if age >= 18:
            print("今年 {0:<5} 歲, 可以看限制級!".format(age))
        elif age >=12:
            print("今年 {0:<5} 歲, 只能看輔導級!".format(age))
        else:
            print("今年 {0:<5} 歲, 請看東森幼幼台!".format(age))
    except Exception :
        break

print("請不要亂填資料!")
