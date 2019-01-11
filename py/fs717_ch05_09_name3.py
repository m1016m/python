# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:18:41 2018
fs717_ch05_09_name3.py
@author: zzjack
"""
#----將上述函數參數方法結合 *args或 **kwargs, 可取用任意數量參數
print('將上述函數參數方法結合 *args或 **kwargs, 可取用任意數量參數')
def sum_args(*args): #*args:任意個數的引述 
    return sum(args) #sum() 是系統內建含數

sum2=sum_args(1,2,3,4,5) #測試函數sum_args(),用5個參數
print('sum2=',sum2)

sum3=sum_args(1,2,3,4,5,6,7,8,9,10) #再次測試函數sum_args(),用10個參數
print('sum3=',sum3)    

#-----------------------------------------------------------------
#--函數的參數中包含一個函數名稱及任意個數參數--
print('--函數的參數中包含一個函數名稱及任意個數參數--')
def ret_with_pos_args(func,*args): #定義函數ret_with_pos_args()
    return func(*args)

sum4=ret_with_pos_args(sum_args,1,2,3,4,5) #呼叫函數ret_pos_args
print('sum4=',sum4)                        #帶入的第一個參數(函數名稱)
                                           #是我們在上面定義的 sum_args()
                                           #其後任易個數的參數,是sumargs()的參數
