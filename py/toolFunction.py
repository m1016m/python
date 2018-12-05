# -*- coding: utf-8 -*-
"""
toolFunction.py
Created on Fri Jan  5 13:54:21 2018
@author: III
"""
#建立 read_files() 函數讀取IMDb檔案目錄
import os
import re
import matplotlib.pyplot as plt

#將MNIST images 資料以圖形顯示
#定義繪圖函數 plot_image()
def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap='binary')
    plt.show()
	
#建立看多筆資料函數 plot_images_labels_prediction()
def plot_images_labels_prediction(images,labels,prediction,idx,num=10):
    fig=plt.gcf() 
    fig.set_size_inches(12,14)      #設定顯示圖形為12"x14" 
    if num>25: num=25               #如果顯示筆數大於25,就設定為25
    for i in range(idx,num):          #畫出num個數字圖形
        ax=plt.subplot(5,5,1+i)     #subplot(nrows, ncols, plot_number), plot_number starts at 1, increments across rows first and has a maximum of nrows * ncols.
        ax.imshow(images[idx], cmap='binary') #show 第 [idx] 個 images, colormap='binary'
        title="label="+str(labels[idx])       #此一subplot抬頭為對應的label值
        if len(prediction)>0:                      #如果呼叫此函數時,有給定預測值prediction (a list)
            title+=",predit="+str(prediction[idx]) #   在抬頭加上對應的預測值 prediction[idx]
        
        ax.set_title(title,fontsize=10)  #設定subplot ax 的 title
        ax.set_xticks([]);ax.set_yticks([]) #set_xticks(ticks, minor=False), Set the x ticks with list of ticks, 此處[]為不設定刻度
        idx+=1
    plt.show()  

#顯示(繪圖)訓練過程,show_train_history
#讀取 train_history 中 loss 與 accuracy, 繪圖
def show_train_history(train_history,train,validation):  #define a function 'show_train_history'
    plt.plot(train_history.history[train])              #train_history.history 是一個 dict
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'],loc='upper left')
    plt.show()

#建立 rm_tag() function 移除文字中的 html tag
def rm_tag(text):
    re_tag=re.compile(r'<[^>]+>') #規則表示式 r'<[^>]+>', r--> 跳脫 '跳脫字元'    
    return re_tag.sub('',text)   #將符合規則表示式的字移除(置換成空字串)

def read_files(filetype): #filetype: 1.train, 2.test
    path="data/aclImdb/"
    file_list=[]  #empty list 'file_list'
    
    positive_path=path+filetype+"/pos/"  #"data/aclImdb/train/pos/" or "data/aclImdb/test/pos/" 
    for f in os.listdir(positive_path):
        file_list+=[positive_path+f]
        
    negative_path=path+filetype+"/neg/" #"data/aclImdb/train/neg/" or "data/aclImdb/test/neg/" 
    for f in os.listdir(negative_path):
        file_list+=[negative_path+f]
    
    print('read',filetype,'files:',len(file_list))
    
    all_labels=([1]*12500+[0]*12500)  #產生12500個1+12500個0的 list 'all_labels'
    
    all_texts=[] #empty list 'all_texts'
    for fi in file_list:  #對目前 list 'file_list' 做迭代處理
        with open(fi, encoding='utf8') as file_input: #以 with open() 逐個開啟檔案
            all_texts+=[rm_tag(" ".join(file_input.readlines()))] #說明1
    
    return all_labels,all_texts