# -*- coding: utf-8 -*-
"""
adv_p1_05.py, comprehension
@author: III
"""
#-------------list comprehension------------------------------------
tuple01=('c#','pascal','SQL','java','python') #tuple 'tuple01'

#將字長超過 3 的程式語言挑出，並構成一串列 'list01'
list01=[] #空串列 list01
for t in tuple01:        #迭代處理tuple01內每個元素
    if len(t) > 3:       #如果元素長度大於 3
        list01.append(t) #加入list 'list01

list01 #檢視 list list01 --> ['pascal', 'java', 'python']

#或者我們可以用串列生成式(list comprehension):
list02=[t for t in tuple01 if len(t)>3]

#也可以在生成時加工(將字母變大寫):
list03=[t.upper() for t in tuple01 if len(t)>3]

#---------------dict. comprehension-----------------------------------
dict01={'a1':'C#','a2':'pascal','a3':'java','a4':'python'}

#將字長超過 3 的程式語言挑出，並構成一字典 'dict02'
dict02={} #空字典 dict01
for k,v in dict01.items(): #迭代處理 dict01.items() (tuple)
    if len(v)>3:           #如果value 長度大於 3
        dict02[k]=v        #新增一個字典元素
        
dict02 #display dict02

#用字典生成式(dictionary comprehension)
dict03={d[0]:d[1] for d in dict01.items() if len(d[1])>3}

#練習:將字長超過 3 的程式語言挑出，並構成一字典，字典內字母字首改為大寫，如下:
#{'a2': 'Pascal', 'a3': 'Java', 'a4': 'Python'}















#練習解答:
#dict04={d[0]:d[1].capitalize() for d in dict01.items() if len(d[1])>3}







