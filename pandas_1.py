'''

http://bokeh.pydata.org/en/latest/docs/user_guide/categorical.html

先安裝pip3 install bokeh 然後輸入以下程式碼測試
上例是一個最簡單的 Bokeh 圖表程式。在 Bokeh 中，我們直接利用其提供的各種函式來繪製圖表。繪製完成後， 
Bokeh 則會依據我們的程式產生一對對應的 HTML 與 JavaScript 碼，並利用 Bokeh 在網頁上的函式庫
「BokehJS」來產生圖表。因此以前面的程式碼為例，一個 Bokeh 程式的基本運作如下：

設定資料與輸出檔案
output_file(“out.html”)
利用 Bokeh 繪製圖表
p = figure()
p.line([1,2,3,4,5], [5,4,3,2,1])
開啟產生的 HTML 檔 ( HTML + JavaScript ，自動生成 )
show(p)
為了讓我們可以輕鬆又有彈性的製作各式圖表， Bokeh 將函式庫大略分成三組：

bokeh.model — 製作圖表的基本元素，例如軸線、形狀等等。用來打造各種元件。
bokeh.plotting — 為我們處理掉一些基本細節 ( 例如格點與軸線 ) ，但保留客製化的彈性。
bokeh.charts — 直接使用各種完整圖表，例如長條圖、盒鬚圖等等。

如果想快速掌握 bokeh 的運作，我們可以直接從 bokeh.plotting 來操作，不過 bokeh.charts 也提供了一些預先建置好的圖表供我們使用，下列為其中幾個範例：

bokeh.charts.Bar — 製作長條圖
bokeh.charts.BoxPlot — 製作盒鬚圖
bokeh.charts.HeatMap — 製作熱圖
bokeh.charts.Donut — 製作甜甜圈圖

from bokeh.plotting import figure, output_file, show
output_file("out.html")
p = figure()
p.line([1,2,3,4,5],[5,4,3,2,1])
show(p)


from bokeh.charts import Donut, output_file, show
output_file('donut.html')
donut = Donut([[2., 5., 3.], [4., 1., 4.], [6., 4., 3.]], ['cpu1', 'cpu2', 'cpu3'])
show(donut)

這個例子使用「p.circle」來繪製圓圈，其中前兩個參數分別為 x 與 y 軸的座標點，後面則另外指定圓的大小及顏色。結果如下：
from bokeh.plotting import figure, output_file, show
p = figure(width=800,height=300)
p.circle([1,2,3],[2,5,3],size=[10,20,30],color=["pink","olive","gold"])
show(p)


Bokeh包含多種佈局選項，用於排列圖表和小部件。他們的目標是快速創建交互式數據應用程序。佈局的核心是三個核心對象Row，
Column和WidgetBox。雖然你可以直接使用這些模型，我們建議使用排版功能row()， column()和widgetbox()。

'''
#Columns ¶
#要以垂直方式顯示繪圖或小部件，請使用以下column()功能：
#也可以改成row
'''
from bokeh.io import output_file, show
from bokeh.layouts import row #
from bokeh.plotting import figure

output_file("layout.html")

x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i - 5) for i in x]

# create a new plot
s1 = figure(plot_width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create another one
s2 = figure(plot_width=250, plot_height=250, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create and another
s3 = figure(plot_width=250, plot_height=250, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# put the results in a column and show
show(row(s1, s2, s3))#
'''
#Widgets
#使用該widgetbox()功能佈局一組小部件
'''
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider

output_file("layout_widgets.html")

# create some widgets
slider = Slider(start=0, end=10, value=1, step=.1, title="Slider")
button_group = RadioButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)
select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
button_1 = Button(label="Button 1")
button_2 = Button(label="Button 2")

# put the results in a row
show(widgetbox(button_1, slider, button_group, select, button_2, width=300))
'''
'''
Bars 
Basic 
Bokeh使用hbar()和 vbar()字形方法創建基本條形圖變得簡單 。在下面的示例中，我們有以下簡單的1級因子序列：

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
為了告知Bokeh x軸是分類的，我們將這些因子列表作為x_range參數傳遞給：fund ~bokeh.plotting.figure.figure::

p = figure(x_range=fruits, ... )
請注意，傳遞因子列表是創建a的便捷簡寫表示法FactorRange。等效的顯式表示法是：

p = figure(x_range=FactorRange(factors=fruits), ... )
當您想要自定義時FactorRange，例如通過更改範圍或類別填充，這更明確 。

接下來，我們可以vbar使用水果名稱因子列表作為x 坐標，條形高度作為top坐標，以及width我們想要設置的任何 或其他屬性：

p.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)
全部放在一起，我們看到輸出：

from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
'''
'''
懸停工具
對於堆積條形圖，Bokeh提供了一些特殊的懸停變量，這些變量對常見情況很有用。

堆疊條形圖時，Bokeh會自動將name堆棧中每個圖層的屬性設置為該圖層的堆棧列的值。通過$name特殊變量，懸停工具可以訪問此名稱值。

此外，hover變量@$name可用於從每個圖層的堆棧列中查找值。例如，如果用戶將鼠標懸停在具有名稱的堆棧字形上，則相當於 

。"US East"@$name@{US East}

下面的示例演示了這兩個懸停變量：

from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("stacked.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

p = figure(x_range=fruits, plot_height=250, title="Fruit Counts by Year",
           toolbar_location=None, tools="hover", tooltips="$name @fruits: @$name")

p.vbar_stack(years, x='fruits', width=0.9, color=colors, source=data,
             legend=[value(x) for x in years])

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
'''
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, factor_cmap

