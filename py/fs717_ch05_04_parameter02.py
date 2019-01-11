# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:28:40 2018
fs717_ch05_04_parameter02.py
@author: zzjack
"""
#function example 1: 位置引數
def menu(wine,entree,dessert):                        #定義 menu()函數
    return{'餐前酒':wine,'主菜':entree,'甜點':dessert} #回傳一個字典

#叫用menu函數,依位置
print('位置引數,叫用menu函數,依位置')
todays_menu=menu('Red wine','Steek','cake')
print(todays_menu)
print('-------------------------------------------------')

#叫用menu函數 2 , 位置不同
tomorrow_menu=menu('Steek','Red winw','cake')
print('位置不同時,牛排當酒,紅酒當正餐!')
print(tomorrow_menu)
print('-------------------------------------------------')

#--------------------------------------------------------------------------
#function example 2: 關鍵字引數
#叫用menu函數 3, 用引數的對應參數名稱來指定引數,就不怕位置錯亂
print('同樣是叫用menu(),用引數的對應參數名稱來指定引數,就不怕位置錯亂')
another_menu=menu(entree='牛排',wine='紅酒',dessert='小蛋糕')
print(another_menu)
print('--------------------------------------------------------')

#---------------------------------------------------------------------------
#function example 3: 指定預設參數值
def menu2(wine,entree,dessert='pudding'): #預設 dessert 為 'pudding'
    return{'餐前酒':wine,'主菜':entree,'甜點':dessert}

print('函數中有指定預設參數值')
a_menu=menu2('chardonnay','beef') #叫用menu2()時,只給兩個引數
print('叫用menu2()時,只給兩個引數')
print(a_menu)
print('叫用menu2()時,有給值則會蓋過預設值')
b_menu=menu2('chardonnay','beef','cake') #叫用menu2()時,有給值則會蓋過預設值
print(b_menu)
print('-----------------------------------------------------')

