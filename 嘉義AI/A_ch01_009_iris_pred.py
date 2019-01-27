# -*- coding: utf-8 -*-
"""
A_ch01_009_iris_pred.py
極簡版鳶尾花品種預測系統
Created on Mon Jun 18 16:14:24 2018
@author: zzjack
"""
import numpy as np
#import joblib module
#conda install -c conda-forge librosa 

from sklearn.externals import joblib 
#將 model file 'iris_knn.pkl' 以 joblib.load() 載入
loadKnnModel=joblib.load('iris_knn.pkl')

#=================================================
#使用者輸入介面:
print("請輸入鳶尾花)樣本尺寸(單位為公分):")
sepal_length=float(input("sepal length in cm (花瓣長):"))
sepal_width=float(input("sepal width in cm (花瓣寬):"))
petal_length=float(input("petal length in cm (花萼長):"))
petal_width=float(input("petal width in cm  (花萼寬):"))
input_list=[sepal_length,sepal_width,petal_length,petal_width]

#將使用者輸入轉成(1,4)的numpy.ndarray
input_array=np.array([input_list])

#以loadKnnModel 對輸入樣本作品種預測
pred=loadKnnModel.predict(input_array)

#建立一個輸出字典 "dict_iris"
dict_iris={0: 'Iris-setosa', 1: 'Iris-versicolor',2: 'Iris-virginica'}

#列印預測結果
#印出預測鳶尾花樣本的品種
print("=========================================")
print("鳶尾花樣本尺寸:")
print("sepal length in cm (花瓣長):",sepal_length," \n",
      "sepal width in cm (花瓣寬):",sepal_width," \n",
     "petal length in cm (花萼長):",petal_length,"\n ",
     "petal width in cm  (花萼寬):",petal_width)
print("預測品種是:",dict_iris[pred[0]])
