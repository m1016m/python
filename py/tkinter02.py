# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:52:15 2017

@author: zzjack
"""
import tkinter

#初始化主視窗
root = tkinter.Tk() 
root.title("Hello III!")
root.minsize(400,100)

#標籤 tkinter.Label()
helloLabel=tkinter.Label(root,text='Hello III!')
helloLabel.pack()

#按鈕 tkinter.Button()
def onfirstButtonPress():   #firstButton 按下時的處理程式
    print('tkinter is easy to use')

firstButton=tkinter.Button(root,text='first button',
                           command=onfirstButtonPress)
firstButton.pack()

#以mainloop() 啟動事件迴圈
root.mainloop()