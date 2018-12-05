# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:33:32 2018
p3_example20_seqFun.py
@author: zzjack
"""
#1. enumerate
#when iterating over a sequence to want to keep track of the index of the
#current item. (追蹤sequence物件的index)

list98=['apple','orange','grape','pear']

for i,fruit in enumerate(list98):
    print(i,fruit)
    
#=========================================================================    
#2. sorted
#returns a new sorted list from the elements of any sequence
list98=['apple','orange','grape','pear']
s_list=sorted(list98)
rs_list=sorted(list98,reverse=True)
ls_list=sorted(list98,key=len,reverse=True)

list98
s_list
rs_list
#注意! 不管排序什麼, sorted() 都回傳 list
sorted(('bbb','aaa','ccc'))
sorted('when i was youg')

#========================================================================
#3. zip
#“pairs” up the elements of a number of lists, tuples, or other sequences to create a
#list of tuples
list98=['apple','orange','grape','pear']
for i,f in zip(range(100,104),list98):
    print("編號:{0:<5} 水果:{1:<20}".format(i,f))
    
list97=['cake','pudding','chocolate'] 
for i,(f,d) in enumerate(zip(list98,list97)):
    print("編號:{0:<10} 水果:{1:<12} 甜點:{2:<12}".format(i,f,d))
#zip在最短sequence結束    
#=======================================================================
#4. reversed
#reversed iterates over the elements of a sequence in reverse order 
for i in reversed(range(10)):
    print(i)
    
#注意 reversed(range(10)) 仍只是iterator,不能直接列印   
