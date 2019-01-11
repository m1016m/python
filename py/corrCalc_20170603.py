import pandas as pd
from pandas import DataFrame
from math import sqrt
import sys
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#從DataFrame rocksVMines 擷取欄位(屬性) "V1","V2","V20"
attr2=rocksVMines["V1"]
attr3=rocksVMines["V2"]
attr21=rocksVMines["V21"]

#計算屬性值"V1"與"V2"間的Pearson關聯性係數
corr23=attr2.cor
corr23 #0.77991587191042633

#計算屬性值"V1"與"V21"間的Pearson關聯性係數
corr221=attr2.corr(attr21,method='pearson')
corr221 #-0.074157217628683797

#------------------------------------------------------
#計算樣本(row)間的Pearson關聯性係數 (原書有誤?)
row2=rocksVMines.iloc[1,0:60]
row3=rocksVMines.iloc[2,0:60]
row21=rocksVMines.iloc[20,0:60]

#使用astype() 將資料型別轉為 float (corr() 不支援原資料型別 np.float64)
row2=row2.astype(float)
row3=row3.astype(float)
row21=row21.astype(float)

corr23=row2.corr(row3,method='pearson')
corr221=row2.corr(row21,method='pearson')

sys.stdout.write("Correlation between attribute 2 and 3 \n")
print(corr23)
sys.stdout.write(" \n")

sys.stdout.write("Correlation between attribute 2 and 21 \n")
print(corr221)
sys.stdout.write(" \n")


# Output:
# Correlation between row 2 and 3
# 0.770938121191
#
# Correlation between row 2 and 21
# 0.466548080789