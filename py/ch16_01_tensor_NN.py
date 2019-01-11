# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:39:00 2018
"""
#ch16_01_tensor_NN.py
#以TensorFlow 張量運算實作神經網路數學公式:
#   輸出=activation function(輸入*權重+偏差)
#     y=activation function(x*W+B)
import tensorflow as tf
import numpy as np

#step1: 計算圖
# x(輸入) --> 以二維張量實作, x.shaple: (1,3)  x1,x2,x3
x=tf.Variable([[0.4,0.2,0.4]]) 
# W(權重) --> 以二維張量實作, w.shaple: (3,2) w11,w12 w21,w22 w31,w33
W=tf.Variable([[-0.5,-0.2],[-0.3,0.4],[-0.5,0.2]])
# B(偏移植) --> 以二維張量實作, b.shape: (2,) b1,b2
b=tf.Variable([[0.1,0.2]])

#step2:  x*W+B, tf.matmul()
xWb=tf.matmul(x,W)+b
#y=activationFunction(x*W+B), 這裡Activaton Function以 ReLU
y=tf.nn.relu(xWb)

#step3: 以 with Session 執行計算圖
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    print('xWb:',sess.run(xWb))
    print('y:',sess.run(y))

tf.summary.merge_all() #將所有要顯示在TensorBoard的資料整合
train_writer=tf.summary.FileWriter('log/area',sess.graph) 
#將資料寫至log檔,log檔會儲存在目前程式執行目錄下的log/area子目錄
    
#==============================================================
#改以 sigmoid 作為 activation function
#y_sigmoid=sigmoid(x*W+B)

#step4.
y_sigmoid=tf.nn.sigmoid(xWb)
with tf.Session() as sess2:
    init=tf.global_variables_initializer()
    sess2.run(init)
    print('xWb:',sess2.run(xWb))
    print('y_sigmoid:',sess2.run(y_sigmoid))   
    
#===========================================================================
#上述, Weight與bias 是一定植。
#以下, 為了建立 MLP model
#我們以 TensorFlow.random_normal() 產生的常態分佈亂數, 給定 W和b 初值
#step5: 建立計算圖, W及b為常態分佈亂數
W=tf.Variable(tf.random_normal([3,2])) # 產生 [3,2] 常態分佈亂數 Weight ([[w11,w12],[w21,w22],[w31,w32]])
b=tf.Variable(tf.random_normal([1,2])) # 產生 [1,2] 常態分佈亂數 bias ([[b1,b2]])
#輸入 x 與前式相同, ([[x1,x2,x3]]), [1,3]
x=tf.Variable([[0.4,0.2,0.4]])
#以relu 作為 activation function
y=tf.nn.relu(tf.matmul(x,W)+b)

#step6.　以 with Session 執行計算圖
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    print('W:',sess.run(W))
    print('b:',sess.run(b))
    print('y:',sess.run(y))

#step6a. 
#step6 可以合併執行如下:
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    (W,b,y)=sess.run((W,b,y)) #只要執行一次 sess.run()
    print('W:',W)
    print('b:',b)
    print('y:',y)
    
#step6b. tensorflow.random_normal, 常態分佈亂數說明
#使用 tf.random_normal() 產生常態分佈的亂數 list
ts_norm=tf.random_normal([1000])
with tf.Session() as session:
    norm_data=ts_norm.eval() #Evaluates this tensor in a `Session`.
print(norm_data[:5])  #印出前5個值

#繪圖顯示 tensor 'ts_norm'
import matplotlib.pyplot as plt
plt.plot(norm_data)
plt.show()

#=========================================================================================
# 以 placeholder 傳入x值
# NN輸入 x (x1,x2,x3),可以是任何數值, 實際運用時我們以 placeholder 傳入NN進行運算
# 以下, 我們將x改為 placeholder, 在 sess.run() 執行計算圖時,可以使用 feed_dict 
# 傳入二維陣列進行運算

W=tf.Variable(tf.random_normal([3,2]))
b=tf.Variable(tf.random_normal([1,2]))
x=tf.placeholder("float",[1,3]) #x, tf.placeholder
y=tf.nn.relu(tf.matmul(x,W)+b)
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    x_array=np.array([[0.4,0.2,0.4]]) #x_array, [1,3]
    (_b,_W,_x,_y)=sess.run((b,W,x,y),feed_dict={x:x_array}) #在sess.run() 執行計算圖時,以feed_dict參數
                                                          #指定 x (placeholder) 值為 'x_array'
    print('b:',_b)
    print('W:',_W)
    print('x:',_x)
    print('y:',_y)
    
#============================================================================
#建立layer函數,以矩陣運算模擬NN
#用以建立Multilayer Perceptron, MLP (多層感知器)

#step1. 以TensorFlow自建layer函數 
#output_dim-->輸出神經元個數, input_dim-->輸入神經元個數
#inputs-->輸入的二維陣列placeholder, activation-->activation function 預設是 None
def layer(output_dim,input_dim,inputs,activation=None):
    #產生維度 [input_dim,output_dim] 的常態分佈亂數矩陣,作為Weight的初值
    W=tf.Variable(tf.random_normal([input_dim,output_dim])) 
    #產生維度 [1,output_dim]的常態分佈亂數矩陣,作為bias的初值
    b=tf.Variable(tf.random_normal([1,output_dim]))
    #矩陣運算式 XWb=(inputs*W)+b
    XWb=tf.matmul(inputs,W)+b
    #activation function 設定
    if activation is None:  #如果未指定 activation function
        outputs=XWb         #回傳 XWb
    else:                   #如果有指定 activation function
        outputs=activation(XWb)
    return outputs
#step2. 使用自建的layer函數,建立3層(輸入層(x)、隱藏層(h)、輸出層(y)的MLP
#       其中輸入層(x)維度-->[1,4], 隱藏層(h)維度-->[1,3], 輸出層(y)維度-->[1,2]
#輸入層 X
X=tf.placeholder("float",[1,4])  
#隱藏層 h,使用layer函數來建立
#activation function--> tf.nn.relu
h=layer(output_dim=3,input_dim=4,inputs=X,
       activation=tf.nn.relu)
#輸出層 y,使用layer函數來建立
y=layer(output_dim=2,input_dim=3,inputs=h)
#以with tf.Session() 執行計算圖
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    #設定X_array 值為 np.array[[4]]
    X_array=np.array([[0.4,0.2,0.4,0.5]])
    #執行sess.run(), feed_dict參數 {X:X_array}
    (layer_X,layer_h,layer_y)=sess.run((X,h,y),feed_dict={X:X_array})
    #print 
    print('input Layer X:',layer_X)
    print('hidden Layer h:',layer_h)
    print('output Layer y:',layer_y)

#=================================================================================
# 建立layer_debug函數顯示Weight與bias
#step1. 建立layer_debug函數,除了回傳 output 外,也回傳 Weight與bias
def layer_debug(output_dim,input_dim,inputs,activation=None):
    W=tf.Variable(tf.random_normal([input_dim,output_dim]))
    b=tf.Variable(tf.random_normal([1,output_dim]))
    XWb=tf.matmul(inputs,W)+b
    if activation is None:
        outputs=XWb
    else:
        outputs=activation(XWb)
    return outputs,W,b

#step2. 使用layer_debug函數建立3層MLP (x,h,y),
#並顯示第一層W1與b1,第二層W2,b2
X=tf.placeholder("float",[1,4])
h,W1,b1=layer_debug(output_dim=3,input_dim=4,inputs=X,activation=tf.nn.relu)
y,W2,b2=layer_debug(output_dim=2,input_dim=3,inputs=h)
with tf.Session() as sess:
    init=tf.global_variables_initializer()
    sess.run(init)
    #設定輸入值 X_array
    X_array=np.array([[0.4,0.2,0.4,0.5]])
    (layer_X,layer_h,layer_y,W1,b1,W2,b2)=sess.run((X,h,y,W1,b1,W2,b2),feed_dict={X:X_array})
    print('input Layer X:')
    print(layer_X)
    print('W1:')
    print(  W1)    
    print('b1:')
    print(  b1)    
    print('hidden Layer h:')
    print(layer_h)    
    print('W2:')
    print(  W2)    
    print('b2:')
    print(  b2)    
    print('output Layer y:')
    print(layer_y)

