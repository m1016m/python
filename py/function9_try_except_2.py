# -*- coding: utf-8 -*-
# 使用try來包住你的程式,用except來處理錯誤
list2=[1,2,3]
position=5
try:
    list2[position]
except:
    print('Need a position between 0 and',len(list2)-1, ' but got',position)
