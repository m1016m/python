# -*- coding: utf-8 -*-
"""
tf_ch01_02_tensorflow.py
Created on Mon Aug 21 15:54:35 2017
@author: III
"""
x=1
y=x+9
print(y)

#以上python一般程式ok!
#---------------------------------------
import tensorflow as tf
x=tf.constant(1,name='x')
y=tf.Variable(x+9,name='y')
print(y) #<tf.Variable 'y:0' shape=() dtype=int32_ref>


