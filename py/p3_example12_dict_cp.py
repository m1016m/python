
# coding: utf-8

# In[1]:

#p3_example12_dict_cp, dict. comprehension (字典生成式) 


# In[2]:

#{鍵運算式:值運算式 for 名稱 in 可迭代項目 if 條件式} 


# In[3]:

#example 1: 字串字母計算


# In[4]:

word='letters' #str word


# In[5]:

letter_counts={le:word.count(le) for le in word} #dict comprehension


# In[6]:

letter_counts


# In[7]:

#上例中'letters'中,'e','t'各會被運算兩次。雖然不會影響結果(dict, key unique)但效率差


# In[8]:

#改進example1


# In[9]:

letter_counts={le:word.count(le) for le in set(word)} 
                                     #iterable str word --> set(word) 


# In[10]:

letter_counts


# In[11]:

#練習: 語言癌,'動作','概念'
#找出一個句子中用超過兩次的字詞


# In[12]:

話句一='我們按下新增按鍵來做一個新增的動作,這是一個新增概念'


# In[13]:

{l:話句一.count(l) for l in set(話句一)}


# In[14]:

{l:話句一.count(l) for l in set(話句一) if 話句一.count(l) >= 2}


# In[15]:

#set comprehension, 集合生成式
#{運算式 for 名稱 in 可迭代者 if 運算式} 


# In[16]:

#example 1: 


# In[17]:

{l*2 for l in 'abcde'} #set


# In[18]:

{l*3 for l in 'abcde' if l*3 >= 'ccc'} #'ccc' 以後的(含'ccc') 


# In[19]:

#練習2: 文句中超過三次的字元集合


# In[20]:

話句一


# In[21]:

三次={字 for 字 in set(話句一) if 話句一.count(字) >= 3}


# In[22]:

三次


# In[23]:

#產生器生成式, 產生器是一種將資料提供給迭代器的方式


# In[24]:

#tuple 沒有生成式


# In[25]:

num_thing=(num for num in range(1,6)) #這不是tuple生成式


# In[26]:

type(num_thing) #num_thing 是generator(產生器)


# In[27]:

for n in num_thing: #可以直接迭代 generator num_thing
    print(n) 


# In[28]:

for n in num_thing: #generator 只能使用執行一次
    print(n)


# In[29]:

num_list=list(num_thing) #generator 只能使用執行一次, 否則可以將num_thing轉成list


# In[30]:

num_list

