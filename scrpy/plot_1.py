#設置軸標籤
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.tools as tls
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api


mpl_fig = plt.figure()#使用plt.figure定义一个图像窗口
ax = mpl_fig.add_subplot(111)#畫子圖
'''
单个整数编码的子绘图网格参数。例如，“111”表示“1×1网格，第一子图”，“234”表示“2×3网格，第四子图”。
add_subplot(111)的替代形式是add_subplot(1,1,1)。

https://i.stack.imgur.com/AEGXG.png

子图：就是在一张figure里面生成多张子图。

Matplotlib对象简介

   FigureCanvas  画布

   Figure        图

   Axes          坐标轴(实际画图的地方)

'''

plt.plot([1,2,3,4])
#plotly_fig = tls.mpl_to_plotly(fig)#將matplotlib圖形轉換為Plotly圖形對象mpl_to_plotly

plt.show()