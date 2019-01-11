# -*- coding: utf-8 -*-
"""
tf_ch01_01_tensorflow.py
Created on Fri Aug 18 11:21:54 2017
@author: III
"""
#測試 tensorflow 是否安裝成功
import tensorflow as tf
hello=tf.constant("Hello Tensorflow!")
sess=tf.Session()
print(sess.run(hello))
