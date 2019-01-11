# -*- coding: utf-8 -*-
"""
web_scraping_80a_NLTK_20161228.py
Created on Wed Dec 28 16:29:27 2016

@author: zzjack
"""
#re.sub('\n+'," ",input).lower() 說明範例
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string  
import operator 
inputStr="I have a pen\nI have an apple\nUgh\n\nApple pen" 
re.sub('\n+'," ",inputStr) 
re.sub('\n+'," ",inputStr).lower()

#將一或多個new line \n+, 置換為單一空格, 並全改為小寫 .lower()

#-----------------------------------------------------------
inputStr2="I hava [990] a pen I have an apple[001]"
re.sub('[[0-9]*\]',"",inputStr2)

#將 [990], [001]等樣式 消除掉 ""

#-----------------------------------------------------------
inputStr3="I have a    pen I have an        apple"
re.sub(" +"," ",inputStr3)

#將不管幾個空格,縮減為一個空格

#-----------------------------------------------------------
inputStr4="I hava a 筆 I hava an 蘋果"
#encode,編碼 (以utf-8)
inputStr4=bytes(inputStr4,"utf-8") #以utf-8編碼(encode)為byte stream
                                 
inputStr4 #b'I hava a \xe7\xad\x86 I hava an \xe8\x98\x8b\xe6\x9e\x9c'
#decode,解碼
inputStr4.decode("utf-8") #將byte stream
inputStr4.decode("utf-8","ignore")
inputStr4.decode("ascii","ignore") #以accii decode,不是ascii 將被忽略
inputStr4.decode("ascii") #如果未使用"ignore"參數,當有未能解碼之位元組時,會發生錯誤
#----------------------------------------------------------------------------
inputStr5="I hava a 筆 I hava an 蘋果"
#encode,編碼 (以big5)
inputStr5=bytes(inputStr5,"big5") #以big5編碼(encode)為byte stream
inputStr5 #b'I hava a \xb5\xa7 I hava an \xc4\xab\xaaG'
#decode,解碼 (以big5)
inputStr5.decode("big5") #big5
inputStr5.decode("utf-8") #utf-8 如果未使用"ignore"參數,當有未能解碼之位元組時,會發生錯誤
inputStr5.decode("utf-8","ignore") #使用 "ignore" 參數,當有未能解碼之位元組時,會跳過

#---------------------------------------------------------------------
# python string.strip(string.punctuation)
# string.strip() --> The method strip() returns a copy of the string in which all chars have been stripped from the beginning and the end of the string
str01 = "0000000this is 000 string example....wow!!!0000000";
str01.strip("0") #修剪掉前後的 "0"

str02="!!hello! what's your name??"
str02.strip(string.punctuation) #修剪字串前後的標點符號

#------------------------------------------------------------------
#cleanInput(input),getNgrams(input, n) 函數說明:

inputStr="I have a pen I have an apple Ugh Apple pen pineapple"

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

input=cleanInput(inputStr) #叫用cleanInput() function 將inputStr 處理為input
                           #此時 input 是一個 list of 單字   

input #display input list (list of word)
len(input) #input list 長度為 12

#-------------------------------------------------------------------------
inputStr="I have a pen I have an apple Ugh Apple pen pineapple"
input=cleanInput(inputStr) #叫用cleanInput() 處理
output={}               #empty dict. output
n=2
for i in range(len(input)-n+1):  #每n個一組
        ngramTemp=" ".join(input[i:i+n]) #i=0,--> input[0,2]; i=1,-->input[1,3],...
        if ngramTemp not in output:
            output[ngramTemp]=0 #如果output字典裡還沒這組字,將這組字加入字典為key,值為0
        output[ngramTemp]+=1    #如果有這組字(上行新加入的也算)值加1
        
#--------------------------------------------------------------
list2=['a','b','c','a']
d1={}
for i in list2:
    if i not in d1:
        d1[i]=0
    d1[i]+=1
    
d1

#-----------------------------------------------------------------
#sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)

dic02={'aaa':10,'bbb':5,'c':12,'ff':3}
sorted(dic02.items(), key=operator.itemgetter(1))
sorted(dic02.items(), key=operator.itemgetter(1), reverse=True)
sorted(dic02.items(), key=operator.itemgetter(0))
sorted(dic02.items(), key=operator.itemgetter(0), reverse=True)

list03=[['jack',52,'teacher'],['mary',46,'doctor'],['clark',60,'worker']]
sorted(list03, key=operator.itemgetter(1), reverse=True)  
sorted(list03, key=operator.itemgetter(0))      















