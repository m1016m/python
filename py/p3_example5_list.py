# coding: utf-8
#p3_example5_list
#list 操作, 以TIOBE程式排行為範例
TIOBE_list=['Java','C','C++','C#','Python','Objective-C'] #list TIOBE_list

#用[位移值]來更改一個項目
TIOBE_list[-1]='Swift' #將最後一項 'Objective-C' 改為 'Swift' 
TIOBE_list #print list TIOBE_list

#用slice [start:end:step]來取出項目，串列的slice仍然是一個串列。
top3_list=TIOBE_list[0:3] #前三名,0,1,2
top3_list #print list top3_list
step2_list=TIOBE_list[::2] #間隔 2
step2_list #['Java', 'C', 'C++', 'C#', 'Python', 'Swift'] 

#將串列反轉的技巧 [::-1] 
inverse_list=TIOBE_list[::-1] #將串列反轉
inverse_list #['Java', 'C', 'C++', 'C#', 'Python', 'Swift'] 

#append() method,將項目附加到結尾
TIOBE_list.append('php') #append() method
TIOBE_list

#extend() method (or +=),結合串列
other_language=['javascript','T-SQL'] #other_language list
TIOBE_list.extend(other_language) #用extend() method 結合串列
TIOBE_list

other_language_2=['ruby','perl'] #other_language_2 list
TIOBE_list+=other_language_2 #用+=結合字串
TIOBE_list

#特別注意!如果使用 append() 是將list 當成一個元素,而不是合併(join) 
other_language_3=['pascal','basic'] #other_language_3 list
TIOBE_list.append(other_language_3) #增加一個串列元素, 不是合併
TIOBE_list

#insert() method 與位移值,加入一個項目
TIOBE_list.insert(1,'lisp') #在位移值1(第二個元素)前插入
TIOBE_list

TIOBE_list.insert(88,'Go') #很明顯位移值不合法,但python會加入到最後,不會發生例外
TIOBE_list

#del 指令與位移值,刪除一個項目, del 是一個 python 指令,不是method或function
del TIOBE_list[-1] #刪除 offset -1,最後一個元素-->'Go'
TIOBE_list

#練習: 將最後的一個元素 ['pascal', 'basic'] 
#      拆成兩個字串元素後，加到 TIOBE_list後面
#      再將list 元素 del

#練習解答:
#......

TIOBE_list

#remove() method 與值,刪除項目
TIOBE_list.remove('php') #remove()  

#pop() method 與位移值,取得項目並刪除它
TIOBE_list
catch_pop=TIOBE_list.pop() #將最後一個元素('basic') pop 出(給catch_pop)後刪除它
catch_pop
TIOBE_list

catch_pop2=TIOBE_list.pop(2) #將第三個元素(C)pop出
catch_pop2
TIOBE_list

#index() method 與值,尋找某個項目的位移值
position_of_Python=TIOBE_list.index('Python')+1 #index()
print('position of Python',position_of_Python)

#in 指令,測試值
'Go' in TIOBE_list #'Go' 有沒有在 TIOBE_list 中?
'perl' in TIOBE_list #'perl' 有沒有在 TIOBE_list 中?

#count() method, 算出某個值出現次數
TIOBE_list.append('Java')
TIOBE_list.count('Java') #計算 'Java' 出現次數
TIOBE_list.count('Cobol') #計算 'Coblo' 出現次數

#join() method, 轉換成字串,join()是字串方法
TIOBE_str=', '.join(TIOBE_list) 
TIOBE_str
TIOBE_str2=' / '.join(TIOBE_list) 
TIOBE_str2

#example: join()是split()的相反
language=['C#','Java','SQL']
separator='*'
joined=separator.join(language) 
joined
separated=joined.split('*') #or joined.split(separator)
separated

#sort() method, 排序項目
#sort() --> 會就地排序串列本身
#sorted() --> 會排序串列,之後回傳複本
sorted_T_list=sorted(TIOBE_list) #sorted() function,排序後傳出一份copy,不改變原list
sorted_T_list #回傳的新list,已排序
TIOBE_list #原list,順序不變
TIOBE_list.sort() #呼叫 sort() method, 改變本身的排序
TIOBE_list #list 已排序

#降冪排序,sort() 參數 reverse=True
R_S_list=TIOBE_list.sort(reverse=True) #reverse=True 改為降冪 
R_S_list #上一行程式,是錯誤示範. sort() method 只會將原串列就地排序,改變原串列,不會傳回排序結果
TIOBE_list
sorted_list_2=sorted(TIOBE_list)
sorted_list_2 #sorted() function 才會回傳一個新物件 (sorted list) 

#list依不同條件排序,sort(key=cond.)
list99=['aaa','bbbbb','dd','a']
list99.sort(key=len,reverse=True) #依長度,reverse
list99

#list依不同條件排序,以lambda寫sort條件
list98=['aaa','bbbbb','dd','a']
list98.sort(key=lambda x:-len(x)) 
list98

#len() 函數, 取得長度
print('TIOBE_list 目前有',len(TIOBE_list),'個元素' ) 
#本尊與分身(copy) 
a=[1,2,3] #list a
a
b=a #變數b,指向變數a所指的list [1,2,3], 變數b,a指向同一物件
b
b[1]=99 #更改list b 的第二個元素
b #print b
a #print a, a與b 所指的是同一串列 [1,99,3] 
#複製新串列的方法: 1.copy(), 2.list(), 3.slice[:] 
a=[1,2,3] #list a [1,2,3] 
b=a.copy() #將list a 新複製一份, 用 b 指向此新物件
b #list b, [1,2,3] 
b[1]=99 #將list b 的第二個元素改為 99
b # print list b
a # print list a, 跟 list b 無關
#另兩種複製方法, list(), slice[:] 
c=list(a) #將list a 複製一份成 list c
c 
d=a[:] ##將list a 複製一份成 list d

#練習1: 將 list str99=['watsons','mcdonalds','dominos','pizzahut']
#      依字串長度編成字典如下:
#      {0: 'mcdonalds', 1: 'pizzahut', 2: 'watsons', 3: 'dominos'}





#練習1 參考解答:
str99=['watsons','mcdonalds','dominos','pizzahut']
dict_str99={i:s for i,s in enumerate(sorted(str99,key=len,reverse=True))}
dict_str99
