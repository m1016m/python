# -*- coding: utf-8 -*-
"""
adv_p2_02.py, Basic Indexing and Slicing
@author: III
"""
import numpy as np
#Basic Indexing and Slicing
arr=np.arange(1,10).reshape(3,3)
arr #display
arr[:2,1:] 

arr[2]
arr[2,:]

arr[:,:2]

arr[1,:2]
#------------------------------------------
#Boolean Indexing
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe']) #一維陣列 names
arr05=np.arange(1,29).reshape(7,4)

#布林陣列
names=='Bob' #布林陣列
             #array([ True, False, False,  True, False, False, False], dtype=bool)
#使用布林陣列當索引切片
arr05[names=='Bob']

mask=(names=='Bob')|(names=='Will') #布林陣列 mask
mask #array([ True, False,  True,  True,  True, False, False], dtype=bool)
arr05[mask]

