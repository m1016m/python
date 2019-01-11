# -*- coding: utf-8 -*-
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

#---------------------------------------------------------------------------
#function example 4: 用*來收集位置引數
#當你在函數的參數使用*時，*會將可變數量的潛在引數群組化，變成一個參數值的tuple
print('用*來收集位置引數')

def print_args(*args):
    print('argument tuple:',args)
#呼叫 function print_args(),不給參數
print_args()
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
