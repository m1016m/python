# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 06:14:48 2018
fs717_ch03_23a_ftree.py
@author: zzjack
"""
n=int(input("請輸入樹高:"))
for i in range(1,n+1):
    print(" "*(n-i),str(i)*(2*i-1))
