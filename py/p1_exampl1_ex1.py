# -*- coding: utf-8 -*-
"""
p1_exampl1_ex1.py
Created on Sun Mar 18 10:42:30 2018
@author: zzjack
"""
import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0, 2*np.pi, 0.1)
plt.figure(1)
plt.plot(t, np.sin(t))

plt.show()
