import requests
from urllib.request import urlopen
import bs4

url = 'http://www.w3school.com.cn/tags/tag_hn.asp'                     # 網址
htmlFile= requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text)

objTag = objSoup.find_all('h1')

print("資料型態    = ", type(objTag))     # 列印資料型態
print("列印Tag串列 = ", objTag)           # 列印串列
print("\n使用Text屬性列印串列元素 : ")
for data in objTag:                       # 列印串列元素內容
    print(data.text)
print("\n使用getText()方法列印串列元素 : ")
for i in range(len(objTag)):
    print(objTag[i].getText())