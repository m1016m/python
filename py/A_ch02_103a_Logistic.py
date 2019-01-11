# -*- coding: utf-8 -*-
"""
A_ch02_103a_Logistic.py
"""
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib
#define sigmoid/logistic function
def sigmod(z):
    return 1.0 / (1.0 + np.exp(-z))
    
#給定輸入 z 
z = np.arange(-7,7,0.1)

#以z對sigmod(z)作圖
plt.plot(z,sigmod(z))
plt.axvline(0.0, color='k')
plt.ylim(-0.1,1.1)
plt.xlabel('z')
plt.ylabel('sigmod(z)')
plt.yticks([0.0,0.5,1.0])
plt.grid()
plt.show()

