# -*- coding: utf-8 -*-
"""
A_ch05_001_evaluation.py

"""
#評估與改善模型效能,一個簡單完整的範例(scikit-learn)

from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#step 0. 建立一組虛擬資料, 使用 make_blobs
X,y=make_blobs(random_state=0,n_samples=200)

#檢視虛擬資料型態
print('type(X)=',type(X),' X.shape=',X.shape,' type(y)=',type(y),
      ' y.shape=',y.shape)

#檢視 X 前5個資料點
X[:5]

#檢視 y(ndarray) 值有多少種, --> 0,1,2 三種
from pandas import DataFrame        #import pandas.DataFrame
df=DataFrame(y,columns=['label'])   #將 y(ndarray) 轉成 DataFrame
df.label.value_counts()             #叫用 DataFrame.value_counts() 

import matplotlib.pyplot as plt
# %matplotlib inline

#繪製檢視 X,y 
for pos in range(0,len(y)):
    if y[pos]==0:
        plt.plot(X[pos][0],X[pos][1],'r^')
    if y[pos]==1:
        plt.plot(X[pos][0],X[pos][1],'g^')
    if y[pos]==2:
        plt.plot(X[pos][0],X[pos][1],'b^')
        
#step 1. 把資料分成train dataset和test dataset
#        train_test_split(), 預設 trainData:testDate 0.75:0.25, 
#        stratify=y, y(label) 比例也是 0.75:0.25 
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,
                                               stratify=y)
#檢視資料比例
print('len(X_train):',len(X_train),' len(X_test):',len(X_test))

#step 2. 建立及訓練(fit)模型,用訓練資料集(X_train,y_train)
#使用LogisticRegression()建立模型 'logregModel'
logregModel=LogisticRegression() 
#以 train data fit 模型
logregModel.fit(X_train,y_train) 

#step 3. 評估模型(score),用測試資料集(X_test,y_test)
score=logregModel.score(X_test,y_test)

print(score)

#step 4. 使用模型預測,注意! predict() 接受的引數 資料維度
logregModel.predict([[-1.73380769,  3.79806117]])

logregModel.predict([X_test[0]])