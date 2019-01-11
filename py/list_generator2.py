# -*- coding: utf-8 -*-
#將range()輸出轉成串列
numer_list=list(range(1,6))

print(numer_list) #test print
#-----------------------------
print('---------------------------------')
#使用for迭代器與range()函數
numer_list2=[]
for numer in range(1,6):
    numer_list2.append(numer)
    
print(numer_list2) #test print
#-------------------------------------------
print('-----------------------------------')
print('--串列生成式,[運算式 for 項目 in 可迭代項目--')
numer_list3=[numer for numer in range(1,6)]
print(numer_list3)
#----------------------------------------------------
print('------------------------------------')
print('--另一個串列生成式----')
numer_list4=[numer-1 for numer in range(1,6)]
print(numer_list4)
#----------------------------------------------------
print('---------------------------------------------')
print('--帶條件運算式的串列生成式--')
print('--[運算式 for 項目 in 可迭代項目 if 條件式]--')
a_list=[numer for numer in range(1,11) if numer%2==1] #1到10的奇數
print(a_list) #test print
#------------------------------------------------------------------
print('----------------------------------------------')
print('--1到10的奇數,原先寫法--')
b_list=[]
for number in range(1,11):
    if number % 2==1:
        b_list.append(number)
        
print(b_list) #test print
    
