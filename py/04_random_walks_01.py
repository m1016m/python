
# coding: utf-8
#04_random_walks_01.py, 隨機漫步說明
#繪圖模式, %pylab / %matplotlib inline

import matplotlib.pyplot as plt
#%pylab

#範例1: 不使用 numpy, 使用 std. liberary 中的 random module
import random #import std. liberary random module
position=0 #設定 position=0

walk=[position] #create list object--> walk

steps=10 #先說明走10步

for i in range(steps):   #range() function
    step=1 if random.randint(0,1) else -1 #random.randint() function, if...else
    position += step
    walk.append(position) #walk.append() method

walk #list walk 內容

plt.plot(walk) #畫這10步

#分解說明, range() 是一個產生器

list(range(10))
list(range(1,10))
list(range(1,10,2))

for i in range(10): #i in [0,1,...,9], 走10步
    print(random.randint(0,1)) #random.randint(0,1) --> 產生0或1的整數

for i in range(10):
    print(random.randint(0,3)) #random.randint(0,3) --> 產生0或1或2或3的整數

for i in range(10):  #走10步
    step=1 if random.randint(0,1) else -1 #如果 random.randint(0,1)值為1(true)-->1
    print(step)                           #如果 random.randint(0,1)值為0(false)-->-1  


for i in range(10):
    step= 1 if random.randint(0,1) else -1
    position+=step #將每步的值累加
    walk.append(position) #放到 list walk 中 (使用 walk.append() method) 


walk

#走1000步
steps=1000

position2=0

walk2=[position2]

for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position2+=step
    walk2.append(position2)

plt.plot(walk2)




