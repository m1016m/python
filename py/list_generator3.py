# -*- coding: utf-8 -*-
#雙層迴圈,99乘法表
#原始寫法
print('--原始寫法--')
rows=range(1,10)
cols=range(1,10)
for row in rows: #外圈
    for col in cols: #內圈
        print(row,'*',col,'=',row*col)
    print('-----------------------')

#--------------------------------------
print('--------------------------------')
print('--使用生成式,製作(row,col) tuple--')
rows=range(1,10)
cols=range(1,10)
cells=[(row,col) for row in rows for col in cols] #
for cell in cells: #for cell in cells
    print(cell)
#----------------------------------------------------
print('----------------------------------------------')
print('--使用 tuple unpacking,從tuple 中拉出 row, col---')
for row,col in cells:
    print(row,'*',col,'=',row*col)
        