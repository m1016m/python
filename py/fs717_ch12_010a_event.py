# -*- coding: utf-8 -*-
"""
fs717_ch12_010a_event.py
「事件驅動」(event driven)
Created on Tue Jun 26 22:41:52 2018
@author: zzjack
"""
from tkinter import * 

#定義一個全域變數(global variable) "counter"
counter=0

#定義一個事件處理函數 "showMsg()"
def showMsg():
    global counter #以 keyword global 指定取用全域變數 "counter"
    
    if counter % 2 == 0:   
        #將label物件 "label01" 的text設為 "Hello World!"
        label01["text"]="Hello, World!" 
    else:
        #將label物件 "label01" 的text設為 "",空字串
        label01["text"]=""
        
    counter+=1    

#以Tk()函數建立一個視窗物件,並以變數"window01"指向它    
window01=Tk() 

#以Button()函數建立一個Button widget "btn01",
#父物件為 "window01",text屬性="Display Message"
#事件處理函數為 "showMsg",command=showMsg,
#函數名稱 "showMsg" 以參考方式作為引數值
btn01=Button(window01,text="Display Message",command=showMsg)

#以Label()函數建立一個Label widget "label01",父物件為 "window01"
label01=Label(window01)   

#排版,以 widget.pack() method 由上而下排列 
btn01.pack()  
label01.pack()

#以視窗物件的mainloop() method,讓視窗進入等待與處理事件的狀態，
#直到使用者關閉視窗為止
window01.mainloop()
  
