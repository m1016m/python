# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:23:27 2018
fs717_ch05_01_function.py
@author: zzjack
"""
#define a function "fun01()
def fun01():
    print("我是fun01!")

#define a function "fun02()
def fun02():
    print("我是fun02!")
    
#呼叫 fun01()
print("第一次呼叫 fun01()")
fun01()

print("第二次呼叫 fun01()")
fun01()

#呼叫 fun02()
print("第一次呼叫fun02()")
fun02()
print("呼叫fun02() 5次")
for i in range(1,6):
    print("第",i,"次呼叫fun02")
    fun02()
    

