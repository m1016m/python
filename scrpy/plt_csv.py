import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一行
    dates, highTemps, lowTemps = [], [], [] # 設定空串列
    for row in csvReader:
        try:                    
            currentDate = datetime.strptime(row[0], "%Y/%m/%d")
            highTemp = int(row[1])          # 設定最高溫
            lowTemp = int(row[3])           # 設定最低溫
        except Exception:
            print('有缺值')
        else:
            highTemps.append(highTemp)      # 儲存最高溫
            lowTemps.append(lowTemp)        # 儲存最低溫
            dates.append(currentDate)       # 儲存日期
       
fig = plt.figure(dpi=80, figsize=(12, 8))   # 設定繪圖區大小
plt.plot(dates, highTemps)                  # 繪製最高溫
plt.plot(dates, lowTemps)                   # 繪製最低溫
fig.autofmt_xdate()                         # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
'''
%Y 四位數年份 ex:2017
%y 2位數年份 ex:17
%m month (1-12)
%B ex:January
%A week ex:Sunday
%d day (1-31)
%H hr (0-23)
%I hr(1-12)
%p AM or PM
%M min (0-59)
%S sec (0-59)
'''

