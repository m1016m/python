
# coding: utf-8

# In[1]:

#p3_example11_code_structure         A433_04_01_20160702


# In[1]:

# 用 \ 來延續多行


# In[2]:

1+2+3+4+5+ 6+7+8+9+10


# In[3]:

# if、elif and else


# In[4]:

honest=True
if honest:
    print('wow!')
else:
    print('Yee!')


# In[5]:

#猜大小,if...else


# In[6]:

base_price=87
guess=input('請輸入0~99的數字:')
if int(guess) >= 87:
    print('你贏了!')
else:
    print('你輸了!')


# In[8]:

#電視分級,if...if...else


# In[9]:

age=int(input('請輸入真實年齡:'))
if age < 18:
    if age >=12:
        print('少年耶,可以看保護級!')
    else:
        print('小朋友,請看東森幼幼台!')
else:
    print('恭喜你,可以看限制級!') 


# In[10]:

#電視分級,if...elif,   elif(else if)


# In[11]:

age2=int(input('請輸入真實年齡:'))
if age2 >= 18:
    print('恭喜你,可以看限制級!')
elif age2 >=12:
    print('少年耶,可以看保護級')
else:
    print('小朋友,請看東森幼幼台!')


# In[12]:

#水果顏色,if...elif...elif...,else; ==運算子


# In[13]:

color=input('請輸入一種水果顏色(紅、橘、黃、...')
if color=='紅':
    print('蘋果')
elif color=='橘':
    print('橘子')
elif color=='黃':
    print('梨子')
else:
    print('我也不知道是甚麼?')


# In[14]:

#電視分級, ?<x<?


# In[15]:

age3=int(input('請輸入真實年齡:'))
if 19 >= age3 >= 13:
    print('teen age!!')
else:
    print('other age')


# In[16]:

#What is True?


# In[17]:

empty_list_1=[] #empty list empty_list_1 


# In[18]:

if empty_list_1:
    print('不是空串列')
else:
    print('空串列')


# In[19]:

if not(set()):
    print('空集合')


# In[20]:

# While loop


# In[21]:

count=1 
while count <=5:
    print(count)
    count+=1


# In[22]:

#無窮迴圈與break,continue


# In[23]:

#example of while with break and continue


# In[24]:

input_count=0  #輸入計數器,開始為 0
while True:    #無窮迴圈
    name=input('請輸入姓名:["q",結束程式;"!",不算]')
    if name=="!":            #continue
        print('這一回合不算!')
        continue
    if name=="q":            #break 
        print('總計輸入',input_count,'次, 結束程式!')
        break
    input_count+=1  #計數器+1
    print(name.capitalize())
    print('第',input_count,'次')   
    


# In[25]:

#while with else, 如果while迴圈正常結束(沒有呼叫break),控制權可以傳給一個選用的else。


# In[26]:

#example of while with else, 尋找串列中的偶數;如果沒找到,列印 '沒有偶數'


# In[27]:

num_list=[1,3,7,9] #list num_list
position = 0       #位置
while position < len(num_list):  #while loop 條件
    number=num_list[position]    #逐一走訪 list num_list
    if number % 2 == 0:          #如果是偶數
        print('找到偶數',number)  #列印後
        break                    #離開 while loop
    position+=1                  #下一個 position
else:            #如果正常離開while
    print('串列中沒有偶數。')


# In[28]:

#for iterator


# In[29]:

#list language_list, while 寫法
language_list=['Java','C','C++','Python','C#'] 
while count < len(language_list):
    print(language_list[count])
    count+=1


# In[30]:

language_list_1=['Java','C','C++','Python','C#'] #list language_list_1, for 寫法
for item in language_list_1:                     #for 迭代 串列
    print(item) 


# In[31]:

#for 迭代 字串


# In[32]:

str1='Apple'      #回傳是字元
for c in str1:   
    print(c) 


# In[33]:

#for 迭代 字典, keys(), values(), items() --> tuple


# In[34]:

program_language={'C':'Dennis Ritchie,1972','Python':'Guido van Rossum,1991',
                  'Java':'James Gosling,1995'}      #dict. program_language


# In[35]:

for k in program_language.keys(): #迭代字典內的 key
    print(k) 


# In[36]:

for k1 in program_language:  #迭代字典內的 key
    print(k1) 


# In[37]:

for v in program_language.values(): #迭代字典內的 values
    print(v) 


# In[38]:

