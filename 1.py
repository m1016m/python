import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np

lena = mpimg.imread('1.jpg') 

lena.shape (10, 10, 3)


lena_1 = lena[:,:,0]
plt.imshow('lena_1')
plt.show()

plt.imshow('lena_1', cmap='Greys_r')

img = plt.imshow('lena_1')
img.set_cmap('gray') 

plt.axis('off')
plt.show()




