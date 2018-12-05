# -*- coding: utf-8 -*-
"""
adv_p2_01.py, ndarray
@author: III
"""
import numpy as np #import numpy as np, 這是一般命名
data=np.array([[2,4,6],[1,7,9]]) #numpy.ndarray(),參數是 lol, list of list
data #檢視

type(data) #numpy.ndarray object
#------------------------------------------------------------------------
#ndarray, shape and dtype and dimension
data.shape #ndarray data, shape 為2x3 (2列3行)
data.dtype #ndarray data, dtype 為int32
#------------------------------------------------------------------------
#Creating ndarrays, 使用 numpy.array() 函數,接受所有sequence-like object
list01=[5,6.5,4,8,-1] #list 'list01'
a1=np.array(list01)   #將list 'list01' 轉成 ndarray 'a1'
tuple01=(3,6,9,-8)    #tuple 'tuple01'
a2=np.array(tuple01)  #將tuple 'tuple01' 轉成 ndarray 'a2'
a1 #檢視
a2 #檢視
#將list of list 轉成 3x4 的ndarray
a3=np.array([list(range(3,7)),list(range(1,5)),list(range(5,9))]) 
a3 #檢視
a3.shape # shape (3,4)
a3.ndim  # dimension 2
#-----------------------------------------------------------------------
#那麼,轉成 np.ndarray object 有什麼好處?
#-->ndarray object 有許多的method 可用 
a3.mean(axis=0) #沿0軸求平均, 結果為 array([ 3.,  4.,  5.,  6.])
a3.sum(axis=1)  #沿1軸求加總, 結果為 array([18, 10, 26])
a3.cumsum(axis=0)  #沿0軸累加
a3.cumprod(axis=1) #沿1軸累乘 
(a3>=2).all(1) #沿1軸檢查是否每個元素都 >= 2, 結果為布林陣列:
               # array([ True, False,  True], dtype=bool)
(a3>=8).any(0) #沿0軸檢查是否有任一元素都 >= 8, 結果為布林陣列:
               # array([False, False, False,  True], dtype=bool)

#練習1: a3的每一元素是否皆為正數?

#---------------------------------------------------------------------
#numpy.random.randn(), 常態分布; normal() 高斯分布; randint(), ...
arr01=np.random.randn(10)
arr01 #檢視
type(arr01) #numpy.ndarray object
arr01.shape #(10,)               
arr01.ndim  #維度為 1

arr02=np.random.randn(5,7)
arr02 #檢視
arr02.shape #(5,7)
arr01.ndim  #維度為 2

#-------------------------------------------------------------------
#numpy.arange() function, reshape() method
arr03=np.arange(1,10) #序列產生器
arr03 #display array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr03=arr03.reshape(3,3) #重塑(reshape)為 3x3
arr03 #display

#-------------------------------------------------------------------
#numpy.where() function
arr04=np.random.randn(3,4) #常態分佈 3x4
arr04
#將所有正值改為1;所有負值改為-1
arr04a=np.where(arr04 > 0, 1, -1)
arr04a
#將所有正值改為1;負值保留
arr04b=np.where(arr04 > 0, 1, arr04)









#練習1 參考解答: (a3 >= 0).all()


