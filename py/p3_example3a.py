# -*- coding: utf-8 -*-
"""
p3_example3a.py 單字出現頻率統計程式
Created on Wed Aug 16 14:52:14 2017
@author: zzjack
"""
import re #import regular expression module
fp=open('sample.txt','r') #以'r',read model 開啟 sample.txt
article=fp.read() #以read() method 讀進 str article
article #檢視 article

#將非英文字母的字元移除,空白保留
#re [^a-zA-Z\s] ^a-zA-Z,只要不是英文字母或不是 \s 空白
new_article=re.sub("[^a-zA-Z\s]","",article)

new_article #檢視 new_article

#用str.split() method 分割成一個個單字
words=new_article.split() #words 是 list of str

#create a empty dict, word_counts
word_counts={}

#下面這一段，你要真的懂 python dictionary，才寫得出來
for w in words:
    if w.upper() in word_counts:
        word_counts[w.upper()]=word_counts[w.upper()]+1
    else:
        word_counts[w.upper()]=1
        
word_counts #檢視 dict word_counts
#將字典 word_counts 依值排序, key=lambda x: (-x[1], x[0]), 回傳值是 list of tuple
w_list=sorted(word_counts.items(), key=lambda x: (-x[1], x[0])) 
sorted_word_counts=dict(w_list[:5]) #擷取前五個元素,轉成字典
sorted_word_counts  #檢視     