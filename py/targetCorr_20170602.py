import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plot
from random import uniform
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#change the targets to numeric values

import numpy as np #import numpy
target=Series(rocksVMines["V60"]) #從DataFrame rocksVMines 擷取
                                  #["V60"] --> Series object
#使用np.where() 將Series target 'M'-->1.1, 'R'-->0.0
target01=Series(np.where(target=='M',1.0,0.0)) 

#擷取屬性['V35']    
dataRow35 = rocksVMines.iloc[:,35]

#繪製 屬性 'V35' 對 target 的散佈圖
plot.scatter(dataRow35, target01)

plot.xlabel("Attribute Value,V35")
plot.ylabel("Target Value,V60")
plot.show()

#
#To improve the visualization, this version dithers the points a little
# and makes them somewhat transparent
target02 = []
for i in range(208):
    #assign 0 or 1 target value based on "M" or "R" labels
    # and add some dither
    if rocksVMines.iat[i,60] == "M":
        target02.append(1.0 + uniform(-0.1, 0.1))
    else:
        target02.append(0.0 + uniform(-0.1, 0.1))

#擷取屬性['V35']    
dataRow35 = rocksVMines.iloc[:,35]

#繪製 屬性 'V35' 對 target 的散佈圖
plot.scatter(dataRow35, target02,alpha=0.5,s=120)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()