# -*- coding: utf-8 -*-
#1.設計basemap
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

map = Basemap(projection='merc',
              resolution='i' ,
              fix_aspect=True,
              llcrnrlon=119.0,
              llcrnrlat=21.8,
              urcrnrlon=122.05,
              urcrnrlat=25.4,
              lat_ts =20)
#參數說明
#1. resolution = i 表示簡單畫出海岸線 / c 表示粗線畫出海岸線
#2. projection = merc 麥卡拖投影(矩形平面) / ortho 正投影(圓滾滾的地球)
#3. llcrnrlat,llcrnrlon 經緯度的最低值(lower lat/lon)，這裡設定台灣的經緯度
#4. urcrnrlat,urcrnrlon　經緯度的最高值(upper lat/lon)，這裡設定台灣的經緯度
#5. lat_ts 最大緯度

#2. 設置地圖屬性
#海岸線的寬度
map.drawcoastlines(linewidth=1)

#儲存map , dpi=100表示存成800*600
plt.savefig('practice_map' , dpi=100)

plt.show()     

