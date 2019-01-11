# -*- coding: utf-8 -*-
#namespace and scope
#全域變數
#example1: 在函式中取得全域變數的值
animal='rabbit'  #全域變數 animal
def print_global():
    print('inside print_global:',animal) #在 function print_global()讀取全域變數 animal

print('at the top level:',animal) #在top level 中讀取animal
print_global() #叫用函式 print_global()

#example2: 但是，如果你要在函式中取用全域變數並更改其值，你會得到一個錯誤。
def change_and_print_global(): #定義函式
    print('insdie change_and_print_global:',animal) #
    animal = 'cat' #不可以,在函式中更改全域變數值
    print('after the change:',animal)
    
change_and_print_global() #叫用函式

#example3: 如果我們是在函式中重新命名一個animal變數
def change_and_print_local(): #定義函式
    animal = 'dog'
    print('print animal=',animal)

change_and_print_local()
    