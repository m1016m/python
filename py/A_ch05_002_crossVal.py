# -*- coding: utf-8 -*-
"""
A_ch05_002_crossVal.py
Created on Thu Mar  8 18:55:25 2018
@author: III
"""
#cross-validation (交叉驗證)
#example 1, 以make_blobs虛擬資料集為例

#import cross_val_score
from sklearn.model_selection import cross_val_score 
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression

#step 0. 建立一組虛擬資料, 使用 make_blobs
X,y=make_blobs(random_state=0,n_samples=200)

#step 1. 建立及訓練(fit)模型,用資料集(X,y)來做交叉驗證
#使用LogisticRegression()建立模型 'logregModel'
logregModel=LogisticRegression() 

#step 2. 以cross_val_score() 做交叉訓練驗證
#        estimator=LogisticRegression model 'logregModel'
#        fold number=3,(cv=3)
score_k3=cross_val_score(logregModel,X,y,cv=3)

#step 3. 檢視cross_validation 過程
print("Cross-validation score:{}".format(score_k3))

#step 4. 檢視acc平均值, score_k3.mean()
print("Average cross-validation score:{:.2f}".format(score_k3.mean()))

#step 5. 更改flod值為5 (cv=5), 做交叉訓練驗證
score_k5=cross_val_score(logregModel,X,y,cv=5)

#step 6. 檢視cross_validation 過程,檢視acc平均值, score_k5.mean()
print("Cross-validation score:{}".format(score_k5))
print("Average cross-validation score:{:.2f}".format(score_k5.mean()))

#step 7. 由上可知,對這組資料以邏輯斯回歸演算法來擬合(estimator=LogisticRegression)
#        k=3,k=5 Avg. acc. 差不多是 0.94
#        以下, 同一組資料我們換一個演算法 SVM 做k=3,k=5的交叉驗證訓練並檢視結果
from sklearn import svm
#建立svm.SVC model 'svmModel'
svmModel=svm.SVC() 

#以svm model 做擬合演算法, cv=3
score_svm_k3=cross_val_score(svmModel,X,y,cv=3)

#檢視cross_validation 過程,檢視acc平均值, score_svm_k3.mean()
print("Cross-validation score:{}".format(score_svm_k3))
print("Average cross-validation score:{:.2f}".format(score_svm_k3.mean()))

#以svm model 做擬合演算法, cv=5
score_svm_k5=cross_val_score(svmModel,X,y,cv=5)

#檢視cross_validation 過程,檢視acc平均值, score_svm_k5.mean()
print("Cross-validation score:{}".format(score_svm_k5))
print("Average cross-validation score:{:.2f}".format(score_svm_k5.mean()))
