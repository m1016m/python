# -*- coding: utf-8 -*-

"""
=========================================================
A_ch03_005_kmeans03_a.py
K-means Clustering
=========================================================
"""
import numpy as np
import matplotlib.pyplot as plt

#匯入3D投影模組 Axes3D (不是)真正的3D物件
from mpl_toolkits.mplot3d import Axes3D

#匯入 KMeans 及 datasets module
from sklearn.cluster import KMeans
from sklearn import datasets

#%pylab
#載入 iris datasets, 並將 features 指給 X, label 指給 y
iris = datasets.load_iris()
X = iris.data
y = iris.target

#檢視 features X
print('X.shape:',X.shape)

#設定KMeans model(n_clusters=3) 
estimators =  KMeans(n_clusters=3)

#以plt.figure()設定一個畫布 'fig'             
fig=plt.figure(1,figsize=(4,3))

#以Axes3D() 在 fig 上設定立體座標物件 'ax' 
ax=Axes3D(fig)

#以X fit model 'estimators'
estimators.fit(X) 

#將訓練後的結果 (KMeans.labels_)存在變數labels
labels=estimators.labels_ 

#將訓練後的結果畫3D圖顯示
ax.scatter(X[:,3],X[:,0],X[:,2],
           c=labels.astype(np.float),edgecolor='k')
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
fig.show()



