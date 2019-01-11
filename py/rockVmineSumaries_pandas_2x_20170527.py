#rockVmineSumaries_pandas_3x_20160227.py
import pandas as pd
from pandas import DataFrame,Series
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import sys

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#使用urlretrieve() 取得target_url(一個*.txt file)並命名為sonar.all-data.txt
urlretrieve(target_url,"sonar.all-data.txt")

#使用 pd.read_csv() 將'sonar.all-data.txt' 讀入為 DataFrame df1,
#header=None, 因原始資料無title, 第一行即是資料
df1=pd.read_csv('sonar.all-data.txt',header=None)

#檢視 DataFrame df1
df1

#計算df1 的column,index 數
cols_of_df1=len(df1.columns)
index_of_df1=len(df1.index)

#display 
sys.stdout.write("Number of Rows of Data = " + str(index_of_df1) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(cols_of_df1))

