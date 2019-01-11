# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:39:43 2018
fs717_ch05_05_parameter03.py
@author: zzjack
"""
#function example 4: 用*來收集位置引數 (arbitrary argument list)
#當你在函數的參數使用*時，*會將可變數量的潛在引數群組化，變成一個參數值的tuple
print('用*來收集位置引數')

def print_args(*args):
    print('argument tuple:',args)
#呼叫 function print_args(),不給參數
print_args()    #列印出 () , empty tuple
#呼叫 function print_args(),給定一些參數
print_args(3,4,5)
#呼叫 function print_args(),給定多一些參數
print_args(3,4,5,'a','b')
print('--------------------------------------------------------')

#---------------------------------------------------------------------------
#function example 5: 用*來收集位置引數
#當你在函數的參數使用*時，*會將可變數量的潛在引數群組化，變成一個參數值的tuple
#如果函數需要用到位置引數,就把 *arg 放在最後,抓取剩下的引數
print('#如果函數需要用到位置引數,就把 *arg 放在最後,抓取剩下的引數')

def print_args_2(name,age,*args):
    print('姓名:',name,'年齡:',age,'其他引數 tuple:',args)
#呼叫 function print_args(),只給指定位置參數
print_args_2('Jack',30)
#呼叫 function print_args(),除了指定位置參數,可給不定數量的其他引數
print_args_2('Jack',30,'A','Kaohsiung',100)
#呼叫 function print_args(),除了指定位置參數,給更多數量的其他引數
print_args_2('mary',28,'B','Kaohsiung',99,'school','NCU')
print('--------------------------------------------------------')

#---------------------------------------------------------------------------
#function example 6:用**來收集關鍵字引數
#用**來將關鍵字引數群組化，變成一個字典
print('用**來將關鍵字引數群組化，變成一個字典')
def print_kwargs(**kwargs):
    print('keyword arguments:',kwargs)

print_kwargs() #呼叫 print_kwargs(),不給參數
#呼叫 print_kwargs(), 給定的參數形式--> k=v
print_kwargs(wine='Red wine',entree='beef',dessert='cake')
#再次呼叫 print_kwargs()
print_kwargs(a=100,b=200,c=300,d=400)
print('--------------------------------------------')

#-------------------------------------------------------------------------
#文件字串
#函數定義中可加入說明字串
print('函數定義中可加入說明字串')
def echo(anything):
    ''' 說明也
        可以是很長
        !
    '''
    return anything

ec=echo('Hello') #呼叫echo()
print(ec)

help(echo) #印出函數的說明字串
