# -*- coding: utf-8 -*-
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

#--------------------------------------------------------------------------------
#另一個範def例:(函數中，參數為其他函數名稱並可指定參數給它)
print('---------------------------------------------------------------')
print('函數中，參數為其他函數名稱並可指定參數給它,另一個範例: (a*a)+(b*b*b)')
def square(a): #定義平方函數 square(), 參數a
    return a*a

def cube(b): #定義立方函數 cube(), 參數b
    return b*b*b

def comp(fun1,fun2,arg1,arg2):     #定義計算函數comp,前兩個參數,fun1、fun2呼叫
    return fun1(arg1)+fun2(arg2)   #函數，並帶入參數arg1,arg2到使用的函數 

sum1=comp(square,cube,4,3) #呼叫函數comp 計算(4*4)+(3*3*3)
print('4*4+3*3*3=',sum1)  
print('--------------------------------------------------------------')

#---------------------------------------------------------------------------
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
        
#-----------------------------------------------------------------------
#--內部函數-->在其他函數的裡面定義函數--
print('-------------------------------------------------------------')
print('--內部函數-->在其他函數的裡面定義函數--')       
def outer(x,y):       #定義外部函數 outer(x,y)
    def inner(a,b):   #在outer內,定義函數 inner(a,b)
        return 2*(a+b)
    return inner(x,y) #outer函數定義中,使用內部定義的函數 inner()
    
print('叫用outer(4,7)')
r2=outer(4,7)
print('r2=',r2) 

#-------------------------------------------------------
#--內部函數範例:將文字附加到它的引數:--
print('---------------------------------------------------')
print('--內部函數範例:將文字附加到它的引數:--')
def king(saying):        #定義函數 king(saying)  
    def inner(quote):        #定義內部函數 inner()
        return "I am the king who say: '%s'" % quote
    return inner(saying) # king()中,叫用inner()
print('叫用king()')
king('Hello!') 

#-------------------------------------------------------------
#--Closure,一種由其他的函數動態生成的函數
#--由內部函數構成
#--closure可以更改或記得函數之外的程式所建立的變數的值
print('-------------------------------------------------')
print('--Closuer 範例: 改寫函數 king()--')
def king2(saying):  #重新定義函數king()為king2()
    def inner2():      #重新定義內部函數inner()為inner2()
        return "I am the king who say: '%s'" % saying #在inner2()中,直接引用saying
    return inner2   #回傳這個專用的inner2函數複本(而不是呼叫它),這是一個closure,
                    #一個被動態建立出來,會記得自己來自哪裡的函數

print('用不同引數呼叫king2()兩次:')
a=king2('First!')
b=king2('Second!!')

#檢視 a,b; 它們是函數,也是closure
type(a) #檢視 a --> function
type(b) #檢視 b --> function 

a # <function __main__.inner2>
b # <function __main__.inner2>

#呼叫 a(),b(), 他們會記得自己被king2()建立時所使用的saying
print(a()) # "I am the king who say: 'First!'"
print(b()) # "I am the king who say: 'Second!!'"
 