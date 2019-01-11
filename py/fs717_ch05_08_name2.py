# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:00:34 2018
fs717_ch05_08_name2.py
@author: zzjack
"""
#另一個def範例:(函數中，參數為其他函數名稱並可指定參數給它)
print('函數中，參數為其他函數名稱並可指定參數給它,另一個範例: (a*a)+(b*b*b)')
def square(a): #定義平方函數 square(), 參數a
    return a*a

def cube(b): #定義立方函數 cube(), 參數b
    return b*b*b

def comp(fun1,fun2,arg1,arg2):     #定義計算函數comp,前兩個參數,fun1、fun2呼叫
    return fun1(arg1)+fun2(arg2)   #函數，並帶入參數arg1,arg2到使用的函數 

#呼叫函數comp 計算(4*4)+(3*3*3)
sum1=comp(square,cube,4,3) 
print('4*4+3*3*3=',sum1)  

#呼叫函數comp 計算(3*3)+(5*5*5)
sum1=comp(square,cube,3,5) 
print('3*3+5*5*5=',sum1)