# coding: utf-8
#05_panda_100_fixed_20180726.py
from pandas import DataFrame #import DataFrame(), Series()
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web  #pandas Remote Data Access

        #http://pandas.pydata.org/pandas-docs/stable/remote_data.html
        #conda install pandas-datareader 
from datetime import datetime
start = datetime(2015, 1, 1)
end = datetime(2017, 12, 31)
        #web.DataReader('F', 'iex', start, end), The Investors Exchange (IEX)
#---------------------------------------------------------------------
#step 1: 資料取得 (Interacting with the outside world)
all_data={} #create a new dict object and named it all_data

for ticker in ['AAPL','IBM','MSFT','GOOG']: 
    all_data[ticker]=web.DataReader(ticker,'iex',start, end)
#以 for指令 對 list['AAPL','IBM','MSFT','GOOG'] 做迭代(iterating)
#迭代工作為叫用 pandas_datareader.data module 的 DataReader() API
#到 iex(yahoo/google) 依指定日期取得交易股價資料,並將此資料(DatFrame Object)
#構成字典(dict) all_data (dict of Dataframe)
#IEX: The Investors Exchange

all_data #dict of DataFrame, key:value (value 資料型別為 DataFrame)

all_data['AAPL'] #dict all_data, ['AAPL'] key 的值-->是一個 DataFrame
#檢視 DataFrame all_data['AAPL']
all_data['AAPL'].keys() #Index(['open', 'high', 'low', 'close', 'volume'], dtype='object')
all_data['AAPL'].head(5) #前5列
#------------------------------------------------------------------------
#step 2: 資料準備, 清理、轉換、合併、重塑

price=DataFrame({tic:data['close'] for tic,data in all_data.items()})
#先以字典生成式(dict comprehension) 將'close'欄位切出,成為dict of Series
#再以DataFrame() 轉成 DataFrame Object price
#你可以先裁 all_data['AAPL']['close'] 看看

volume=DataFrame({tic:data['volume'] for tic,data in all_data.items()})
#先以字典生成式(dict comprehension) 將'volume'欄位切出,成為dict of Series
#再以DataFrame() 轉成 DataFrame Object volume
#你可以先裁 all_data['AAPL']['volume'] 看看

#檢視 重塑的DataFrame price, volume
price.head(5)
volume.head(5)

#解說 1: d1 --> dict object
d1={tic:data['close'] for tic,data in all_data.items()}

#解說 2: keys() method of dict object
d1.keys()

#解說 3: 以key ['GOOG'] 取得字典中元素的值, 該值為Series object
# 該Series 的index 為日期, vlaue為  close (收盤價)
d1['GOOG']

#解說 4: 上述 Series object d1['GOOG], 以index ['2015-12-31'] 取值
d1['GOOG']['2015-12-31']
#----------------------------------------------------------------------
#step 3a: 計算、套用模型
#資料分析:計算 google 價格的百分比變化, DataFrame.pct_change() method
#pandas.DataFrame.pct_change() : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pct_change.html
#DataFrame.pct_change(periods=1, fill_method='pad', limit=None, freq=None, **kwargs)
#Percent change over given number of periods.
g_pct_price=price.pct_change() #叫用 DataFrame.pct_change() method

g_pct_price #仍是一個 DataFrame Object

#以DataFrame.tail(10) method, 檢視前10筆

g_pct_price.head(10)

#step 3b: correlation and covariance (相關係數及協方差), corr() / cov() method
#pandas.Series.corr() method : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.corr.html 
#Series.corr(other, method='pearson', min_periods=None)
#Compute correlation with other Series, excluding missing values

g_pct_price.GOOG.corr(g_pct_price.MSFT) #google 與 microsoft
#g_pct_price.GOOG是一Series Object, 叫用Series.corr() method 引數則為
#另一個Series Objecdt g_pct_price.MSFT (MicroSoft)
#計算兩者間的相關性 (correlation)

#pandas.Series.cov() method : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.cov.html
#Series.cov(other, min_periods=None)
#Compute covariance with Series, excluding missing values
g_pct_price.GOOG.cov(g_pct_price.MSFT)
#計算兩者間的協方差(協變) (convariance)
#----------------------------------------------------------------------
#step 4: 展示、視覺化
import matplotlib.pyplot as plt
#%pylab

price['GOOG']['2017-01-01':'2017-12-31'] 
#從DataFrame Price 以 key ['GOOG'] 切成 Series Object
#再從此Series Object 上 以[start:stop:step] slicing 
#'2015-01-01'~'2015-12-31' 的股價

plt.plot(price['GOOG']['2017-01-01':'2017-12-31'] )
#叫用plt.plot() 函數, 以 price['GOOG']['2017-01-01':'2017-12-31'] 
#為引數 繪圖

#Missing Data Processing
df2=g_pct_price.loc['2015-01-01':'2017-12-31',
                     ['GOOG','MSFT']]

#檢視 df2, 有nan 需處理
df2

#以DataFrame.fillna() method 處理 nan
df2=df2.fillna(value=0)

#再次檢視 df2
df2

#以DataFrame.plot() 繪圖
df2.plot()





