#p3_example7_tuple_20180724.py
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

#==============================================
#練習1:qTuple01,qTuple02 是tuple嗎?
#qTuple01=('Java','C#'),('Python','SQL'),'Perl'
#qTuple02='Java,C#,Python'

#==============================================
#練習2:tuple是不可變的(immutable),無法添加、刪除或更改它的項目
#如果 tuple qTuple01 如下
#qTuple01=('Java',['aaa','bbb','ccc'],'SQL')
#question 1: 可以嗎?為什麼?
#qTuple01[1]=['aaa','bbb','ccc','ddd'] 
#question 2: 可以嗎?為什麼?
#qTuple01[1].append('ddd')

#========================================================
#練習3:
#tup01=(5,6,7,(8.5,8.8))
#a,b,c,d=tup01
#d1 是什麼資料型別