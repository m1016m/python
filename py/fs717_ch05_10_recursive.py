# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:28:08 2018
fs717_ch05_10_recursive.py
@author: zzjack
"""
#階乘函數 F(n)
def F(n):
    if n==0:
        return 1
    elif n>0:
        return n*F(n-1)
    else:
        return -1
        
#叫用階乘函數
print("0!=",F(0))
print("10!=",F(10))
print("5!=",F(5))        
