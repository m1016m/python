# -*- coding: utf-8 -*-
"""
fs717_ch03_01_random.py
Created on Wed Jun 27 10:17:16 2018
@author: zzjack
"""
import random
from tkinter import *

#定義一個 "Start" 處理事件函數 startFun()
def startFun():
    num01.set(random.randint(1,6))
    num02.set(random.randint(1,6))
    num03.set(random.randint(1,6))
    sum01.set(num01.get()+num02.get()+num03.get())
  
#以Tk()函數建立一個windows object "window01"
window01=Tk()

#以IntVar() 建立四個 Int object, "num01","num02","num03","sum01"
num01=IntVar()
num02=IntVar()
num03=IntVar()
sum01=IntVar()

#Label object "骰子一"
Label(window01,width=10,text="骰子一").grid(row=0,column=0)
#Label object "骰子二"
Label(window01,width=10,text="骰子二").grid(row=0,column=1)
#Label object "骰子三"
Label(window01,width=10,text="骰子三").grid(row=0,column=2)
#Label object "總點數"
Label(window01,width=10,text="總點數").grid(row=0,column=3)


#以 Entry() 函數建立一個Entry物件(方塊文字)
#父物件 "window01",內容為變數物件 "num01"
Entry(window01,width=10,textvariable=num01).grid(row=1,column=0)
#再接一個 Entry object
Entry(window01,width=10,textvariable=num02).grid(row=1,column=1)
#再接一個 Entry object
Entry(window01,width=10,textvariable=num03).grid(row=1,column=2)
#再接一個 Entry object
Entry(window01,width=10,textvariable=sum01).grid(row=1,column=3)

#====================================================================
#再來，用Button()函數建立一個Button object,對應的事件處理函數 "addFun()"
Button(window01,width=10,text="擲骰子",command=startFun).grid(row=3,column=0)

#以視窗物件的mainloop() method,讓視窗進入等待與處理事件的狀態，
#直到使用者關閉視窗為止
window01.mainloop()  
