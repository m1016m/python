__author__ = 'mike_bowles'
import urllib2
import sys
#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    #split on comma
    row = line.strip().split(",") #strip()用於去除字符串的首尾字符,預設是空白字符
    xList.append(row)
#檢視list xList (list of list)
xList
#檢視 xList[0] (list)
t1=xList[0]

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])))

