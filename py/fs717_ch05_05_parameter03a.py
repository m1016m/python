# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:53:22 2018
fs717_ch05_05_parameter03a.py
@author: zzjack
"""
#定義函數 sum_all(), 使用任意引數串列(arbitrary argument list)
def sum_all(*numbers):    #numbers is a tuple
    sumAll=0
    for i in numbers:
        sumAll+=i
    return sumAll
    
#叫用 function sum_all()
sum_all()

sum_all(2,3)

sum_all(2,3,5,9)    
