# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 08:23:52 2018

@author: zzjack
"""
import time

time.time()

print(time.localtime().tm_mon,'/',time.localtime().tm_mday)

print(time.localtime().tm_hour,':',time.localtime().tm_min)

#==========================================================

secs = eval(input("請輸入要倒數的秒數 : "))
for  i  in  range(secs,  0,  -1):
    print("倒數",  i,  "秒…")
    time.sleep(1)

print("間時到 !")

#==========================================================
import  calendar
calendar.isleap(2000)
print(calendar.calendar(2020))