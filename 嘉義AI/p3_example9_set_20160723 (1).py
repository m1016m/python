# coding: utf-8
#p3_example9_set_20160723
#set,集合

#以set() 來建立集合
empty_set=set() #以set() 來建立空集合
empty_set #空集合是 set(), 不是{} , {} 是空字典

#用set(),轉換其他類型成為集合,並丟棄任何重複的值。
set_1=set('letters') #字串-->集合, 注意,重複字母會被刪除
print (set_1)
len(set_1)

list_1=list('letters') #比較 list,重複字母不會被刪除
list_1
len(list_1)
print (list_1)

list_1.count('t') #count() method, 計算 't' 出現次數

#count() 綜合運用練習, 將重複兩次以上字母列出:
li=list('letters') #將str 'letters' 轉成 list of character
li.count('t')

set([c for c in li if li.count(c) >= 2]) #串列生成式, 

set_2=set(list_1) #串列-->集合,重複元素會被刪除
set_2

#tuple-->set
tuple_3=('Java','C#','Python') #tuple tuple_3
set_3=set(tuple_3) #tuple-->set
set_3

#dictionary --> set
language_dict={'Java':'1995','C':'1972','Python':'1991'} #dictinory language_dict
set_4=set(language_dict) #dict.-->set, 只取key
set_4

#用in來測試值
#dictionary drinks, 每一元素值皆為集合
drinks={'martini':{'vodka','vermouth'},
        'black russian':{'vodka','kahlua'},
        'white russian':{'cream','kahlua','vodka'},
        'manhattan':{'rye','vermouth','bitters'},
        'screwdrive':{'orange juice','vodka'}}       

#example1: 那些飲料含 vodka?
for name, contents in drinks.items(): #drinks.items() 回傳形式為 (key,value)
    if 'vodka' in contents:           #的tuple, 所以for迭代時可以有兩個變數 
        print(name)                   #name, contents

#分解 example1:(以串列生成式說明)
drinks.items() #每一個items都是一個tuple ('white russian', {'kahlua', 'vodka', 'cream'}) 
[(di[0],di[1]) for di in drinks.items()] #drinks.items(), 串列生成式 
[(di[0],di[1]) for di in drinks.items() if 'vodka' in di[1]] #串列生成式with if 

#example2: 那些vodka 飲料,不含cream,vermouth
for name, contents in drinks.items():
    if 'vodka' in contents and not ('cream' in contents or 'vermount' in contents):
        print(name) 

#練習: 用串列生成式寫 example2 (那些vodka 飲料,不含cream,vermouth)
[di[0] for di in drinks.items() if 'vodka' in di[1] and 
 'cream' not in di[1] and 'vermount' not in di[1]]

#集合運算

#交集運算: &, intersetion() method
set_a={'a','b','c','d'} #set set_a
set_b={'c','d','e','f'} #set set_b

intersection_a_b=set_a & set_b #intersection of set a and set b
intersection_a_b #set intersection_a_b

set_a.intersection(set_b) #交集,用 intersection() method

#example 3: 找出含有 orange juice 或 vermouth 的飲料
for name,contents in drinks.items():           #drinks 的每一個值(contents)都是set
    if contents & {'orange juice','vermouth'}: #如果contents 與 
        print(name)                            #集合{'orange juice','vermouth'}有交集

#example 3: 串列生成式改寫,找出含有 orange juice 或 vermouth 的飲料
[di[0] for di in drinks.items() if {'orange juice','vermouth'}&di[1]] 

#example 4: 找出含 vodka,但不要 cream,vermouth ; 以交集 & 改寫 example2
for name,contents in drinks.items():
    if 'vodka' in contents and not contents & {'cream','vermouth'}:
        print(name) 

#練習:將example 4 以串列生成式改寫:
[di[0] for di in drinks.items() if 'vodka' in di[1] and not {'cream','vermouth'}&di[1]]

#聯集運算: |, union() method
set_c={'a','b','c','d'} #set set_c
set_d={'c','d','e','f'} #set set_d

set_c | set_d #set_c union set_d

set_c.union(set_d) #使用 union() method

#差集: 屬於第一個集合,但不屬於第二個集合, - , difference() method
set_c - set_d #set_c 與 set_d 的差集

set_d - set_c #set_d 與 set_c 的差集

#互斥: 只屬於其中一個集合的項目,^, symmetric_difference() method 
set_c ^ set_d #set_c 與 set_d 的互斥

set_c.symmetric_difference(set_d) #set_c 與 set_d 的互斥



