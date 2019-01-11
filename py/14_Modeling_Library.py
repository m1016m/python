# -*- coding: utf-8 -*-
"""
14_Modeling_Library.py
"""
#--------------------------------------------------------------
#turn a DataFrame into a NumPy array, use the .values property.
import pandas as pd
import numpy as np
#crate DataFrame 'data'
data = pd.DataFrame({
             'x0': [1, 2, 3, 4, 5],
             'x1': [0.01, -0.01, 0.25, -4.1, 0.],
             'y': [-1.5, 0., 3.6, 1.3, -2.]})

data #display DataFrame 'data'    
data.columns #colums of DataFrame 'data'

#----------------------------------------------------------------
#turn DataFrame 'data' into Numpy array 'ar1'
ar1=data.values        
ar1 #array

#turn a two-dimensional ndarray 'ar1' into DataFrame 'data2' with
#columns=['one', 'two', 'three'] 
data2=pd.DataFrame(ar1,columns=['one', 'two', 'three'])
data2 #display DataFrame 'data2'

#---------------------------------------------------------------
#如果資料值不是 homogeneous, dtype=object
data3=data.copy() #複製一個 DataFrame 'data3'
data3['str'] = ['a', 'b', 'c', 'd', 'e'] #data3新增一個column 'str'
data3 #heterogeneous data,dtype=object
ar2=pd.DataFrame(data3.values) #還是可以轉成DataFrame

#--------------------------------------------------------------
#如果你只是要裁DataFrame的部分欄位(column),使用loc indexing
data3
sub_col=['x0','x1','y']
ar3=data3.loc[:,sub_col].values
ar3

#=============================================================
#pandas’s Categorical type and the pandas.get_dummies function.
data
#增加一個['category']欄位
data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'],
                                  categories=['a', 'b'])
data  
#replace the 'category' column with dummy variables
#以pd.get_dummies() 建立DataFrame 'dummies'
dummies = pd.get_dummies(data.category, prefix='category')                                 
dummies
#將column 'category' drop, join dummies
data_with_dummies = data.drop('category', axis=1).join(dummies)
data_with_dummies
                                  
#--------------------------------------------------------------------
#Categorical 物件說明
raw_cat = pd.Categorical(["a","b","c","a"], categories=["b","c","d"],
                         ordered=False)
type(raw_cat) #pandas.core.categorical.Categorical
s = pd.Series(raw_cat)
s                                

































             