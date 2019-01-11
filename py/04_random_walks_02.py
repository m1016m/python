
# coding: utf-8

#04_random_walks_02.ipynb,隨機漫步說明,使用numpy
import numpy as np #import numpy module as alias np
import matplotlib.pyplot as plt #import matplotlib

get_ipython().magic('matplotlib inline')

nsteps=1000 #設定 1000 步

draws=np.random.randint(0,2,size=nsteps) #產生1000個 0或1 的numpy.ndarray object draws

steps=np.where(draws > 0,1,-1) #以np.where() function將 draws中 1-->1, 0-->-1

walk=steps.cumsum() #method cumsum() 

#繪圖

plt.plot(walk)

#利用min()/max() method, 求最小/最大值,隨機漫步統計分析
walk.min() #利用 min() method, 求最小值

walk.max() #利用 max() method, 求最大值

# 隨機漫步統計分析 複雜範例: first crossing time

(np.abs(walk) >= 10).argmax() #np.abs() function 逐一求 walk 中元素絕對值
                              #(np.abs(walk)>=10) 將傳回 True or False
                              #第一個 True 的索引值,以 argmax() method 求出   

#example3: Simulating Many Random Walks at Once
nwalks=5000 #5000 個隨機漫步
nsteps=1000 #1000 步

draws=np.random.randint(0,2,size=(nwalks,nsteps)) # 5000x1000 ndarray, 元素值為0 or 1 

steps=np.where(draws>0,1,-1) #將 0-->-1, 1-->1

walks=steps.cumsum(1) #沿 axis1 cumsum, (每一個隨機漫步,共5000個)

walks #每一個隨機漫步,共5000個

plt.plot(walks[0]) #把第一個隨機慢步畫出來看
#統計所有隨機漫步,walks 中 max/min

walks.max()

walks.min()

#first crossing time,compute the minimum crossing time to 30 or -30
#但並不是所有5000次皆有穿越30,需先使用any() methond 檢驗

hits30=(np.abs(walks)>=30).any(1) #any(1), 沿axis1 使用 any(), 
                                  #即檢查每次隨機漫步中 有任一穿越30者為true
                                  #共檢查5000次

hits30 #一個布林值陣列, 大小為 5000
hits30.sum() #統計true (穿越30) 的個數

crossing_times=(np.abs(walks[hits30])>=30).argmax(1) #每個穿越點
                                                     #說明-->999

crossing_times

crossing_times.mean() #求平均

#用其他分布方式得到漫步數據,如 numpy.random.normal() 


steps2=np.random.normal(loc=0,scale=0.25,size=(nwalks,nsteps))


#999 --> 分解說明 (np.abs(walks[hits30])>=30).argmax(1) 
walks #5000x1000, axis1是已經cumsum,
hits30 #布林陣列

walks[hits30] #walks陣列與 hits30布林陣列運算, true的元素才出現

crossing_times=(np.abs(walks[hits30])>=30).argmax(1) #argmax(1),沿著axis1
                                                     #找到第一個穿越30元素的 index
                                                     #每一個axis0 會找到一個,共3399
                                                     #個,形成一個一維陣列

crossing_times



