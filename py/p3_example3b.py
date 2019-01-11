# -*- coding: utf-8 -*-
"""
p3_example3b.py 單字出現頻率統計程式, 使用Counter()與 OrderedDict()
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

#使用Counter() / OrderedDIct
from collections import Counter,OrderedDict
dict5=dict(Counter(words).most_common(5)) #有做出來，但未排序 (字典是無序的)
#dictionary sorted by value
OrderedDict(sorted(dict5.items(), key=lambda t: -t[1]))


    