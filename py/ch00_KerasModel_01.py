# -*- coding: utf-8 -*-
"""
ch00_KerasModel_01.py
Created on Tue Jul  3 10:55:22 2018
@author: III
"""
#Keras Sequential Model, 方法一
#create a Sequential model by passing a list of layer instances 
#to the constructor
#==============================================================
#import module
from keras.models import Sequential
from keras.layers import Dense,Activation

#建立一個參數list "layers"
layers=[Dense(32,input_shape=(784,)),
        Activation('relu'),
        Dense(10),
        Activation('softmax')]

#以Sequential()函數,以list "layers" 當引數,建立模型 "model01"
model01=Sequential(layers)

#檢視 model "model01"
print(model01.summary())

#================================================================
#Keras Sequential Model, 方法二
#You can also simply add layers via the .add() method

#以Sequential() 函數,建立一個空的 Sequential model "model02"
model02=Sequential()

#以.add() method 加上一個層
model02.add(Dense(32,input_shape=(784,)))
#以.add() method 設定此層的activation function 為 "Relu"
model02.add(Activation('relu'))
#在加一個10個神經元的輸出層
model02.add(Dense(10))
#設定輸出層的activation function 為 "Softmax"
model02.add(Activation('softmax'))

#檢視 model "model02"
print(model02.summary())








