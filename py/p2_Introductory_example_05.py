# coding: utf-8

#p2_Introductory_example_05, 
#US Baby Names 1880-2015

import pandas as pd #慣例
from pandas import DataFrame,Series #from pandas import DataFrame,Series
import numpy as np #import numpy as np

import matplotlib.pyplot as plt #for drawing

get_ipython().magic('matplotlib inline')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Data Analysis: step 0 --> 取得資料 http://www.ssa.gov/oact/babynames/limits.html names.zip

# 檢視 names\\yob2015.txt
# !type  "names\\yob2015.txt" #this is a nicely comma-separated form

#this file is a nicely comma-separated form,(csv) 
#it can be loaded into a DataFrame with pandas.read_csv
#Read CSV (comma-separated) file into DataFrame

#pd.read_csv() 
names2015=pd.read_csv('names/yob2015.txt',names=['name','sex','births']) 

names2015 #檢視 DataFrame names2015

#聚合處理範例:
#SQL--> select sum(births) from names2015 group by sex
names2015.groupby('sex').births.sum() #對應SQL: select sum(births)
                                      #         from names2015
                                      #         group by sex;
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Data Analysis: step1--> 資料準備 

#將names 目錄中 yob1880.txt~yob2015.txt 合併組裝成一個 DataFrame

#years,range object
years=range(1880,2016) #range object

#create a empty list, pieces
pieces=[] #empty list pieces

#crate a list, columns
columns=['name','sex','births'] #list columns

#組裝:
for year in years:
    path='names/yob%d.txt' % year
    frame=pd.read_csv(path,names=columns)
    
    frame['year']=year #將DataFrame frame 加上一個 ['year'] 欄位, 並填值為 year
    pieces.append(frame) #將DataFrame frame 加到 list pieces (list of DataFrame)

#此時,pieces 是一個 list of Dataframe
#Concatenate everything into a single DataFrame

#使用pd.concat() 將list pieces 中的每個元素(都是DataFrame) 合併成一個 DataFrame names
names=pd.concat(pieces,ignore_index=True) 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#組裝分解說明 1:

# %d 每次以 year 代入

ys=[2001,2002,2003,2004,2005]
for year in ys:
    p='dir/yob%d.txt' % year # %d 每次以 year 代入
    print(p)

#組裝分解說明 2:
#我們先讀一個yob2015.txt --> frame_2015 做說明
frame_2015=pd.read_csv('names/yob2015.txt',names=['name','sex','births'])

frame_2015 #DataFrame frame_2015, 原先(剛讀入時)只有3個欄位

#將DataFrame frame_2015加上一個欄位['year']
#並填值 2015
frame_2015['year']=2015 

frame_2015 #frame_2015 有4個欄位

#++++++++++++ 組裝分解說明結束 ++++++++++++++++++++
names #display DataFrame names

#Data Analysis: Step 2 --> 資料處理與分析(聚合處理)

#example1: 依性別加總出生數, 
#SQL--> select sum(births) from names group by sex

total_births_sex=names.groupby('sex').births.sum() 
#這樣寫也可以 names.groupby('sex')['births'].sum()

total_births_sex

#example2: 依年度加總出生數,
#SQL--> select sum(births) from names group by year

total_births_year=names.groupby('year').births.sum()

total_births_year.tail(10) #取最後10行來看

#example3: 依年度、性別加總出生數, 
#SQL--> select year,sex,sum(births) from names group by year,sex

total_births_year_sex=names.groupby(['year','sex']).births.sum()

total_births_year_sex.tail(10)

#example4: 叫用 pandas.pivot_table() method
#pandas.pivot_table() method
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html
#注意 API function 與 object method 參數不同

total_births=names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
                                       
total_births.tail(5)

#繪圖顯示 total_births

total_births.plot(title='Total births by sex and year')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Data Analysis: Step 2a --> 資料處理與分析。首先，增加一個比率(prop) column 

#insert a column prop with the fraction of babies given each name relative to
#the total number of births. 
#A prop value of 0.02 would indicate that 2 out of every 100 babies was given a particular name.

