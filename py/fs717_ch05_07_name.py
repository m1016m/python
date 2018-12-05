# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:54:56 2018
fs717_ch05_07_name.py
@author: zzjack
"""
#將函數名稱當作參數傳遞
#定義兩個個簡單函數--> answer(), answer2()
def answer(): #定義第一個簡單的函數 answer()
    print('I am answer')
    
def answer2(): #定義第二個簡單的函數 answer2()
    print('I am answer2')
    
def run_another_fun(func): #定義另一個函數run_another_fun(),參數是函數的名稱
    func()
    func()   #執行兩次

run_another_fun(answer) #呼叫函數run_another_fun(), 參數以 answer 這個函數名稱帶入
                        #注意是帶入 answer, 不是answer()
                        #不使用(),Python就將函數視為物件

run_another_fun(answer2) #呼叫函數run_another_fun(), 參數以 answer2 這個函數名稱帶入
                         #注意是帶入 answer2, 不是answer()

def run_another_fun2(func1,func2): #定義函數 run_another_fun2(),依位置引數(函數名稱),呼叫函數執行
    func1()
    func2()
    func2()
    
run_another_fun2(answer,answer2) # #呼叫函數run_another_fun2(), 參數以answer,answer2 這兩個函數名稱帶入

