# -*- coding: utf-8 -*-
"""
fs717_ch12_011_Entry.py
Created on Wed Jun 27 10:17:16 2018
@author: zzjack
"""
from tkinter import *

#定義一個 "+" 處理事件函數 addFun()
def addFun():
    result01.set(num01.get()+num02.get())
    
#定義一個 "-" 處理事件函數 minusFun()
def minusFun():
    result11.set(num11.get()-num12.get())    
#以Tk()函數建立一個windows object "window01"
window01=Tk()

#以DoubleVar() 建立三個 DoubleVar object, "num01","num02","result01"
num01=DoubleVar()
num02=DoubleVar()
result01=DoubleVar()

num11=DoubleVar()
num12=DoubleVar()
result11=DoubleVar()

#以 Entry() 函數建立一個Entry物件(方塊文字)
#父物件 "window01",內容為變數物件 "num01"
#以Entry.pack() method 指定靠左 
Entry(window01,width=10,textvariable=num01).grid(row=0,column=0)

#緊接著一個 Label object "+"
Label(window01,width=5,text="+").grid(row=0,column=1)

#再接一個 Entry object
Entry(window01,width=10,textvariable=num02).grid(row=0,column=2)

#再來，用Button()函數建立一個Button object,對應的事件處理函數 "addFun()"
Button(window01,width=5,text="=",command=addFun).grid(row=0,column=3)

#最後是一個 Entry object,顯示結果
Entry(window01,width=10,textvariable=result01).grid(row=0,column=4)

#===================================================================
Entry(window01,width=10,textvariable=num11).grid(row=1,column=0)
Label(window01,width=5,text="-").grid(row=1,column=1)
Entry(window01,width=10,textvariable=num12).grid(row=1,column=2)
Button(window01,width=5,text="=",command=minusFun).grid(row=1,column=3)
Entry(window01,width=10,textvariable=result11).grid(row=1,column=4)

#以視窗物件的mainloop() method,讓視窗進入等待與處理事件的狀態，
#直到使用者關閉視窗為止
window01.mainloop()  