#定義一個 add_prop() function
def add_prop(g):
    #Integer division floors
    births=g.births.astype(float)
    
    g['prop']=births/births.sum() #新增prop欄位,填值為 births/births.sum()
    return g #回傳新增prop欄位並已填值的 DataFrame

names #先檢視原來的 DataFrame names

#groupby(['year','sex'])
names_2=names.groupby(['year','sex']).births.sum()

#將groupby(['year','sex'])的結果以apply(),將add_prop() 套用在本身
names_3=names.groupby(['year','sex']).apply(add_prop)

#Applying Operations Over pandas Dataframes 說明
#p2_Introductory_example_051.ipynb

names_3 #檢視 DataFrame names_3

#在作group operation 時,一般會先做有效性檢查
#這裡我們先驗證所有分組的prop總合是否為1。
#但由於是float,所以我們用np.allclose來檢查分組合計總值是否夠接近1

np.allclose(names_3.groupby(['year','sex']).prop.sum(),1)

#extract a subset of the data : the top 1000 names for each sex/year combination.
#再更進一步分析前,我們從names_3擷取一個子集:the top 1000 names for each sex/year combination.

def get_top1000(g):
   return g.sort_index(by='births',ascending=False)[:1000]

groupd=names_3.groupby(['year','sex']) #groupd, GroupBy Object

top1000=groupd.apply(get_top1000) #top1000, DataFrame Object

top1000

#++++++++ 以下,我們就使用 top1000 資料集 ++++++++++

#分析命名趨勢
#Analyzing Naming Trends

#Splitting the Top 1,000 names into the boy and girl portions

boys=top1000[top1000.sex=='M'] #布林陣列

girls=top1000[top1000.sex=='F']


#form a pivot table of the total number of births by year and name:
#pivot_table()

total_births=top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)

total_births #檢視 DataFrame total_births

#找幾個菜市場姓名來看看:
#從total_births DataFrame 擷取 ['John','Harry','Mary','Marilyn']

subset=total_births[['John','Harry','Mary','Marilyn']]

#以DataFrame的plot method 繪製上述姓名的時間序列圖

subset.plot(subplots=True,figsize=(12,10),grid=False,title='Number of births per year')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Measuring the increase in naming diversity
#評估命名多樣性的增長

#the proportion of births represented by the top 1000 most popular names

table=top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)

table

table.plot(title='Sum of top1000.prop by year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))

#命名多樣項確實出現增長

#另一個範例:計算2015年男生,占總出生人數前50%的不同名字數量

df=boys[boys.year==2015]

df

#使用NumPy的cumsum累加prop,再以searchsorted 找出0.5的位置

prop_cumsum=df.sort_index(by='prop',ascending=False).prop.cumsum()

prop_cumsum[:10] #display top 10

prop_cumsum.searchsorted(0.5)[0] 
#注意! prop.cumsum.searchsorted(0.5) 傳回的是一個ndarray[134]
#我們需要 prop_cumsum.searchsorted(0.5)[0] 取出一整數值 

#Since arrays are zero-indexed, adding 1 to this result gives you a result of 135.

#用1915年的資料分析,前50%命名總數

df=boys[boys.year==1915]

in1915=df.sort_index(by='prop',ascending=False).prop.cumsum()

in1915

in1915.searchsorted(0.5)[0]+1

#1915年前50%只有33個名字

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#將上例(2015,M,前50%命名數) / (1915,M,前50%命名數) 計算方法,寫成函數並對groupby['year','sex'] 套用

def get_quantile_count(g,q=0.5):
    g=g.sort_index(by='prop',ascending=False)
    return g.prop.cumsum().searchsorted(q)[0]+1

diversity=top1000.groupby(['year','sex']).apply(get_quantile_count)

type(diversity)

diversity

diversity=diversity.unstack('sex') #將Series diversity以unstack('sex') 轉成DataFrame

type(diversity)

#現在DataFrame diversity擁有兩個時間序列(每個性別一個，按年度索引)

#你可以查看:
diversity.head(10)

#也可以繪圖
diversity.plot(title='Number of popular names in top 50%')





