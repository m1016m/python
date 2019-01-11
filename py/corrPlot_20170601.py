__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#calculate correlations between real-valued attributes
dataRow2 = rocksVMines.iloc[1,0:60] #第二列 instance 2 (第二份樣本) 
dataRow3 = rocksVMines.iloc[2,0:60] #第三列 instance 3 (第三份樣本)

#我們關心的應是屬性 V1與V2間的關聯性:
dataCol2=rocksVMines.iloc[:,1] #屬性 V2
dataCol3=rocksVMines.iloc[:,2] #屬性 V3  
plot.scatter(dataCol2,dataCol3)

plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()   
#或是以series.corr() method
dataCol2.corr(dataCol3)  #V2 與 V3 相關性 0.77991587191042633
#-----------------------------------------------------------
#屬性 V1與V21間的關聯性:
dataCol21=rocksVMines.iloc[:,20] #屬性 V21    
plot.xlabel("2nd Attribute")
plot.ylabel(("21rd Attribute"))
plot.show()

dataCol2.corr(dataCol21) #V2 與 V21 相關性 0.075255286791170051
