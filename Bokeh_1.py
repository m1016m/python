'''
工具疊加
一些Bokeh工具還具有可配置的可視屬性。例如，各種區域選擇工具和框縮放工具都overlay 可以設置其線和填充屬性：


import numpy as np

from bokeh.models import BoxSelectTool, BoxZoomTool, LassoSelectTool
from bokeh.plotting import figure, output_file, show

output_file("styling_tool_overlays.html")

x = np.random.random(size=200)
y = np.random.random(size=200)

# Basic plot setup
plot = figure(plot_width=400, plot_height=400, title='Select and Zoom',
              tools="box_select,box_zoom,lasso_select,reset")

plot.circle(x, y, size=5)

select_overlay = plot.select_one(BoxSelectTool).overlay

select_overlay.fill_color = "firebrick"
select_overlay.line_color = None

zoom_overlay = plot.select_one(BoxZoomTool).overlay

zoom_overlay.line_color = "olive"
zoom_overlay.line_width = 8
zoom_overlay.line_dash = "solid"
zoom_overlay.fill_color = None

plot.select_one(LassoSelectTool).overlay.line_dash = [10, 10]

show(plot)

懸停檢查
為懸停在其上的字形設置高亮顯示策略完全類似於設置selection_glyph或nonselection_glyph，
或通過前綴的顏色或alpha參數"hover_"。下面的例子演示了後一種方法：
'''

from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.sampledata.glucose import data
import bokeh.sampledata
bokeh.sampledata.download()



output_file("styling_hover.html")

subset = data.ix['2010-10-06']

x, y = subset.index.to_series(), subset['glucose']

# Basic plot setup
plot = figure(plot_width=600, plot_height=300, x_axis_type="datetime", tools="",
              toolbar_location=None, title='Hover over points')

plot.line(x, y, line_dash="4 4", line_width=1, color='gray')

cr = plot.circle(x, y, size=20,
                fill_color="grey", hover_fill_color="firebrick",
                fill_alpha=0.05, hover_alpha=0.3,
                line_color=None, hover_line_color="white")

plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))

show(plot)