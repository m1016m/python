# LSTM for international airline passengers problem with regression framing
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


# 產生 (X, Y) 資料集, Y 是下一期的乘客數 國際航空公司的乘客：每月總數為千人
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)
    
# fix random seed for reproducibility
numpy.random.seed(7)


# 載入訓練資料
dataframe = read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
dataset = dataframe.values
dataset = dataset.astype('float32')
# 正規化(normalize) 資料，使資料值介於[0, 1]
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# 2/3 資料為訓練資料， 1/3 資料為測試資料
train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

# 產生 (X, Y) 資料集, Y 是下一期的乘客數(reshape into X=t and Y=t+1)
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# 建立及訓練 LSTM 模型
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

# 預測
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# 回復預測資料值為原始數據的規模
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

# calculate 均方根誤差(root mean squared error)
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# 畫訓練資料趨勢圖
# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# 畫測試資料趨勢圖
# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

# 畫原始資料趨勢圖
# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()


探討一個可應用在企業運作上的實例，銷售預測主要是希望藉由過去的銷售記錄預測下一個週期的銷售量，在統計上，我們會使用簡單迴歸，

乃至複雜的『時間序列分析』(Time Series Analysis)來預測銷售趨勢，因為，當期的銷售量通常會與前期的銷售量有緊密的關係，

除非公司發生重大事件，否則，應該會循著規律變化。還記得嗎? 在『自然語言處理』時，我們會使用LSTM考慮上下文的關係，這個模型

恰好與前面講的銷售量預測不謀而合，所以，本篇就以 LSTM 模型來預測銷售量。

銷售量預測的樣態很多種，包括營收、利潤、來客數、遊園人數、銷售產品數/金額、...等等，都屬於同一範疇，以航空公司的每月乘客人數為例

，使用 LSTM 模型預測下個月的乘客數。

時間序列(Time Series Analysis)概念淺介

簡單迴歸(Regression) 公式 y=ax+b，是基於 y(i) 與 y(j) 是相互獨立，沒有任何關聯，但在銷售量的表現上，這個假設並不合理，

公司銷售業績通常不會暴漲暴跌，而是『逐步』上升或下跌，也就是與前期的表現有緊密的關聯，另外，大部分的公司也會有淡、旺季，即

所謂的『季節效應』(Seasonal Effect)，因此，使用更複雜的『時間序列分析』(Time Series Analysis)預測會更貼近事實，時間

序列分析的模型因應問題的型態不同也有很多種，我們以ARIMA(Autoregressive Integrated Moving Average)為例
