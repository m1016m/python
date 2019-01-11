# -*- coding: utf-8 -*-
"""
08_Plotting_a01_20161003.py
Created on Mon Oct  3 08:58:54 2016

@author: zzjack
"""
#Plotting and Visualization
#matplotlib, mplot3d, basemap

import pandas as pd
from pandas import DataFrame,Series
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
#%pylab 

#example 1: a simple case
plot(np.arange(10))

close() #關閉視窗

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Figure and Subplot:
#matplotlib 的繪圖都在 Figure Object 上
plt.figure() #create a Figure Object, pop a empty windows
plt.figure(2) #編號
plt.gcf() #get a reference to the active figure

#You can’t make a plot with a blank figure. 
#You have to create one or more subplots using add_subplot:
#example 2: add_subplot() 
fig=plt.figure() #create a Figure Object and named fig
ax1=fig.add_subplot(2,2,1) #在fig上,create 2x2 subplot 中的第一個
ax2=fig.add_subplot(2,2,2) #no. 2
ax3=fig.add_subplot(2,2,3) #no. 3

#在最後一個用過的subplot (ax3) 上繪圖
plt.plot(randn(50).cumsum(),'k--') #'k--',黑色虛線

#或直接叫用subplot物件的繪圖method
ax1.hist(randn(100),bins=20, color='r',alpha=0.3) #hist, Plot a histogram.
#                                                  http://matplotlib.org/api/axes_api.html?highlight=hist#matplotlib.axes.Axes.hist        

ax2.scatter(np.arange(30),np.arange(30)+3*randn(30)) 
#scatter,Make a scatter plot of x vs y, where x and y are sequence like objects of the same length.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#there is a convenience method, plt.subplots, that creates a new figure
#and returns a NumPy array containing the created subplot objects: 
#example 3:plt.subplots()
f, axes=plt.subplots(2,3) #create a 2x3 ndarray of subplt

#axes[0,0], plot()
axes[0,0].plot(randn(100))

#axes[0,1], scatter()
axes[0,1].scatter(np.arange(30),np.arange(30)+3*randn(30))

#axes[0,2], hist(), histogram
axes[0,2].hist(randn(100),bins=10,color='g',alpha=0.2)

#axes[1,0]
t=np.arange(0.0, 2.0, 0.01)
s=np.sin(2*np.pi * t)
axes[1,0].plot(t,s)







