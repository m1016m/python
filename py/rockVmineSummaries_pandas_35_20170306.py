# -*- coding: utf-8 -*-
"""
#rockVmineSummaries_pandas_35_20170306.py
Created on Mon Mar  6 14:48:55 2017

@author: zzjack
"""
from urllib.request import urlopen
from urllib.request import urlretrieve
from pandas import DataFrame
import pandas as pd
import sys

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#以urlretrive() function, 將URL target_url抓取到現行目錄,並存為 'sonar.all-data.txt' 檔名
urlretrieve(target_url,"sonar.all-data.txt")

#以 pd.read_csv()將 'sonar.all-data.txt' 讀入成dataframe df1, header=None
#沒有header, 第一行就是資料
df1=pd.read_csv('sonar.all-data.txt',header=None)

#計算column(欄)及index數目(列)
no_of_col=len(df1.columns)
no_of_idx=len(df1.index)

#print 
sys.stdout.write("Number of Rows of Data = " + str(no_of_idx) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(no_of_col))



