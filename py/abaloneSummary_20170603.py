import pandas as pd
from pandas import DataFrame,Series
from pylab import *
import matplotlib.pyplot as plt

#target_url = ("http://archive.ics.uci.edu/ml/machine-"
#              "learning-databases/abalone/abalone.data")
#read abalone data from file "abalone.data.txt", 形成 DataFrame abalone
abalone=pd.read_csv("abalone.data.txt",header=None)

#更改 DataFrame abalone 的欄位名稱
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight',
                   'Shucked weight', 'Viscera weight', 'Shell weight',
                   'Rings']


print(abalone.head())
print(abalone.tail())

#print summary of data frame
summary = abalone.describe()
print(summary)

#以箱型圖檢視 'Sex' 以外的實數屬性資料
array = abalone.iloc[:,1:9] #DataFrame array

                    
                    
                    plt.boxplot(array)
plt.xlabel("Attribute Index")
plt.ylabel(("Quartile Ranges"))
plt.show()
#the last column (rings) is out of scale with the rest
# - remove and replot
array2 = abalone.iloc[:,1:8].values
boxplot(array2)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
show()

#removing is okay but renormalizing the variables generalizes better.
#renormalize columns to zero mean and unit standard deviation
#this is a common normalization and desirable for other operations
# (like k-means clustering or k-nearest neighbors
abaloneNormalized = abalone.iloc[:,1:9]


for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    abaloneNormalized.iloc[:,i:(i + 1)] = (
                    abaloneNormalized.iloc[:,i:(i + 1)] - mean) / sd

array3 = abaloneNormalized.values
boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized "))
show()