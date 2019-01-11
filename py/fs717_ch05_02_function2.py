# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:21:25 2018
fs717_ch05_02_function2.py
@author: zzjack
"""

#定義兩個 "攝氏" 轉 "華氏" 函數 degreeF=degreeC*1.8+32 
#CtoF01(degreeC), 只列印, 無顯式 return (return None)
def CtoF01(degreeC):
    degreeF=degreeC*1.8 + 32
    print("攝氏 {0:5.1f} 度, 等於華氏 {1:5.1f}".format(degreeC,degreeF))
    
#CtoF02(degreeC), 回傳(return) 華氏溫度值
def CtoF02(degreeC):
    degreeF=degreeC*1.8 + 32
    return degreeF

#輸入介面
dg=eval(input("請輸入攝氏溫度(度C):" ))

#叫用 function CtoF01()
CtoF01(dg)   

#叫用 function CtoF02()
print("攝氏 {0:5.1f} 度, 等於華氏 {1:5.1f}".format(dg,CtoF02(dg))) 

