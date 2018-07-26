import numpy as np
list_1 = np.arange(0,10,2)    # 生成 0~10, 間隔為 2 的數列
list_2 = np.random.sample(5)  # 隨機生成 5 個數字
print(list_1)
print(list_2)
array_1 = np.random.choice(list_2, (4,3)) # 從 list_1 隨機抽數字來建立 4 * 3 的矩陣
print(array_1)
array_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_2 = np.array([[1+1j,2+2j],[3+3j,4+4j]], dtype=complex)  # 生成複數矩陣 j就是i
array_3 = np.zeros((4,3)) # 生成 4*3, 每個element是 1 的矩陣
array_4 = np.ones((3,4))  # 生成 3*4, 每個element是 1 的矩陣
array_5 = np.eye(3)     # 生成 n階單位矩陣
print(array_2)
print(array_5)
print(array_5.ndim)  # 幾維矩陣
print(array_5.shape) # x * y 矩陣
print(array_5.size)  # 可以觀察用途為何
array_1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(array_1.shape)
print(array_1.reshape((2,6)))  # 改變矩陣維度, 注意他跟 .resize() 會有差異
print(array_1.swapaxes(0,1))   # 維度交換
print(array_1.flatten())
"""
矩陣的組合
np.vstack # 合併兩陣列，增加列
np.hstack # 合併兩陣列，增加欄
np.concatenate() # 合併多陣列
np.newaxis() # 增加矩陣維度用, 一維變二維，二維變三維...
"""
A = np.zeros((1,3))
B = np.ones((1,3))
C = np.array([[3,4,5]])
print(np.vstack((A,B))) # 合併增加列
print(np.hstack((A,B))) # 合併增加欄
print('-'*20)
print(np.concatenate((A,B,C,B), axis=0))
print(np.concatenate((A,B,C,B), axis=1))
# newaxis 的用法
D_1 = np.array([1,2,3,4]) # 一維陣列
print(D_1.shape)

D_2 = D_1[:, np.newaxis]
print(D_2) # 變成 4*1的矩陣了
print(D_2.shape) 

print('-'*20)
D_3 = D_1[np.newaxis,:]
print(D_3) # 變成 1*4 的矩陣了
print(D_3.shape)
"""
矩陣的分割
np.split: 平均分割
np.array_split: 不等量分割
"""
array_1 = np.arange(12).reshape(3,4)

array_2 = np.split(array_1, 2, axis=1)       # 縱向切成 兩個 3*2 矩陣
array_3 = np.array_split(array_1, 3, axis=1) # 縱向切成 3份，第一個會有 (4//3 + 1) = 2欄，其餘的是 4//3 = 1欄
print(array_1)
print(array_2)
print(array_3)
"""
常見運算
np.sqrt()
np.log()
np.abs()
np.sin()
np.dot()
np.max([1,2,3,4])
... 還有很多，要用時再查即可。 後續有需要的話也可以 google numpy 要怎麼取得 特徵值跟特徵向量，或反矩陣與轉置矩陣。
"""

