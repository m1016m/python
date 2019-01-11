# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:13:29 2018
fs717_ch05_06_localVar.py
@author: zzjack
"""
#global variable x,y
x=0;y=0
#定義 fun01()
def fun01():
    x=10   #local variable x
    print(x)
#定義 fun02(p)
def fun02(p):
    global y   #不可同時指派值
    y=p
    print(y)
#===============================    
#叫用fun01()
print("叫用fun01()")
fun01()
#檢視 global variabel x
print("檢視 global variabel x")
print(x)

#叫用fun02()
print("叫用fun02()")
fun02(24)
#檢視 global variabel y
print("檢視 global variabel y")
print(y)