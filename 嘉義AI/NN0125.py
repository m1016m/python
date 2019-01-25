import numpy as np
A = np.array([[1 , 2] , [3 , 4]])
print(A.shape)
B = np.array([[5 , 6] , [7 , 8]])
print(B.shape)
#矩陣相乘 np.dot(A, B) 與 np.dot(B, A)因為順序不同所以乘積也會不同
print(np.dot(A, B))
#多維矩陣相乘必須 Ａ矩陣第一維的元素數量（行數）與Ｂ矩陣第0維的元素數量（列數）必須相同
#例如 A = np.array([[1 , 2 ,3] , [4 , 5 ,6]]) 2 * 3 矩陣  B = np.array([[1 , 2 ] , [3 ,4 ] ,[5 ,6]]) 3 * 2
C = np.array([[1 , 2 ,3] , [4 , 5 ,6]]) # 2 * 3 矩陣  
D = np.array([[1 , 2 ] , [3 ,4 ] ,[5 ,6]]) # 3 * 2
print(np.dot(C, D))

E = np.array([[1 , 2] , [4 , 5]])# 2 * 2 矩陣
# print(np.dot(C, E)) 會發生錯誤 因為 C矩陣第一維的元素數量（行數）與E矩陣第0維的元素數量（列數）不同
#F是二維矩陣，G是一維矩陣，遵循同樣讓對應維度的元素數量一致
F = np.array([[1 , 2],[3, 4],[5 , 6]])
G = np.array([7 , 8])
print(np.dot(F , G))

#神經網路的乘積 (一層)
# X是輸入值  W是權重  Y是輸出值
X = np.array([1 , 2])
W = np.array([[1 , 3 , 5],[2 , 4 , 6]])
Y = np.dot(X , W)
print(Y)
#多層神經網路 加權總和  A(1) = X*W(1) + B(1)
#先處理第 0 層
def sigmoid(x) :
    return 1 / (1 + np.exp(-x))
X = np.array([1.0 , 0.5])
W = np.array([[0.1 , 0.3 , 0.5] , [0.2 , 0.4 , 0.6]])
B1 = np.array([0.1 , 0.2 , 0.3])
print(X.shape)
print(W.shape)
print(B1.shape)

A1 = X.dot(W) + B1
Z1 = sigmoid(A1)
print(A1)
print(Z1)
#處理第 1 層
W2 = np.array([[0.1 , 0.4] , [0.2 , 0.5], [0.3 , 0.6]])
B2 = np.array([0.1 , 0.2])
print(Z1.shape)
print(W.shape)
print(B1.shape)

A2 = np.dot(Z1 , W2) + B2
Z2 = sigmoid(A2)
print(A2)
print(Z2)
#最後一層輸出
def identity_function (x) :
    return x

W3 = np.array([[0.1 , 0.3] , [0.2 , 0.4]])
B3 = np.array([0.1 , 0.2])

A3 = np.dot(Z2 , W3) + B3
Y = identity_function (A3)# or Y = A3
#神經網路可以用來解決分類和迴歸的問題，解決分類和迴歸的問題必須改變輸出層的活化函數，回歸要用恆等函數而分類則要用softmax函數
#分類問題是指資料屬於哪種類別問題？例如：從拍攝的人像中分類男性或女性，然而回歸問題是：從輸入資料中預測（連續性）數值，例如：從拍攝的人像中預測哪個人的體重
#恆等函數是將輸入直接輸出，對於輸入的內容完全不做任何處理
#softmax function
a = np.array([0.3 , 2.9 , 4.0])
exp_a = np.exp(a) #指數函數
print(exp_a)
sum_exp_a = np.sum(exp_a)#指數函數的和
print(sum_exp_a)
y = exp_a /sum_exp_a
print (y)
#寫成function
def softmax(a) :
    exp_a = np.exp(a)
    um_exp_a = np.sum(exp_a)
    y = exp_a /sum_exp_a
    return y

#MNIST
#wget https://github.com/tensorflow/models/archive/master.zip -O models.zip 
#unzip models.zip
import sys , os
import sys, os 
#os.chdir('/ch03')  
sys.path.append(os.pardir) #載入父目錄檔案設定 
from dataset.mnist import load_mnist
#(訓練影像，訓練標籤)(測試影像，測試標籤)
(x_train , t_train),(x_test , t_test) = load_mnist(flatten = True , normalize = False)
#normalize設定輸入影像是否正規化為 0.0 ~ 1.0的值，如果是False輸入影像的像素就維持原本的 0 ~ 255
#flatten設定輸入影像是否變平（一維陣列）如果是False輸入影像的像素就是 1* 28 * 28 三維陣列，如果是True就儲存由784個元素形成的一維陣列
#one_hot_label 是設定是否儲存成one_hot編碼
#分別輸出資料的形狀
print (x_train.shape)
print (t_train.shape)
print (x_test.shape)
print (t_test.shape)




