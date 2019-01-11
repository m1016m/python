# -*- coding: utf-8 -*-
#locals()-->回傳local namespace 的字典內容
#globals() -->回傳 globas namespace 的字典內容
#example:
animal='fruitbat' #global variable
def change_local(): #定義函式
    animal = 'wowbat' #local variable
    print('local',locals())
    
print('global',globals()) #回傳 globas namespace 的字典內容
change_local() #呼叫函式, 回傳local namespace 的字典內容