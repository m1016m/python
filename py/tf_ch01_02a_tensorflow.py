# -*- coding: utf-8 -*-
"""
tf_ch01_02a_tensorflow.py
Created on Mon Aug 21 16:01:51 2017
@author: III
"""
import tensorflow as tf

x=tf.constant(1,name='x')
y=tf.Variable(x+9,name='y')

model=tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))