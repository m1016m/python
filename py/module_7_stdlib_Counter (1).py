#module_7_stdlib_Counter 2016.4.17
#stand liberary, collections.Counter() function
#example1: 
from collections import Counter #from module collections import Counter() function
breakfast=['spam','spam','eggs','spam','eggs','apple'] #宣告一個 breakfast list
breakfast_counter=Counter(breakfast) #使用 collections.Counter()
print(breakfast_counter)             #Counter({'spam': 3, 'eggs': 2, 'apple': 1})
print('垃圾早點計數-->',breakfast_counter['spam']) #垃圾早點計數--> 3, 直接使用Counter

type(breakfast_counter) #是一個 collection.Counter() 物件 (成對形式)
breakfast_dict=dict(breakfast_counter) #用dict() 將 breakfast_counter 轉成字典
print('垃圾早點計數-->',breakfast_dict['spam']) #垃圾早點計數--> 3

type(breakfast_counter)     #breakfast_counter是函數物件, collections.Counter
#----------------------------------------------------------------------------------------

#計數器物件 (Counter object), most_common() method
#使用most_common()降冪排序
print(breakfast_counter.most_common())  #[('spam', 3), ('eggs', 2), ('apple', 1)]
#使用most_common(1)降冪排序,並只取top 1
print(breakfast_counter.most_common(1)) #[('spam', 3)]
#使用most_common(2)降冪排序,並只取top 2
print(breakfast_counter.most_common(2)) #[('spam', 3), ('eggs', 2)]

#---------------------------------------------------------------------------------
#練習: 字串分析 '我們做一個新增的動作，這個動作可以動作到資料'
from collections import Counter
Counter('我們做一個新增的動作，這個動作可以動作到資料').most_common(3) 

#---------------------------------------------------------------------------------

#counter 使用範例1:將兩個計數器相加
#
lunch=['spam','eggs','spam','bacon','eggs'] #定義一個lunch list
lunch_count=Counter(lunch) #定義一個 collection.counter 物件 lunch_count

#看一下 lunch_count 的內容
print(lunch_count) #Counter({'spam': 2, 'eggs': 2, 'bacon': 1})
#回顧一下 breakfask_counter的內容
print(breakfast_counter) #Counter({'spam': 3, 'eggs': 2, 'apple': 1})
#----------------------------------------------------------------------------
#計數器相加, +
full_meal=breakfast_counter+lunch_count
print(full_meal) #Counter({'spam': 5, 'eggs': 4, 'apple': 1, 'bacon': 1})
print(full_meal.most_common())
#全部餐飲排名-->[('spam', 5), ('eggs', 4), ('apple', 1), ('bacon', 1)]
print(full_meal.most_common(1)) #全部餐飲top one-->[('spam', 5)]

#-----------------------------------------------------------------------------
#計數器相減,-->早餐與中餐的差別,甚麼食物是早餐比中餐多?
diff_meal=breakfast_counter-lunch_count 
print(diff_meal) #Counter({'apple': 1, 'spam': 1}), 注意結果!,早餐比中餐多一餐 'spam'

#計數器相減,-->早餐與中餐的差別,甚麼食物是中餐比早餐多?
diff_meal_2=lunch_count-breakfast_counter
print(diff_meal_2) #Counter({'bacon': 1}),注意結果!,中餐比早餐少一餐 'spam',負數不會出現在結果

#-----------------------------------------------------------------------------------------
#交集 & :早餐與午餐共同--> 交集會選取數量較少的那個項目
intersection_meal=breakfast_counter&lunch_count
print(intersection_meal) #Counter({'spam': 2, 'eggs': 2})

#聯集 | : 與加法不同，聯集不會加總數量而是選取數量較多的那個項目
union_meal=breakfast_counter|lunch_count
print(union_meal) #Counter({'spam': 3, 'eggs': 2, 'apple': 1, 'bacon': 1})

#==============================================================================
#collections.Counter 參考 --> https://docs.python.org/3.4/search.html?q=collections.Counter&check_keywords=yes&area=default








