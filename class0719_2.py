# 下面這一行 %matplotlib inline 的目的是讓matplotlib畫出的圖片能直接在 jupyter notebook 顯示，如果你在VS code加這行是沒有用的。 
# 相對的，你在 VS code 執行時，圖片會直接跳出來。
import matplotlib.pyplot as plt
import pandas as pd

x = [0,1,2,3,4,5]
y1 = [0,1,2,3,4,5]
y2 = [0,1,4,9,16,25]

plt.figure(figsize=(10, 2)) # 圖片尺寸 10*6
# 這一行能畫散點圖,  s是點的尺寸, marker 是點的形狀
plt.scatter(x,y1, s=30, c='red', marker='<')
# 這一行能畫折線圖， linestyle是點的
plt.plot(x, y2, color='blue', linewidth=2.0, linestyle=':')
# 下面這一行也是畫線用，座標從 [4,4] 到 [3,16] 
plt.plot([4, 4], [3, 16], 'b--', linewidth=5)  # b-- => color:blue & linestyle:'--'

plt.xlabel('x')
plt.ylabel('y')
plt.legend(["y = x", "y = x**2"], loc=2); # loc指的是legend要放的位置，loc=2是放在第二象限
plt.title('sample_title');
plt.show() # 要把圖片顯示出來記得加這一行

# 取得 Google 股價資料

url = 'http://markets.financialcontent.com/stocks/action/gethistoricaldata?Month=12&Symbol=GOOG&Range=300&Year=2017'
google_stock = pd.read_csv(url)
google_stock.head()
# 因為收到的資料是從 12/29/17 開始到 03/28/14，因此要轉個方向變成3/28/14到12/29/17。
new_google_stock = google_stock.iloc[::-1]
plt.figure(figsize=(10, 5))
print(new_google_stock.shape) # 確認這資料有幾欄，幾列

x = range(0,new_google_stock.shape[0]) # [0,1,2...,945] # 產生 x 座標用
y = new_google_stock['Open'] # 取得 Open 那一欄的所有資料，用來當 y 座標。
plt.plot(x, y, color='blue', linewidth=2.0, linestyle=':') # 畫折線圖，因為 linestyle 設定為 ':' 所以會是一堆點
# .annotate 是畫那條箭頭線用的， 
# connectionstyle: 曲線角度 參考：https://matplotlib.org/2.0.2/api/patches_api.html#matplotlib.patches.ConnectionStyle
# xytext 指的是要將文字放在座標軸的哪裡。xy指的是點要在哪裡 arrowstyle箭頭要怎樣形式 angle3 箭頭的頭射入樣子
plt.annotate(
    s='something happened', xy=(324, 627), xytext=(400, 900), fontsize=15,
    arrowprops={'arrowstyle':'->', 'connectionstyle': "angle3,angleA=0,angleB=90"}
)
plt.title('google stock from 3/28/14 ~ 12/29/17')
plt.show()