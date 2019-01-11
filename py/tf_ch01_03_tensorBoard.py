# -*- coding: utf-8 -*-
"""
tf_ch01_03_tensorBoard.py
Created on Mon Aug 21 16:30:47 2017
@author: III
"""
import tensorflow as tf

a=tf.constant(10,name='a')
b=tf.constant(90,name='b')

y=tf.Variable(a+b*2,name='y')
model=tf.global_variables_initializer()

with tf.Session() as session:
    merged=tf.summary.merge_all()
    writer=tf.summary.FileWriter("C:\\tensorflow\\tensorboard",session.graph)
    session.run(model)
    print(session.run(y))