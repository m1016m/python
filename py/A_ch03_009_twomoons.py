#A_ch03_009_twomoons.py
import matplotlib.pyplot as plt

#以 make_moons() 建立虛擬 two_moons 資料集
from sklearn.datasets import make_moons
X,y=make_moons(n_samples=200, noise=0.05,random_state=0)

#檢視資料 feature 'X' and label 'y'
import collections #使用 collections.Counter() 計算 y 內容
contents_of_y=collections.Counter(y)
print('X.shape: ',X.shape,'  y.shape: ',y.shape,' y.',' contents_of_y:',contents_of_y)

#繪圖檢視 two_moons 資料集
plt.scatter(X[:,0],X[:,1],c=y)

#以 k-means 演算法將資料 X 分成兩群
from sklearn.cluster import KMeans
kmeans_2=KMeans(n_clusters=2) #設定 n_clusters=2
kmeans_2.fit(X)               #以 X 來fit模型 kmeans_2
y_pred_2=kmeans_2.predict(X)  #使用 KMeans.predict() 將資料集X貼分群標籤,並指定給 y_pred_2

#繪圖顯示 k-means 對 two_moons 資料集分群結果,
#    顯示群分配與群中心

import mglearn
plt.scatter(X[:,0],X[:,1],c=y_pred_2,cmap=mglearn.cm2,s=60) 
plt.scatter(kmeans_2.cluster_centers_[:,0],kmeans_2.cluster_centers_[:,1],  #畫群分配
           marker='^',c=[mglearn.cm2(0),mglearn.cm2(1)],s=100,linewidths=2) #畫群中心
plt.xlabel("Feature 0") #橫座標label
plt.ylabel("Feature 1") #縱座標label
