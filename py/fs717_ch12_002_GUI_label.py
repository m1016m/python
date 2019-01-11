# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:16:41 2018
fs717_ch12_002_GUI_label.py
@author: zzjack
"""
from  tkinter  import  *
window = Tk()
label1 = Label(window, text = "我愛資策會", width = 30, bg = "lightyellow")
label2 = Label(window, text = "我真的愛資策會", width = 30, bg = "lightblue")
label3 = Label(window, text = "我真的很愛資策會", width = 30, bg = "lightgray")
#label.pack() pack method 
#pack() 設定位置的方法
label1.pack()
label2.pack()
label3.pack()
window.mainloop()

