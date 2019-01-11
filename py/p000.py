# -*- coding: utf-8 -*-
"""
p000.py
"""
#for instruction
for i in range(0,10):
    print(i)

#內建函數(Built-in Functions): input(),print()
num=input('input a number:')
print('輸入值:',num)    

#標準函數庫(std. lib.): re, datetime module
import re
if re.search('aa*bbb(cc)*(d | )','aaaaaabbbcccd '):
    print("符合!")
else:
    print("不符合!")

#other Python Package :
import pandas as pd
df3=pd.read_csv('df3.csv')
df3
    