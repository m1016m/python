import pandas as pd

'''
抽樣（簡單隨機抽樣，種群，樣本，參數，統計）
變量
頻率分佈
pandas 和 matplotlib
我們將使用兩個電影評級樣本：一個樣本中的數據是在Hickey的分析之前收集的，而另一個樣本是在之後收集的。這將有助於我們比較分析前後的系統特徵。
幸運的是，我們在這兩段時間內都有現成的數據：
Walt Hickey 我們將使用他收集的數據來分析Fandango評級系統的特徵。Dataquest的一名團隊成員收集了2016年和2017年發布的電影的電影評級數據。
小數位數： display.precision
有效數字（有效數字位數）： display.float_format
關於四捨五入的說明
顯示的最大行數： display.max_rows
最大顯示列數： display.max_columns
默認行數/列數顯示： display.show_dimensions
總體最大顯示寬度： display.width
每列的最大顯示寬度： display.max_colwidth
對齊列名稱顯示的右/左： display.colheader_justify

'''
pd.options.display.max_columns = 100  # Avoid having displayed truncated output

previous = pd.read_csv('fandango_score_comparison.csv')
after = pd.read_csv('movie_ratings_16_17.csv')

print(previous.head(3))
print(after.head(3))
#我們僅隔離提供有關Fandango信息的列，以使相關數據更容易供以後使用。
fandango_previous = previous[['FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes',
                             'Fandango_Difference']].copy()
fandango_after = after[['movie', 'year', 'fandango']].copy()

print(fandango_previous.head(3))
print(fandango_previous.head(2))
'''
在Hickey的分析之後，我們的新目標是確定Fandango對2015年熱門電影的評分與Fandango對2016年熱門電影的評分之間是否有任何差異
有了這個新的研究目標，我們有兩個感興趣的人群：

1.所有Fandango對2015年發布的熱門電影的評分。
2.所有Fandango在2016年發布的熱門電影評級。
我們需要清楚什麼是流行電影。我們將使用Hickey的30粉絲評級基準，只有在Fandango網站上有30個粉絲評級或更高的粉絲時才算一部電影。
我們的第二個樣本中的一個採樣標準是電影受歡迎程度，檢查此示例的代表性的一種快速方法是從中隨機抽取10部電影，
然後在Fandango的網站上查看粉絲評級的數量。理想情況下，10部電影中至少有8部有30個或更多的粉絲評級。
'''
fandango_after.sample(10, random_state = 1)#使用值1作為隨機種子。這是一種很好的做法，因為它表明我們並沒有嘗試各種隨機種子來獲得有利的樣本。
print(sum(fandango_previous['Fandango_votes'] < 30))#0
'''
從Hickey的數據集開始，並僅隔離2015年發布的電影。發布年份沒有特殊列，但我們應該能夠從FILM列中的字符串中提取它。
'''
print(fandango_previous.head(2))
fandango_previous['Year'] = fandango_previous['FILM'].str[-5:-1]
print(fandango_previous.head(2))
print(fandango_previous['Year'].value_counts())
fandango_2015 = fandango_previous[fandango_previous['Year'] == '2015'].copy()
fandango_2015['Year'].value_counts()
fandango_after.head(2)
print(fandango_after['year'].value_counts())

fandango_2016 = fandango_after[fandango_after['year'] == 2016].copy()
fandango_2016['year'].value_counts()
'''
比較2015年和2016年的分佈形狀
我們的目的是弄清楚Fandango在2015年對熱門電影的評分與Fandango在2016年對熱門電影的評分之間是否存在任何差異。
一種方法是分析和比較兩個樣本的電影評級分佈。

我們將首先使用核密度圖比較兩個分佈的形狀。我們將使用FiveThirtyEight樣式繪製圖表。
'''
import matplotlib.pyplot as plt
from numpy import arange
plt.style.use('fivethirtyeight')
'''
DataFrame.plot.kde（bw_method = None，ind = None，** kwds ）[來源]
使用高斯核生成核密度估計圖。

在統計學中，核密度估計（KDE）是一種估計隨機變量的概率密度函數（PDF）的非參數方法。此函數使用高斯內核並包括自動帶寬確定。

參數：	
bw_method：str，scalar或callable，可選用於計算估計器帶寬的方法。這可以是'scott'，'silverman'，標量常量或可調用。
如果為None（默認值），則使用“scott”。

ind：NumPy數組或整數，可選估算PDF的評估點。如果為None（默認值），則使用1000個等間距點。
如果ind是NumPy數組，則在傳遞的點處評估KDE。如果ind是整數， 則使用ind數量等間隔的點。

** kwds：可選其他關鍵字參數記錄在中 pandas.DataFrame.plot()。
'''

