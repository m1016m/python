# -*- coding: utf-8 -*-
"""
ch00_201_tensor.py
Created on Wed Sep 26 21:13:04 2018
@author: zzjack
"""
#初始化互動式 TensorFlow session
import tensorflow as tf
tf.InteractiveSession()

#1. 初始化常數張量
#1.1 設定0階常數張量 (純量) a
a=tf.constant(2)

#直接檢視 a, TensorFlow 回傳一個參考,而不是張量的值
a  #<tf.Tensor 'Const:0' shape=() dtype=int32>

#要傳回張量的值,必須呼叫 tf.Tensor.eval() method
a.eval() #2

#1.2 設定1階常數張量 (向量) b
b=tf.constant([2,5,7])

b #<tf.Tensor 'Const_1:0' shape=(3,) dtype=int32>

#1.3 設定2階常數張量 (矩陣) c
c=tf.constant([[1,2,3],[4,5,6]])
c.eval() #<tf.Tensor 'Const_2:0' shape=(2, 3)
c.eval().shape #(2,3)
c.eval().ndim #2

#=================================================
#以tf.zeros() 建立張量
a1=tf.zeros(2) #1階張量
a1 #<tf.Tensor 'zeros:0' shape=(2,) dtype=float32>
a1.eval() #array([0., 0.], dtype=float32)

#=================================================
#以tf.ones() 建立張量
b1=tf.ones((3,3)) #2階張量
b1.eval()
b1.eval().shape #(3,3)

#=================================================
#以tf.fill() 建立張量
c1=tf.fill((2,2,3),value=5)
c1.eval()
c1.get_shape() #TensorShape([Dimension(2), Dimension(2), Dimension(3)])

#=================================================
#以 tf.random_normal() 建立隨機常態值的張量
d1=tf.random_normal((2,2),mean=0,stddev=1)
d1.eval()

#=================================================
#以 tf.truncated_normal() --> 行為模式與 random_normal() 相同
#但是會將離平均值兩個標準差以上的值移除並重新抽樣
#在大樣本時，張量會較穩定
e1=tf.truncated_normal((10,10,3),mean=0,stddev=1)
e1.eval()

#=================================================
#以 tf.random_uniform(),從指定範圍均勻分布隨機值
f1=tf.random_uniform((2,2),minval=-2,maxval=2)
f1.eval()

