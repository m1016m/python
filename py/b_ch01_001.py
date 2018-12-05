# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:58:58 2018

@author: zzjack
"""

n=int(input('please key in a int:'))
sum=0
for i in range(n+1):
    sum+=i
    
print('1+2+3+...+',n,'=',sum)