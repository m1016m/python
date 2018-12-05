# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 09:54:41 2018

@author: zzjack
"""
#1.1 IPython, Jupyter, and matplotlib modes
#For interactive matplotlib sessions, turn on the matplotlib mode
#IPython console use:
%matplotlib

#Jupyter notebook:
%matplotlib inline 

#----------------------------------------------------------------
#1.2 pyplot
#pyplot provides a procedural interface to the matplotlib object-oriented plotting library.
from matplotlib import pyplot as plt

#----------------------------------------------------------------
#2 Simple plot
#we want to draw the cosine and sine functions on the same plot.
import numpy as np
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)
plt.show()

#----------------------------------------------------------------
#3 Create a figure
# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(2, 2, 1) 

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot cosine with a blue continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

plt.subplot(2,2, 2)
plt.plot(X, C, color="red", linewidth=2.0, linestyle="--")

# Set x limits
plt.xlim(-4.0, 4.0)
# Set x ticks
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Set y limits
plt.ylim(-1.0, 1.0)
# Set y ticks
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

plt.show()
