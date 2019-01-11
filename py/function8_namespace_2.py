# -*- coding: utf-8 -*-
#namespace and scope
#全域變數
#example1: 在函式中取得全域變數的值
animal='rabbit'  #全域變數 animal
def print_global():
    print('inside print_global:',animal) #在 function print_global()讀取全域變數 animal

print('at the top level:',animal) #在top level 中讀取animal
print_global() #叫用函式 print_global()

#example2: 如果你要在函式中取用全域變數並更改其值，你要明確使用global關鍵字。
def change_and_print_global2(): #定義函數
    global animal  #明確使用 keyword 'global'
    animal = 'cat' #在函式中用全域變數(global animal)並更改其值
    print('inside fuction, animal=',animal)
    
change_and_print_global2() #呼叫函數

print_global() #再次叫用函式 print_global(), animal 已指向 'cat' 物件

    



    