#迭代字典的items,回傳的是 (key,value) tuple
#你可以用兩個區域變數 (k2,contents) 在一次迭代中處理
for k2,contents in program_language.items():       
    print('程式語言:',k2,'; 作者,年代-->',contents)  


# In[39]:

#for with break, continue, else


# In[40]:

num_list_2=[1,3,7,9] 
for n in num_list_2:
    if n % 2 == 0:
        print('偶數:',n)
        break
else:         #沒有 break, 到底都沒找到偶數
    print('沒有偶數')


# In[41]:

#zip(),以並行方式來迭代多個序列


# In[42]:

#example of zip(), 注意!zip() 會在最短的序列結束時停止。


# In[43]:

days=['Monday','Tuesday','Wednesday'] #list days   ,len=3
fruits=['banana','orange','peach']    #list fruits ,len=3
drinks=['coffee','tea','beer']        #list drinks ,len=3
desserts=['cake','pie','ice cream','pudding'] #list desserts ,len=4
for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day,' \t 水果:',fruit,'\t飲料:',drink,'\t點心:',dessert)  #pudding 永不錄用


# In[44]:

#dict()  搭配 zip() 


# In[45]:

days_list=['Monday','Tuesday','Wednesday'] #list days_list
星期串列=['星期一','星期二','星期三'] #list 星期串列
list2=list(zip(days_list,星期串列)) #list list2
dict2=dict(zip(days_list,星期串列)) #dict. dict2


# In[46]:

list2 #list of tuple


# In[47]:

dict2 #dict


# In[48]:

#range(),用來產生數字序列


# In[49]:

for x in range(1,10,1):
    print(x) 


# In[50]:

for x in range(2,10,2): #start 2, stop 10, step 2
    print(x)


# In[51]:

for x in range(10,0,-1): #start 10, stop 0, step -1 (倒數) 
    print(x)


# In[52]:

list(range(0,10,2)) #以list() 將range object 
                    #轉成串列


# In[53]:

#練習:萬年考古題 九九乘法表


# In[54]:

for x in range(1,10):
    for y in range(1,10):
        print(x,'*',y,'=',x*y) 
    print('------------')


# In[55]:

#生成式,Comprehension


# In[56]:

#串列生成式,list Comprehension


# In[57]:

#0. 原先,建立整數串列


# In[58]:

num_list=[] #先建立一個空串列


# In[59]:

num_list.append(1) 
num_list.append(2)
num_list.append(3)
num_list.append(4)
num_list.append(5)


# In[60]:

num_list #print list num_list


# In[61]:

#1. 使用一個迭代器與range() function 


# In[62]:

num_list=[]


# In[63]:

for num in range(1,6):    #一個迭代器與range()
    num_list.append(num)


# In[64]:

num_list #print list num_list


# In[65]:

#2. 使用list() function 與 range() function


# In[66]:

num_list=list(range(1,6))


# In[67]:

num_list


# In[68]:

#3. 串列生成式, [運算式 for 項目 in 可迭代項目]
#              [運算式 for 項目 in 可迭代項目 if 運算式]


# In[69]:

num_list=[num for num in range(1,6)] 


# In[70]:

num_list


# In[71]:

#3.1. 串列生成式, [運算式 for 項目 in 可迭代項目]


# In[72]:

num_list_1=[num+1 for num in range(1,6)] #運算式 (num+1), 項目(num), 可迭代項目 (range(1,6))


# In[73]:

num_list_1


# In[74]:

#3.2. 串列生成式, [運算式 for 項目 in 可迭代項目]


# In[75]:

num_list_2=[num*2 for num in range(1,6)] #運算式 (num*2)


# In[76]:

num_list_2


# In[77]:

#3.3 串列生成式,[運算式 for 項目 in 可迭代項目 if 條件式]
#    串列生成式可以容納條件運算式


# In[78]:

odd_list=[num*2-1 for num in range(1,10) if num%2==1] #運算式(num*2-1), 項目(num), 可迭代項目(range(1,10))
                                                      #條件式 (num%2 == 1)


# In[79]:

odd_list


# In[80]:

#3.4 雙重迴圈 


# In[81]:

rows=range(1,4) #range(1,4)


# In[82]:

cols=range(1,3) #range(1,3)


# In[84]:

for row in rows:
    for col in cols:
        print(row,col)


# In[85]:

#以生成式改寫上例


# In[86]:

cells=[(row,col) for row in rows for col in cols]


# In[87]:

for cell in cells:
    print(cell)


# In[ ]:



