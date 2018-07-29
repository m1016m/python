import numpy as np
import pandas as pd
#http://pyzh.readthedocs.io/en/latest/python-pandas.html
# 若不加後面的index，則index預設是0,1,2,3...
pets = ['Labrador Retriever', 'Beagle', 'Dachshund', 'Shiba Inu']
pets_index = ['Alex', 'Alice', 'Neo', 'Kenny']
series_1 =  pd.Series(pets,index=pets_index)
print(type(series_1))
print(series_1)
print(series_1[0])
print('-'*20)
print(series_1[[0,1,2]])#印出第0 1 2 個
print('-'*20)
print(series_1['Alex'])
print('-'*20)
print(series_1[['Alex','Alice']])
"""
<class 'pandas.core.series.Series'>
Alex     Labrador Retriever
Alice                Beagle
Neo               Dachshund
Kenny             Shiba Inu
dtype: object
Labrador Retriever
--------------------
Alex     Labrador Retriever
Alice                Beagle
Neo               Dachshund
dtype: object
--------------------
Labrador Retriever
--------------------
Alex     Labrador Retriever
Alice                Beagle
dtype: object
"""
print(series_1[1:2]) # 從第2個到第3個
print('-'*20)
print(series_1[:'Neo']) #從第一個 ~ Neo
# 1. 可以直接對兩個Series做加減乘除
price = pd.Series([15,20,40,10])
counts = pd.Series([1,3,5,6])
total_price = price*counts
print(total_price)


num_list = np.random.sample(1000000) # 隨機產生 100000 個數字的陣列, 這個陣列型態是 "numpy 陣列"
pd_series = pd.Series(num_list)
ori_list = list(num_list)  # 把 numpy 陣列轉變為一般 python 的陣列

# 用 傳統的 (for i in ori_list...) 來將兩個list的內容相加的運算時間會是用 pd_series + pd_series 來相加的 100倍

#Dataframe  把字典內容轉換成表格形式
pm25 = [55.4800251788,55.4800551787,55.4160551788,55.4300551788,55.2800551788]
pm10 = [81.6167142157,21.3467142857,81.5467144857,61.6467142857,31.7467142857]
dict = {'pm25': pm25,'pm10':pm10}
df = pd.DataFrame(dict)
print(df)
import pandas as pd

table = [
    [52.4800551788,83.6467142857],
    [51.4800551788,85.6467142857],
    [59.4800551788,87.6467142857],
    [55.4800551788,89.6467142857],
    [57.4800551788,80.6467142857]
]
df = pd.DataFrame(table,columns = ['pm25','pm10'])
print(df)
print('-'*20)
print(df['pm25'])
print('-'*20)
print(df.iloc[0,1]) # 選取第 1 列 (0)，第二欄(1)的數值
print('-'*20)
print(df.iloc[0:2,1]) # 選取第 1 ~ 2 列 (0:2)，第二欄(1)的數值
#pandas 能直接對資料做排序
"""
也能夠合併兩組資料
可使用

.concat: 直接水平或垂直整併兩組資料
join: 若合併時發現資料有缺值，決定是建立一列新的資料或是忽略該資料
.merge: 根據相同欄位內容來合併
.append: 直接將數據增加為新的列
"""
table = [
    [52.4800551788,83.6467142857],
    [51.4800551788,85.6467142857],
    [59.4800551788,87.6467142857],
    [55.4800551788,89.6467142857],
    [57.4800551788,80.6467142857]
]
df = pd.DataFrame(table,columns = ['pm25','pm10'])
df.sort_values(by = 'pm25',ascending=False) # ascending 可調整升降冪

#axis=0 會根據最左側index進行排序, axis=1 會根據最上方欄位名稱(pm25, pm10)從左到右排序, ascending 可調整升降冪
# df.sort_index(axis=1, ascending=False) 
# concat
table_1 = [
    [52.4800551788,83.6467142857],
    [51.4800551788,85.6467142857]
]
table_2 = [
    [59.4800551788,87.6467142857],
    [55.4800551788,89.6467142857],
    [57.4800551788,80.6467142857]
]
df_1 = pd.DataFrame(table_1,columns = ['pm25','pm10'])
df_2 = pd.DataFrame(table_2,columns = ['pm25','pm10'])
# axis=0 -> 合併時新增列, ignore_index=True 將會將最左側 index重置 (否則會是0,1,0,1,2)
df_3 = pd.concat([df_1, df_2], axis=0, ignore_index=True)#axis=0會向下合併 =1會加在旁邊

# 可以取消註解這行試試看igore=False, 最左邊的索引會怎麼跑
# df_3 = pd.concat([df_1, df_2], axis=0, ignore_index=False)

print(df_3)
# join='outer'  np.nan是空直 如果是空的 資料就會9   NaN        NaN         NaN     William         76
#join='inner' 如果是空的 資料就會直接刪除
table_1 = [
    ['A', 'Noah', 90], ['B', 'Liam', 81], ['C', 'William', np.nan], ['B', 'Benjamin.', 82], ['A', 'Emma.', 90],
    ['C', 'Olivia', np.nan], ['A', 'Isabella', 70],
    ['C', 'Amelia', np.nan], ['B', 'Mia', 88],
]
table_2 = [
    ['Liam', 83], ['Benjamin.', 82], ['Emma.', 90], ['Olivia', 89], ['Isabella', 70],
    ['Amelia', 99], ['Mia', 88], ['new_person', 87],['Noah', 92], ['William', 76],
]
df_1 = pd.DataFrame(table_1,columns = ['class','name','math_score'])
df_2 = pd.DataFrame(table_2,columns = ['name','eng_score'])

# axis = 1 -> 合併時新增欄。
df_3 = pd.concat([df_1,df_2], axis=1, join='outer')
# join 預設會是 outer, 若設定inner 則 new_person 這筆資料會被移除
# df_3 = pd.concat([df_1,df_2], axis=1, join='inner')
print(df_3)
#怎麼跟把同樣名子的學生資料也合併?
table_1 = [
    ['A', 'Noah', 90], ['B', 'Liam', 81], ['C', 'William', np.nan], ['B', 'Benjamin.', 82], ['A', 'Emma.', 90],
    ['C', 'Olivia', np.nan], ['A', 'Isabella', 70],
    ['C', 'Amelia', np.nan], ['B', 'Mia', 88],
]
table_2 = [
    ['Liam', 83], ['Benjamin.', 82], ['Emma.', 90], ['Olivia', 89], ['Isabella', 70],
    ['Amelia', 99], ['Mia', 88], ['new_person', 87],['Noah', 92], ['William', 76],
]
df_1 = pd.DataFrame(table_1,columns = ['class','name','math_score'])
df_2 = pd.DataFrame(table_2,columns = ['name','eng_score'])

## 上面都一樣，從下面開始不一樣, 這裡的 inner 跟 outer 意義跟上上一頁的一樣，若放outer 會把有缺值的資料砍掉。
df_3 = pd.merge(df_1,df_2, on='name', how='inner')
print(df_3)
#pandas 也可以直接從網路上讀取資料
# 臺南市健康促進醫院一覽表
url = 'http://data.tainan.gov.tw/dataset/1b89994d-ab2a-4126-ab1e-ed1a0cfaeb27/resource/f169b4d7-11d7-400e-b061-249cf9a2bf34/download/1070612tnhp.csv'
data = pd.read_csv(url, encoding='utf-8')
print(type(data))
# data.to_csv('file_name.csv') 這一行會把剛才的資料存成 csv 檔
data.head() # 取前幾行資料，如果你不是在jupyter notebook打這行外面要加 print ()裡輸入要幾行的資料
print (data.info)
#Pandas 也提供幾種常用的方法來查看你的資料
"""
.shape: 回傳列，欄數。 e.g. (8,7) 
.info: 回傳資料 
.describe(): 回傳統計數字 
.columns: 回傳所有欄位名稱 .index: 回傳索引值，如 0~8 
.head(): 取前面幾行資料 
.tail(): 取後面幾行資料
"""
# 統計數據
print (data.describe())
"""
有時(常常)外部拿到的資料會有空值(沒有給值)，Pandas 亦可以用來判斷資料是否存在空值，並加以處理
判斷空值:
.isnull() 
.notnull() 

處理空值: 
.dropna() 把有空值的那一列資料砍掉
.fillna() 用其他數值把空值補上
"""
# np.nan 是從 numpy 來的，意思是空值，這裡可以先不管他。
table = [
    ['A', 'Noah', 90],
    ['B', 'Liam', 81],
    ['C', 'William', np.nan],
    ['B', 'Benjamin.', 82],
    ['A', 'Emma.', 90],
    ['C', 'Olivia', np.nan],
    ['A', 'Isabella', 70],
    ['C', 'Amelia', np.nan],
    ['B', 'Mia', 88],
]
df = pd.DataFrame(table,columns = ['class','name','score'])

print(df['score'].isnull()) # 列出每一列是不是有空值
# np.nan 是從 numpy 來的，意思是空值。
table = [
    ['A', 'Noah', 90],
    ['B', 'Liam', 81],
    ['C', 'William', np.nan],
    ['B', 'Benjamin.', 82],
    ['A', 'Emma.', 90],
    ['C', 'Olivia', np.nan],
    ['A', 'Isabella', 70],
    ['C', 'Amelia', np.nan],
    ['B', 'Mia', 88],
]
df = pd.DataFrame(table,columns = ['class','name','score'])
new_df = df.fillna(df['score'].mean()) # 把空值用平均分數補上 fillna空值的話要塞什麼
# or new_df = df.fillna({'score': df['score'].mean()}) 也可以傳入字典來選擇 哪些欄位 要用 什麼資料 填補空值

print(new_df)


