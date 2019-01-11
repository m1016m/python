#A_ch03_011_DBSCAN_twomoons.py
import matplotlib.pyplot as plt
%matplotlib inline

#以 make_moons 建立虛擬資料 
from sklearn.datasets import make_moons
X,y=make_moons(n_samples=200, noise=0.05,random_state=0)

#檢視資料 feature 'X' and label 'y'
import collections #使用 collections.Counter() 計算 y 內容
contents_of_y=collections.Counter(y)
print('X.shape: ',X.shape,'  y.shape: ',y.shape,' y.',' contents_of_y:',contents_of_y)

#繪圖檢視 two_moons 資料集
plt.scatter(X[:,0],X[:,1])

#以StandardScaler() 重新縮放資料
#使單個特徵儘可能接近「零均值(平均值是0)」 和「單位方差(標準差為1)」的高斯分佈
from sklearn import preprocessing
scaler=preprocessing.StandardScaler() #建立 StandardScaler Object 'scaler'
scaler.fit(X)                         #以 X fit scaler
X_scaled=scaler.transform(X)          #以 fit 過的 model 對 X 做 transform 

#繪圖檢視 經 StandardScaler 縮放後的 two_moons 資料集 X_scaled (注意!標尺已更動)
plt.scatter(X_scaled[:,0],X_scaled[:,1])

#建立 DBSCAN model 'dbscan'
from sklearn.cluster import DBSCAN
dbscan=DBSCAN()

#以DBSCAN.fit_predict() 對 資料集 X_scaled 做分群
clusters=dbscan.fit_predict(X_scaled)

#繪圖顯示群的分配
plt.scatter(X_scaled[:,0],X_scaled[:,1],c=clusters)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
