import random
import csv

def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
    return heads
'''
該coin_trial功能代表了10個硬幣投擲的模擬。它使用該random()函數生成0到1之間的浮點數，
heads如果它在該範圍的一半之內，則遞增計數。然後，simulate根據您喜歡的次數重複這些試驗，
返回所有試驗的平均頭數
'''

def simulate(n):
   trials = []
   for i in range(n):
       trials.append(coin_trial())
   return(sum(trials)/n)
   
#print (simulate(10))

#print (simulate(100))

print(simulate(10000))

#print (simulate(1000000))

'''
隨著我們獲得越來越多的數據，現實世界開始變得像理想一樣。因此，給定足夠的數據，
統計數據使我們能夠使用真實世界的觀察來計算概率。概率提供了理論，而統計提供了使用
數據測試該理論的工具。描述性統計，特別是均值和標準差，成為理論的代理。

你可能會問，“如果我能計算理論概率本身，為什麼還需要代理呢？” 硬幣投擲是一個簡單
的玩具示例，但更有趣的概率並不那麼容易計算。隨著時間的推移，某人患病的機率是多少
？駕駛時關鍵汽車部件發生故障的概率是多少？
https://www.dataquest.io/blog/basic-statistics-in-python-probability/
'''
with open("wine-data.csv", "r", encoding="latin-1") as f:
    wines = list(csv.reader(f))

# Extract the Tokaji scores
tokaji = []
non_tokaji = []
for wine in wines:
    if points != '':
        points = wine[4]
    if wine[9] == "Tokaji":
        tokaji.append(float(points))
    else:
        non_tokaji.append(points)

# Extract the Lambrusco scores 
lambrusco = []
non_lambrusco = []
for wine in wines:
    if points != '':
        points = wine[4]
    if wine[9] == "Lambrusco":
        lambrusco.append(float(points))
    else:
        non_lambrusco.append(float(points))
