#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:03:18 2018

@author: shuhuimeng
"""
'''
冷知識：scikit-learn 源於於 SciPy，事實上 scikit 有很多個，我們使用的 scikit-learn 

套件是專門用來實作機器學習以及資料採礦的，這也是為什麼使用 learn 來命名:)，這個套件提供了大量常見演算法高效能版本，簡潔，一致，最新的API

我們首先由 sklearn 套件載入 datasets 模組，然後使用 datasets 模組的 load_digits() 

方法來輸入資料，試著依照註解的提示完成程式後點選 Run 觀察結果

datasets 模組還有其他讀取資料的方法，您也可以用它來產生虛擬資料。我們現在所使用的資料集 

digits 也可以從加州大學 Irvine 分校的機器學習資料集載入，您可以在這個

http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/找到。

假如您想要從加州大學 Irvine 分校的機器學習資料集載入 digits，讀入資料的程式寫法會變得像這樣

digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)

，試著依照註解的提示完成程式後點選 Run 觀察結果

值得注意的是，從檔名的 .tra 與 .tes 可以得知，加州大學 Irvine 分校的機器學習資料集已經切分好訓練與測試資料，而上面這段程式中我們只讀入了訓練資料，如果要實作機器學習則還需要再讀入測試資料，

秘訣：想學習更多使用 Python 的 Pandas 套件來讀入與整理資料的技巧，可以參閱 Importing Data in Python course。

探索資料
仔細閱讀資料的文件或描述是很好的習慣，加州大學 Irvine 分校的機器學習資料集針對每個資料都有提供文件，閱讀文件可以提高我們對資料的瞭解程度。然而光是初步認識還是略嫌不足，接著我們要進行的是探索性分析（Exploratory data analysis），我們又該從何開始探索這些手寫數字圖片資料呢？

搜集基本資訊
假如我們直接透過 scikit-learn 讀入 digits 資料，那麼不同於加州大學 Irvine 分校的機器學習資料集在網頁中提供描述或文件，我們必須另外透過使用 digits 的屬性與方法來搜集基本資訊。

我們將透過 digits 的 keys() 方法來得知有哪些基本資訊可以搜集；透過 data 屬性觀察預測變數；透過 target 屬性觀察目標變數；透過 DESCR 屬性閱讀資料的描述文件。

'''

# 從 `sklearn` 載入 `datasets`
from sklearn import datasets
# 載入 matplotlib
import matplotlib.pyplot as plt

# 載入 `digits`
digits = datasets.load_digits()

# 設定圖形的大小（寬, 高）
fig = plt.figure(figsize=(4, 2))

# 調整子圖形 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# 把前 8 個手寫數字顯示在子圖形
for i in range(8):
    # 在 2 x 4 網格中第 i + 1 個位置繪製子圖形，並且關掉座標軸刻度
    ax = fig.add_subplot(2, 4, i + 1, xticks = [], yticks = [])
    # 顯示圖形，色彩選擇灰階
    ax.imshow(digits.images[i], cmap = plt.cm.binary)
    # 在左下角標示目標值
    ax.text(0, 7, str(digits.target[i]))

# 顯示圖形
plt.show()
'''
這段程式看起來有點難懂，讓我們分開來看：

載入 matplotlib 套件。
設定一個長 2 吋，寬 4 吋的空白畫布，準備待會將子圖形畫在上面。
調整子圖形的一些參數。
使用一個 for 迴圈開始要將空白畫布填滿。
初始化 8 個子圖形，並依序填入 2 x 4 網格中的每一格。
最後畫龍點睛的部分是在每個子圖形 (0, 7) 的位置（左下角）顯示目標值。
別忘了使用 plt.show() 將畫好的圖顯示出來！
'''
#或者採取這段較簡潔的程式：
'''
在這個例子中，我們將兩個陣列存入 images_and_labels 這個變數，然後將這個變數中的前 8 個元素

（包含 digits.images 與相對應的 digits.target）在一個 2 x 4 的格線上繪製子圖形，並且使用 

plt.cm.binary 這個灰階色彩，搭配子圖形標題顯示出來。

經過這兩個視覺化練習之後，您應該對目前手上處理的 digits 資料有更深的認識！

視覺化：主成份分析（Principal Component Analysis, PCA）
digits 資料有 64 個變數，面對這種高維度的資料（實務上還有其他很多像是財務或者氣候資料也都屬於高維度資料）

，我們需要用一些方法找出特別重要的二到三個變數，或者將許多的變數組合成讓我們更容易理解且視覺化的幾個維度。

這種方法稱作降維（Dimensionality Reduction），我們接著要使用其中一種方法稱為：主成份分析

（Principal Component Analysis, PCA）來協助我們視覺化 digits 資料。主成份分析的精神在於找出變數之間的

線性關係組成新的一個主成份，然後使用這個主成份取代原有的變數，屬於一種最大化資料變異性的線性轉換方法
'''
# 從 `sklearn` 載入 `datasets`
from sklearn import datasets
# 載入 matplotlib
import matplotlib.pyplot as plt

# 載入 `digits`
digits = datasets.load_digits()

# 將觀測值與目標值放入一個 list
images_and_labels = list(zip(digits.images, digits.target))

# list 中的每個元素
for i, (image, label) in enumerate(images_and_labels[:8]):
    # 在 i + 1 的位置初始化子圖形
    plt.subplot(2, 4, i + 1)
    # 關掉子圖形座標軸刻度
    plt.axis('off')
    # 顯示圖形，色彩選擇灰階
    plt.imshow(image, cmap = plt.cm.binary)
    # 加入子圖形的標題
    plt.title('Training: ' + str(label))

# 顯示圖形
plt.show()

# 建立 K-Means 模型
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import numpy as np
from sklearn import cluster

digits = datasets.load_digits()
data = scale(digits.data)
X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, digits.target, digits.images, test_size=0.25, random_state=42)
clf = cluster.KMeans(init='k-means++', n_clusters=10, random_state=42)
clf.fit(X_train)

# 載入 matplotlib
import matplotlib.pyplot as plt

# 設定圖形的大小
fig = plt.figure(figsize=(8, 3))

# 圖形標題
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

# 對所有的目標值（0 - 9）
for i in range(10):
    # 在 2x5 的網格上繪製子圖形
    ax = fig.add_subplot(2, 5, i + 1)
    # 顯示圖片
    ax.imshow(clf.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
    # 將座標軸刻度關掉
    plt.axis('off')

# 顯示圖形
plt.show()

#接著我們來將預測的目標值視覺化：

# 建立 K-Means 模型
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import numpy as np
from sklearn import cluster
# 載入 `Isomap()`
from sklearn.manifold import Isomap

digits = datasets.load_digits()
data = scale(digits.data)
X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(data, digits.target, digits.images, test_size=0.25, random_state=42)
clf = cluster.KMeans(init='k-means++', n_clusters=10, random_state=42)
clf.fit(X_train)

# 使用 Isomap 對 `X_train` 資料降維
X_iso = Isomap(n_neighbors=10).fit_transform(X_train)

# 使用 K-Means 演算法
clusters = clf.fit_predict(X_train)

# 在 1x2 的網格上繪製子圖形
fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# 調整圖形的外觀
fig.suptitle('Predicted Versus Training Labels', fontsize=14, fontweight='bold')
fig.subplots_adjust(top=0.85)

# 加入散佈圖 
ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=clusters)
ax[0].set_title('Predicted Training Labels')
ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=y_train)
ax[1].set_title('Actual Training Labels')

# 顯示圖形
plt.show()
#視覺化手寫數字圖片與預測的結果：

# 使用 SVC 演算法
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.preprocessing import scale
from sklearn import cluster
digits = datasets.load_digits()
data = scale(digits.data)

X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(digits.data, digits.target, digits.images, test_size=0.25, random_state=42)
from sklearn import svm
svc_model = svm.SVC(gamma=0.001, C=100., kernel='linear')
svc_model.fit(X_train, y_train)

# 載入 matplotlib
import matplotlib.pyplot as plt

# 將預測結果指派給 `predicted`
predicted = svc_model.predict(X_test)

# 將 `images_test` 與 `predicted` 存入 `images_and_predictions`
images_and_predictions = list(zip(images_test, predicted))

# 繪製前四個元素
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    # 在 1x4 的網格上繪製子圖形
    plt.subplot(1, 4, index + 1)
    # 關掉座標軸的刻度
    plt.axis('off')
    # 色彩用灰階
    plt.imshow(image, cmap=plt.cm.binary)
    # 加入標題
    plt.title('Predicted: ' + str(prediction))

# 顯示圖形
plt.show()

#我們很明顯地看出 SVC 表現得比先前的 K-Means 分群好得太多，接著我們利用 Isomap() 視覺化預測結果與目標值：

# 使用 SVC 演算法
from sklearn import datasets
from sklearn.preprocessing import scale
from sklearn import cluster
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

digits = datasets.load_digits()
data = scale(digits.data)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test, images_train, images_test = train_test_split(digits.data, digits.target, digits.images, test_size=0.25, random_state=42)
from sklearn import svm
svc_model = svm.SVC(gamma=0.001, C=100., kernel='linear')
svc_model.fit(X_train, y_train)

# 對 `digits` 資料降維
X_iso = Isomap(n_neighbors=10).fit_transform(X_train)

# 使用 SVC 演算法
predicted = svc_model.predict(X_train)

# 在 1x2 的網格上繪製子圖形
fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# 調整外觀
fig.subplots_adjust(top=0.85)

# 繪製散佈圖 
ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=predicted)
ax[0].set_title('Predicted labels')
ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=y_train)
ax[1].set_title('Actual Labels')

# 加入標題
fig.suptitle('Predicted versus actual labels', fontsize=14, fontweight='bold')

# 顯示圖形
plt.show()










