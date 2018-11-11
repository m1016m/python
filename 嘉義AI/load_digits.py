#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:12:34 2018

@author: shuhuimeng
"""

# Import the `pandas` library as `pd`
import pandas as pd
from sklearn import datasets

# Load in the data with `read_csv()`
digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)

# Print out `digits`
print(digits)
'''
值得注意的是，從檔名的 .tra 與 .tes 可以得知，加州大學 Irvine 分校的機器學習資料集已經切分好訓練與測試資料，而上面這段程式中我們只讀入了訓練資料，
如果要實作機器學習則還需要再讀入測試資料
'''
# 從 `sklearn` 載入 `datasets`
from sklearn import datasets
# 載入 matplotlib
import matplotlib.pyplot as plt

# 載入 `digits`
digits = datasets.load_digits()

# 設定圖形的大小（寬, 高）
fig = plt.figure(figsize=(4, 2))

# 調整子圖形 使用plt.subplots_adjust更改子圖之間的間距
'''
left = 0.125＃該圖的子圖的左側
right = 0.9＃該圖的子圖的右側
bottom = 0.1＃該圖的子圖的底部
top = 0.9＃該圖的子圖的頂部
wspace = 0.2＃為子圖之間的空白區域保留的寬度量
hspace = 0.2＃為子圖之間的空白區域保留的高度
'''
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# 把前 8 個手寫數字顯示在子圖形
for i in range(10):
    # 在 2 x 4 網格中第 i + 1 個位置繪製子圖形，並且關掉座標軸刻度
    ax = fig.add_subplot(2, 4, i + 1, xticks = [], yticks = [])
    # 顯示圖形，色彩選擇灰階
    ax.imshow(digits.images[i], cmap = plt.cm.binary)
    # 在左下角標示目標值
    ax.text(0, 7, str(digits.target[i]))

# 顯示圖形
plt.show()