# -*- coding: utf-8 -*-
"""
ch00_KerasModel_02.py
Created on Wed Jul  4 22:21:04 2018
@author: zzjack
"""
#From Keras documents

#import 必需模組
from keras.layers import Input, Dense
from keras.models import Model

#以Input()定義輸入層 inputs_784
inputs_784 = Input(shape=(784,))

#定義兩個隱藏層，每個隱藏層皆有64個神經元，啟動函數皆為 relu
#第一個隱藏層(h1)以輸入層(inputs_784)作為參數
#第二個隱藏層(h2)以h1作為參數 
h1 = Dense(64, activation='relu')(inputs_784)
h2 = Dense(64, activation='relu')(h1)

#定義輸出層(y),以最近的隱藏層(h2)作為參數,啟動函數為 softmax
y = Dense(10, activation='softmax')(h2)

#定義 Model object "model_mnist",輸入(inputs)及輸出(outputs)參數
model_mnist=Model(inputs=inputs_784,outputs=y) 

#完成模型物件定義後, 以.compile() 編譯
model_mnist.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#檢視模型
print(model_mnist.summary())
#fitting, 目前本例中未帶入真正資料
model_mnist.fit(train_data, labels)


