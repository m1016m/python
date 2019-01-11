#p3_example7_tuple_20160723
#tuple
#用()來建立Tuple
empty_tuple=() #製作一個空tuple
empty_tuple

#在元素後面加逗點 ','
language_tuple='Java', #在元素後面加逗點 ','
language_tuple #是一個tuple
type(language_tuple) #language_tupel 是一個tuple物件

#多個元素的tuple,用逗點隔開
l_tuple='Java','C#','Python','SQL' #用逗點隔開

#tuple 是 sequence 物件, 可以 for 做迭代
#str, list 也是 sequence 物件

for i in l_tuple: #逐一 "彈出"
    print(i)

#tuple 也是 Iterable 物件, 用串列生成式測試:
import collections.abc #import collections.abc module (sequences 抽象類別)

issubclass(tuple,collections.abc.Iterable)

[x for x in l_tuple] #串列生成式
[x for x in l_tuple if len(x)>=3] #串列生成式

l_tuple[2] #tuple 是 sequence 物件

l_tuple[2]='R' #將tupe l_tuple 第三個元素改為 'R'
               #NG! why?

l_tuple_2=('Java','C','Go',) #有沒有小括號無所謂;多個元素,最後逗點無所謂
print(l_tuple_2)

#tuple可以一次指派給多個變數, (tuple unpacking)
week=('星期一','星期二','星期三','星期四','星期五','星期六','星期日') 
mon,tue,wed,thu,fri,sat,sun=week #tuple unpacking
tue  
tue,fri

#tuple(), 將其他東西做成tuple
#list week
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
week_tuple=tuple(week) #用tupe()將list week 轉成 tuple 

for d in week_tuple: 
    print(d) 

week_tuple[0]='星期一' #錯!, tuple不可變

#練習1: var_x='xxx', var_y='yyy', --> 最快將var_x與var_y內容交換的方式
var_x='xxx'
var_y='yyy'

#練習2:讀取高雄市政府資料開放平台
#     http://data.kaohsiung.gov.tw/Opendata/index.aspx
#     捷運動態資料之站代號及站名稱對照表 (kmrt.txt) csv 格式
#     取抬頭成tuple 如下:
#('ODMRT_MrtId', 'ODMRT_Name', 'ODMRT_Code', 'ODMRT_CName', 'ODMRT_Remark')







#練習1: 參考解答
var_x,var_y=var_y,var_x

#練習2: 參考解答
import csv
with open('kmrt3.txt','r') as fin:
    list_of_kmrt=[x for x in csv.reader(fin)]
    tuple_of_kmrt=tuple(list_of_kmrt[0])

tuple_of_kmrt

