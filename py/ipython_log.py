# IPython log file

#IPython Basics
a=5
a
import numpy as np
from numpy.random import randn
data={i:randn() for i in range(7)}
#字典生成式, 生成式
data
print(data)
#Tab Completion
an_apple=29
an_pen=39
b=[1,2,4,6] #list b
b
import datetime
get_ipython().magic('run 03_IPython_test01.py')
get_ipython().magic('run 03_IPython_test02.py')
get_ipython().magic('run 03_IPython_test02.py 5 6 7')
import numpy as np
a=np.random.randn(100,100) #ndarray a (100x100)
a
get_ipython().magic('timeit np.dot(a,a) #%timeit 檢視矩陣相乘 np.dot(a,a) 花費時間')
get_ipython().magic('magic #有哪些 Magic Commands')
get_ipython().magic('whos #目前變數(Variable)')
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
img=plt.imread('IMG060.jpg')
img=plt.imread('IMG060.jpg')
plt.imshow(img)
plt.plot(randn(1000).cumsum())
get_ipython().magic('hist #印出歷史指令')
get_ipython().magic('logstart')
get_ipython().magic('hist #印出歷史指令')
get_ipython().system('dir ')
get_ipython().system('type t1.py ')
get_ipython().system('type t1.py ')
