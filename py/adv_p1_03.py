# coding: utf-8
#adv_p1_03.py list
empty_list=[] #空串列 

#list of str, 元素是string
#注意,最後的逗號可有可無
weekdays=['Monday','Tuesday','Wednesday','Friday',]

weekdays #display list 'weekdays'

another_empty_list=list() #以list()函數製作一個空串列 

another_empty_list #display list 'weekdays'

#用list()將其他的資料類型轉換成串列

list_c=list('apple') #用list() 將字串轉成 "字元串列" 

list_c #list list_c, list of character

tuple_s=('ready','fire','aim') #create a tuple tuple_s,內含3個不可變的字串型別元素

tuple_s #tuple tuple_s ,tuple 符號為(),元素不可變 

list_t=list(tuple_s) #用list() 將tuple tuple_s 轉成串列

list_t #list list_t ,list 符號為[],元素可變 

#用split() method 將字串(str) 依指定字符 拆成 串列(list) 

birthday='1990/1/10' 

bd_list=birthday.split('/') #用字串的split() method 以 '/'為分隔,轉成一個list bd_list

bd_list #list bd_list

#split() 另一個範例 ','分隔

student_01='s001,jack huang,cs,0931777005' #string student_01

sstu_01_list=student_01.split(',') #split() method 以',' 分割

sstu_01_list #list sstu_01_list

#使用[offset(位移值)]取得串列項目

city=['Kaohsiung','Tainai','Taipei','Kaohsiung'] #list of string, 其中有重複值

city[0] #offset=0, 第一個元素

city[1] #offset=1, 第二個元素
city[-1] #offset=-1, 最後一個元素

city[4] #offset=4, 位移值無效例外, NG

city[-5] #offset=-4, 位移值無效例外, NG 
#串列的串列,list of list
list_1=[34,67,66,'ok','cont.'] #list list_1

list_2=[55,77,'ok','cont.'] #list list_2

list_3=['aaa','bbb'] #list list_3

list_all=[list_1,list_2,'sss',list_3] 

#list list_all, include 4 elements,(3 lists) 
list_all # list list_all

list_all[0] #offset 0, 第一個元素,list_1

list_all[-2] #offset -2, 倒數第二個元素, string 'sss'

list_all[1][1] #第二個元素(list_2)的第二個元素 77

list_all[-1][-2]  #猜猜看