fandango_2015['Fandango_Stars'].plot.kde(label = '2015', legend = True, figsize = (8,5.5))
fandango_2016['fandango'].plot.kde(label = '2016', legend = True)

plt.title("Comparing distribution shapes for Fandango's ratings\n(2015 vs 2016)",
          y = 1.07) # the `y` parameter pads the title upward
plt.xlabel('Stars')
plt.xlim(0,5) # because ratings start at 0 and end at 5
plt.xticks(arange(0,5.1,.5))
plt.show()
'''
上圖的兩個方面是驚人的：

兩種分佈都強烈傾斜。
相對於2015年的分佈，2016年的分佈略微向左移動。
左傾斜表明Fandango上的電影主要是高和非常高的粉絲評級。再加上Fandango賣票的事實，高收視率有點可疑。
進一步調查這一點非常有趣 - 理想情況是在一個單獨的項目中，因為這與我們分析的當前目標無關。

對於我們的分析，2016年分佈的輕微左移非常有趣。這表明2016年的收視率與2015年相比略有下降。
這表明Fandango在2015年的熱門電影收視率與Fandango對2016年流行電影的收視率之間存在差異。
我們還可以看到差異的方向：收視率與2015年相比，2016年略低。
'''
#由於數據集具有不同數量的電影，因此我們將表格標準化並顯示百分比。
print('2015' + '\n' + '-' * 16) # To help us distinguish between the two tables immediately and avoid silly mistakes as we read to and fro

fandango_2015['Fandango_Stars'].value_counts(normalize = True).sort_index() * 100
print('2016' + '\n' + '-' * 16)
fandango_2016['fandango'].value_counts(normalize = True).sort_index() * 100
'''
確定變化的方向
讓我們採用幾個匯總指標來更準確地了解變化的方向。在下文中，我們將計算兩個分佈的均值，中值和模式，然後使用條形圖繪製值。
'''
mean_2015 = fandango_2015['Fandango_Stars'].mean()
mean_2016 = fandango_2016['fandango'].mean()

median_2015 = fandango_2015['Fandango_Stars'].median()
median_2016 = fandango_2016['fandango'].median()

mode_2015 = fandango_2015['Fandango_Stars'].mode()[0] # the output of Series.mode() is a bit uncommon
mode_2016 = fandango_2016['fandango'].mode()[0]

summary = pd.DataFrame()
summary['2015'] = [mean_2015, median_2015, mode_2015]
summary['2016'] = [mean_2016, median_2016, mode_2016]
summary.index = ['mean', 'median', 'mode']
summary
plt.style.use('fivethirtyeight')
summary['2015'].plot.bar(color = '#0066FF', align = 'center', label = '2015', width = .25)
summary['2016'].plot.bar(color = '#CC0000', align = 'edge', label = '2016', width = .25,
                         rot = 0, figsize = (8,5))

plt.title('Comparing summary statistics: 2015 vs 2016', y = 1.07)
plt.ylim(0,5.5)
plt.yticks(arange(0,5.1,.5))
plt.ylabel('Stars')
plt.legend(framealpha = 0, loc = 'upper center')
plt.show()
#2016年的平均評分較低，約為0.2。這意味著相對於2015年的平均評級下降近5％。
prin((summary.loc['mean'][0] - summary.loc['mean'][1]) / summary.loc['mean'][0])

'''
結論
我們的分析顯示，Fandango對2015年熱門電影的評分與Fandango對2016年熱門電影的評分確實存在細微差別。
我們還確定，2016年發布的熱門電影在Fandango上的評分低於2015年發布的熱門電影。

我們不能完全確定導致這種變化的原因，但是在Hidkey的分析之後，由Fandango修復偏見的評級系統引起的可能性非常高。
'''




