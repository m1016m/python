# -*- coding: utf-8 -*-
"""
#tf_ch03_01_linearRegression.py, 線性迴歸演算法
Created on Thu Aug 17 11:02:44 2017
@author: zzjack
"""
#線性迴歸演算法
#目標: 依照一個或多個自變數(x)的值來預測因變數的值(y)
#若自變數(x)與因變數(y)之間的關係是線性,則函數為 y=Ax+b
#藉由線性迴歸演算法說明機器學習兩個重要的觀念: 
#  1.成本函數(cost function)
#  2.梯度下降演算法(gradient descent algorithms)
#---------------------------------------------------
#step1. 資料模型: 產生測試資料 
#       為測試線性迴歸演算法,我們產生二維空間的資料點
#       y=Ax+b, A,b 為常數

#import numpy
import numpy as np 

#指定繪製點的數量為 500
num_of_pts=500 

#空串列, x_point y_point
x_point=[]
y_point=[]

#設定常數A,b值
A=0.22
b=0.78

#以 Numpy.random.normal() 產生500個在線性方程式 y=0.22x+0.78 周圍隨機的點
for i in range(num_of_pts):
    x=np.random.normal(0.0,0.5)
    y=A*x+b+np.random.normal(0.0,0.1)
    x_point.append([x])  #這裡x不是以純量加入list,而是以list形式加入
    y_point.append([y])
    
# 繪圖顯示這500個點
import matplotlib.pyplot as plt
#%pylab    
plt.plot(x_point,y_point, 'o', label='Input Data') #'o'-->circle marker
plt.legend()  #圖例
plt.show()

#----------------------------------------------------------------------
#step2. 成本函數(cost function)與梯度下降演算法(gradient descent algorithms)
#       我們將使用step1產生的x,y資料,以線性回歸演算法來逼近常數A,b(這兩個值應該是未知)
#       我們需要在機器學習時選定一種評估方法(成本函數)。這裡,我們選用平均方差(mean square error)
#       而且為了最小化成本函數,我們選用梯度下降演算法。
#       這些(mse,gradient descent)在tensorflow 中都有提供,我們將直接使用

#lost function: 為了訓練模型，必須先定義衡量模型好與壞的標準,在機器學習中，我們使用loss / cost，
#               即，當前模型與理想模型的差距。訓練的目的，就是不斷縮小 loss / cost.
#               如 mean square error (用在線性迴歸)、crossentropy (用在分類模型,如CNN分類)    
#optimizer method: 如何縮小 lost /cost 的 algorithm  
#                  如 'adam'、'mse'、'gradient descent'等      

#import tensorflow
import tensorflow as tf

#使用tf.Variable 定義未知數 A與b:
A=tf.Variable(tf.random_uniform([1],-1.0,1.0)) #1維 [1], 介於-1到1的隨機值
b=tf.Variable(tf.zeros([1])) #b,初始值被設定為 1維 0

#寫出線性方程式
y=A*x_point+b

#引入 tensorflow 的均方差(mean square error)函數,當我們的成本函數 'cost_function'
cost_function=tf.reduce_mean(tf.square(y-y_point))

#引入 tensorflow.train套件中的梯度下降演算法(gradient descent)
#     參數learn rate=0.5 
optimizer=tf.train.GradientDescentOptimizer(0.5)

#使用梯度下降演算法物件的最小化函數, optimizer.minimize()對成本函數 cost_function
#做最小化計算,並命名為 'train'
train=optimizer.minimize(cost_function)

#-----------------------------------------------------------------------------
#step3. 訓練模型
#       以step1. 的資料模型測試梯度下降演算法

#初始化所有變數
model=tf.global_variables_initializer()

#迭代20次,用以決定A,b的最佳值,進而確定最適合資料模型的線
#並繪圖展示
with tf.Session() as session:        #with
    session.run(model)               
    for step in range(0,21):
        session.run(train)
        if (step % 5)==0:            #每5個step
            #繪製點
            plt.plot(x_point,y_point,'o',
                     label='step={}'.format(step))
            #繪製線
            plt.plot(x_point,session.run(A)*x_point + 
                     session.run(b))
            
            plt.legend()
            plt.show()




























