#module_8_stdlib_itertools.py 2016.4.18
#使用 itertools 來迭代程式結構, 這個模組提供許多特殊的迭代函數,當你使用for...in迴圈
#呼叫它們時,他們會一次回傳一個項目,並記得每次呼叫間的狀態。
#itertools — Functions creating iterators for efficient looping 
#https://docs.python.org/3/library/itertools.html?highlight=itertools#module-itertools
#以下介紹itertools的幾個函數: chain(), cycle(), accumulate(),

import itertools #import itertools 標準模組
#chain(), 逐一經過引數,就像它們是可迭代的單一項目
for item in itertools.chain([1,2,3],['a','b'],[45,56]):  #將三個串列chain起來
    print(item)
# 1
# 2
# 3
# a
# b
# 45
# 56

#----------------------------------------------------------------------------
#cycle(), 無限迭代器,請小心!
#for item in itertools.cycle([1,2]):
#    print(item)

#-----------------------------------------------------------------------------
#accumulate()會計算累加的值
for item in itertools.accumulate([1,2,3,4]):
    print(item)
#結果:
#     1
#     3
#     6
#    10

#accumulate() 範例2,在accumulate()的第二個引數提供一個函數
import itertools
def multiply(a,b): #定義一個function, multiple(a,b)
    return a*b

for item in itertools.accumulate([1,2,3,4],multiply): #第二個引數,multiply
    print(item)
    
# 1  
# 2    <--  1*2
# 6    <--  2*3
# 24   <--  6*4
