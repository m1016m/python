#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:56:08 2018

@author: shuhuimeng
"""
"""
我们训练好了一个Model 以后总需要保存和再次预测, 所以保存和读取我们的
sklearn model也是同样重要的一步。这次主要介绍两种保存Model的模块pickle与joblib。
"""
import pickle
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn import datasets

# 定义分类器
svm = SVC()

# 加载iris数据集
iris = datasets.load_iris()
# 读取特征
X = iris.data
# 读取分类标签
y = iris.target

# 训练模型
svm.fit(X, y)

# 第一种：保存成python支持的文件格式pickle, 在当前目录下可以看到svm.pickle
with open('svm.pickle', 'wb') as fw:
    pickle.dump(svm, fw)
# 加载svm.pickle
with open('svm.pickle', 'rb') as fr:
    new_svm = pickle.load(fr)
    print (new_svm.predict(X[0:1]))
    
    
# 第二种：保存成sklearn自带的文件格式
joblib.dump(svm, 'svm.pkl')
# 加载svm.pkl
new_svm = joblib.load('svm.pkl')
print (new_svm.predict(X[0:1]))

