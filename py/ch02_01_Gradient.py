# -*- coding: utf-8 -*-
"""
ch02_01_Gradient.py
求取梯度範例
Created on Wed Sep 26 11:36:58 2018
@author: III
"""
#初始化互動式 TensorFlow session
import tensorflow as tf
tf.InteractiveSession()

#設定一維張量W=(3,) 
W=tf.Variable((3,))
l=tf.reduce_sum(W)
#求梯度
gradW=tf.gradients(l,W)

#檢視梯度
gradW


#tf.reduce_sum()
#Computes the sum of elements across dimensions of a tensor.
#for example:
# x = tf.constant([[1, 1, 1], [1, 1, 1]])
# tf.reduce_sum(x)  # 6
# tf.reduce_sum(x, 0)  # [2, 2, 2]
# tf.reduce_sum(x, 1)  # [3, 3]