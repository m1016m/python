# -*- coding: utf-8 -*-
"""
web_scraping_80_NLTK_20161228.py
Created on Wed Dec 28 10:22:52 2016
@author: zzjack
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string  #Common string operations, 'https://docs.python.org/3.4/library/string.html'
import operator  #python operator module, 'https://docs.python.org/3.5/library/operator.html'

#尋找2-grams組別,使用Python operator module 排序
def cleanInput(input):
    input=re.sub('\n+'," ",input).lower() #re.sub(pattern, repl, string, count=0, flags=0)
    input=re.sub('[[0-9]*\]',"",input)
    input=re.sub(' +'," ",input)  #將不管幾個空格,縮減為一個空格
    input=bytes(input,"utf-8")
    input=input.decode("ascii","ignore") #以accii decode,不是ascii 將被忽略
    cleanInput=[] #empty list cleanInput
    input=input.split(' ') #將前面已處理為單一空格字串，分割為單字串列
    for item in input:
        item=item.strip(string.punctuation) #修剪字串前後的標點符號
        if len(item) > 1 or (item.lower() == 'a' or item.lower()== 'i'):
            cleanInput.append(item) 
    return cleanInput
        
def getNgrams(input, n):
    input=cleanInput(input) #叫用cleanInput() 處理
    output={}               #empty dict. output
    for i in range(len(input)-n+1):  #每n個一組
        ngramTemp=" ".join(input[i:i+n]) #i=0,--> input[0,2]; i=1,-->input[1,3],...
        if ngramTemp not in output:
            output[ngramTemp]=0 #如果output字典裡還沒這組字,將這組字加入字典為key,值為0
        output[ngramTemp]+=1    #如果有這組字(上行新加入的也算)值加1
    return output

#執行 2-grams        
content=str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
ngrams=getNgrams(content, 2)
#sorted() function , 排序依據 key
sortedNGrams=sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)

#自動且準確的移除不感興趣的單字
#http://corpus.byu.edu/coca/
#Just the first 100 words vastly improves the results, with the addition of an isCommon function:
def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", 
           "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
           "they", "is", "an", "at", "but","we", "his", "from", "that", "not",
           "by", "she", "or", "as", "what", "go", "their","can", "who", "get",
           "if", "would", "her", "all", "my", "make", "about", "know", "will",
           "as", "up", "one", "time", "has", "been", "there", "year", "so",
           "think", "when", "which", "them", "some", "me", "people", "take",
           "out", "into", "just", "see", "him", "your", "come", "could", "now",
           "than", "like", "other", "how", "then", "its", "our", "two", "more",
           "these", "want", "way", "look", "first", "also", "new", "because",
           "day", "more", "use", "no", "man", "find", "here", "thing", "give",
           "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False






#說明範例: web_scraping_80a_NLTK_20161228.py
