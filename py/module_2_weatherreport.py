# -*- coding: utf-8 -*-
#module
#所謂的模組(module),只是一個Python程式檔
#要參考其他模組的程式，使用import 陳述式，它可以讓你的程式使用被匯入
#的模組裡的程式與函式

#匯入模組 import module, 其中module是其他Python檔，不包含.py副檔名
#example: module_2_weatherreport.py
import report #import report.py

print('使用 report.py 中的 get_description()')
description=report.get_description() #使用report.py 中 get_description()函式
print("Today's weather:",description)
print('----------------------------------------------')

print('使用 report.py 中的 get_description2()')
description2=report.get_description2() #使用report.py 中 get_description2()函式
print("Today's weather 2:",description2)
print('----------------------------------------------')