output_file("periodic.html")

periods = ["I", "II", "III", "IV", "V", "VI", "VII"]
groups = [str(x) for x in range(1, 19)]

df = elements.copy()
df["atomic mass"] = df["atomic mass"].astype(str)
df["group"] = df["group"].astype(str)
df["period"] = [periods[x-1] for x in df.period]
df = df[df.group != "-"]
df = df[df.symbol != "Lr"]
df = df[df.symbol != "Lu"]

cmap = {
    "alkali metal"         : "#a6cee3",
    "alkaline earth metal" : "#1f78b4",
    "metal"                : "#d93b43",
    "halogen"              : "#999d9a",
    "metalloid"            : "#e08d49",
    "noble gas"            : "#eaeaea",
    "nonmetal"             : "#f1d4Af",
    "transition metal"     : "#599d7A",
}

source = ColumnDataSource(df)

p = figure(plot_width=900, plot_height=500, title="Periodic Table (omitting LA and AC Series)",
           x_range=groups, y_range=list(reversed(periods)), toolbar_location=None, tools="hover")

p.rect("group", "period", 0.95, 0.95, source=source, fill_alpha=0.6, legend="metal",
       color=factor_cmap('metal', palette=list(cmap.values()), factors=list(cmap.keys())))

text_props = {"source": source, "text_align": "left", "text_baseline": "middle"}

x = dodge("group", -0.4, range=p.x_range)

r = p.text(x=x, y="period", text="symbol", **text_props)
r.glyph.text_font_style="bold"

r = p.text(x=x, y=dodge("period", 0.3, range=p.y_range), text="atomic number", **text_props)
r.glyph.text_font_size="8pt"

r = p.text(x=x, y=dodge("period", -0.35, range=p.y_range), text="name", **text_props)
r.glyph.text_font_size="5pt"

r = p.text(x=x, y=dodge("period", -0.2, range=p.y_range), text="atomic mass", **text_props)
r.glyph.text_font_size="5pt"

p.text(x=["3", "3"], y=["VI", "VII"], text=["LA", "AC"], text_align="center", text_baseline="middle")

p.hover.tooltips = [
    ("Name", "@name"),
    ("Atomic number", "@{atomic number}"),
    ("Atomic mass", "@{atomic mass}"),
    ("Type", "@metal"),
    ("CPK color", "$color[hex, swatch]:CPK"),
    ("Electronic configuration", "@{electronic configuration}"),
]

p.outline_line_color = None
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_standoff = 0
p.legend.orientation = "horizontal"
p.legend.location ="top_center"

show(p)







