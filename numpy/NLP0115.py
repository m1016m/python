import numpy as np
'''
#及閘(AND)含權重的總和超過臨界值(theta)回傳1
print ('及閘(AND)含權重的總和超過臨界值(theta)回傳1')
def AND(x1 , x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta :
        return 0
    elif tmp > theta :
        return 1

print (AND (0 , 0))
print (AND (1 , 0))
print (AND (0 , 1))
print (AND (1 , 1))
print ()
print ('反及閘(NAND)含權重的總和超過臨界值(theta)回傳0')
def NAND(x1 , x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta :
        return 1
    elif tmp > theta :
        return 0

print (NAND (0 , 0))
print (NAND (1 , 0))
print (NAND (0 , 1))
print (NAND (1 , 1))
print ()
print ('或閘(OR)只要有一個輸入訊號為1，就會輸出1')
def OR(x1 , x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= 0 :
        return 0
    else :
        return 1

print (OR (0 , 0))
print (OR (1 , 0))
print (OR (0 , 1))
print (OR (1 , 1))
print ()
'''
#導入權重(w)和偏權值(bias)
print ('導入權重(w)和偏權值(bias)')
def AND(x1 , x2):
    x = np.array([x1 , x2])
    w = np.array([0.5 , 0.5])
    b = -0.7#調整發火難度的參數
    #假設b = -0.1 輸入的加權總合只要超過0.1神經元就會發火，假設b = -20.0 輸入的加權總合必須超過20.0神經元才會發火
    tmp = np.sum(w * x) + b
    if tmp <= 0 :
        return 0
    elif tmp > 0 :
        return 1

print (AND (0 , 0))
print (AND (1 , 0))
print (AND (0 , 1))
print (AND (1 , 1))
print ()

print ('NAND的權重和偏權值剛好相反')
def NAND(x1 , x2):
    x = np.array([x1 , x2])
    w = np.array([-0.5 , -0.5])
    b = 0.7#調整發火難度的參數
    #假設b = -0.1 輸入的加權總合只要超過0.1神經元就會發火，假設b = -20.0 輸入的加權總合必須超過20.0神經元才會發火
    tmp = np.sum(w * x) + b
    if tmp <= 0 :
        return 0
    elif tmp > 0 :
        return 1

print (NAND (0 , 0))
print (NAND (1 , 0))
print (NAND (0 , 1))
print (NAND (1 , 1))
print ()
print ('OR的權重和偏權值和及閘不同')
def OR(x1 , x2):
    x = np.array([x1 , x2])
    w = np.array([0.5 , 0.5])
    b = -0.2#調整發火難度的參數
    #假設b = -0.1 輸入的加權總合只要超過0.1神經元就會發火，假設b = -20.0 輸入的加權總合必須超過20.0神經元才會發火
    tmp = np.sum(w * x) + b
    if tmp <= 0 :
        return 0
    elif tmp > 0 :
        return 1

print (OR (0 , 0))
print (OR (1 , 0))
print (OR (0 , 1))
print (OR (1 , 1))
print ()
#當x1 or x2之中有一個是1時，就會輸出1。叫做XOR
#(0 , 0) 0 (1 , 0) 1  (0 , 1) 1 (1 , 1) 0單層感知機無法表示出以繪圖呈現

def step_function(x) :
    if x > 0:
        return 1
    else :
        return 0
print ('執行互斥或閘')
def XOR(x1 , x2):
    s1 = NAND (x1 , x2)
    s2 = OR (x1 , x2)
    y = AND (s1 , s2)
    return y

print (XOR (0 , 0))
print (XOR (1 , 0))
print (XOR (0 , 1))
print (XOR (1 , 1))
print ()
#x只能輸入實數(浮點數)但不能輸入step_function(np.array([1.0,2.0]))
#所以可以改成這樣
def step_function(x) :
    y = x > 0
    return y.astype(np.int)

#以直譯器撰寫的程式碼
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
y = x > 0


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
 #階梯函數是以0為界線，輸出從0切換到1 (或從1切換到0)
def step_function(x) :
    return np.array(x > 0,dtype = np.int)

x = np.arange(-5.0 , 5.0 ,0.1)
y = step_function(x)
print(y)
plt.plot(x , y)
plt.ylim(-0.1 , 1.1)#設定y軸的範圍
plt.show()

#sigmoid
def sigmoid( x ) :
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
y = sigmoid(x)
print (y)

#sigmoid繪圖
def sigmoid( x ) :
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0 , 5.0 ,0.1)
y = sigmoid(x)
print (y)
plt.plot(x , y)
plt.ylim(-0.1 , 1.1)#設定y軸的範圍
plt.show()

#relu繪圖  np.maximum：(X, Y, out=None) X 与 Y 逐位比较取其大者；最少接收两个参数
def relu( x ) :
    return np.maximum(0 , x)

x = np.arange(-5.0 , 5.0 ,0.1)
y = relu(x)
print (y)
plt.plot(x , y)
plt.ylim(-0.1 , 1.1)#設定y軸的範圍
plt.show()