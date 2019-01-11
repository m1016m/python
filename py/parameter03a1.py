# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:09:19 2018
fs717_ch05_05_parameter03a1.py
@author: zzjack
"""

#定義函數 sum_all(), 使用任意引數串列(arbitrary argument list)
def sum_all(*numbers):    #numbers is a tuple
    sumAll=0
    for i in numbers:
        sumAll+=i
    return sumAll
    
#輸入介面
list_n=[]
while True:
    n=input("請逐次輸入數值(任意個數或直接按enter結束):")
    if n!='':
        list_n.append(eval(n))
    else:
        break

#輸出結果,注意! sum_all(*tuple_n)
print("加總值為 {0:10.2f}".format(sum_all(*list_n)))



    
