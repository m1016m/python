# -*- coding: utf-8 -*-
"""
A_ch03_007_Agglomerative_02.py
Agglomerative Clustering 實作範例說明(2)
@author: zzjack
"""
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs 

#import AgglomerativeClustering module
from sklearn.cluster import AgglomerativeClustering

#以make_blobs() 建立虛擬資料, 200資料點, 4個中心
X,y=make_blobs(n_samples=200,centers=4)

#檢視虛擬測試資料 shape
print('X.shape:',X.shape,'  y.shape:',y.shape)

#檢視虛擬測試資料
%matplotlib inline

#以 plt.scatter() 繪圖檢視虛擬測試資料
plt.scatter(X[:,0],X[:,1],c=y)

#建立 AgglomerativeClustering 物件 'agg', n_clusters=4
agg=AgglomerativeClustering(n_clusters=4)

#scikit-learn AgglomerativeClustering 沒有 predict() method, 而是用 fit_predict() method
#fit_predict(X, y=None), Performs clustering on X and returns cluster labels.
#使用 fit_predict() 做分群,並將分群label存於 assignment
assignment=agg.fit_predict(X)

#檢視 assignment
assignment

#使用 mglearn.discrete_scatter 繪圖檢視 AgglomerativeClustering 分群結果
mglearn.discrete_scatter(X[:,0],X[:,1],assignment)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.legend()

#練習 : 同樣虛擬資料 X, AgglomerativeClustering 分群, n_clusters=3
