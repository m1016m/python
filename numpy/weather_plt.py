import csv #匯入csv模組，該模組包含於python標準庫中
from matplotlib import pyplot as plt #從matplotlib中匯入pyplot並重命名為plt
from datetime import datetime #匯入日期模組，用以轉換字元型日期為日期型

#從檔案中獲取數值
filename='weather_2014.csv' #檔名
with open(filename) as f: #開啟檔案檔案
    reader=csv.reader(f) #讀取並將內容儲存在列表reader中
    header_row=next(reader)#next()函式獲取第一行，即檔案頭

    #提取氣溫、日期資料儲存在列表中
    highs,lows,dates=[],[],[]  #將最高氣溫、最低氣溫、日期儲存在列表中
    for row in reader: #遍歷reader列表

        high=int(row[1]) #將字元型溫度轉換成數值型
        highs.append(high) #將最高氣溫附加到highs列表中

        low=int(row[3])#同上
        lows.append(low)

        current_date=datetime.strptime(row[0],'%Y-%m-%d')#將字元型日期轉換成日期型
        dates.append(current_date)

    #繪製氣溫圖表
    fig=plt.figure(dpi=128,figsize=(8,6))#新增繪圖視窗，可繪製多條曲線
    plt.plot(dates,highs,c='red',alpha=0.6)#plot()函式，第一個引數x值，第二個y值，第三個圖形顏色
    plt.plot(dates,lows,c='blue',alpha=0.6)

    #設定圖形的格式
    plt.title("Daily high and low tempratures-2014\nDeath Valley,CA",fontsize=24)#圖形標題
    plt.xlabel("Date",fontsize=14)#x軸標題及字號
    fig.autofmt_xdate()#呼叫fig.autofmt_xdate()繪製斜的日期標籤，以防日期彼此重疊
    plt.ylabel("Temperature(F)",fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=8)#座標軸格式

    #給圖表區域著色
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    """
    facecolor為填充區域顏色
    alpha為填充顏色的透明度，0表示完全透明，1表示完全不透明
    """

    #顯示圖表
    plt.show()