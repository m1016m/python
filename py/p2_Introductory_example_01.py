# coding: utf-8
#p2_Introductory_example_01
path3='usagov_bitly_data_ANSI.txt' #
open(path3).readline() #讀取 path 中的第一行

import json #import json 模組
path3='usagov_bitly_data_ANSI.txt'

# use the json module and its loads function invoked on each line 


# In[6]:

# in the sample file 'usagov_bitly_data_ANSI.txt'


# In[5]:

records=[json.loads(line) for line in open(path3)] # list comprehension,串列生成式


# In[6]:

records[0] #The resulting object records is now a list of Python dicts


# In[7]:

#access individual values within records by passing a string for the key you wish to access


# In[8]:

records[0]['tz']


# In[9]:

print(records[0]['tz'])


# In[10]:

# extract a list of time zones again using a list comprehension


# In[11]:

time_zones=[rec['tz'] for rec in records] 


# In[12]:

# not all of the records have a time zone field!


# In[13]:

# we can add the check if 'tz' in rec at the end of the list comprehension


# In[14]:

time_zones=[rec['tz'] for rec in records if 'tz' in rec] 


# In[15]:

time_zones[:10] #Just looking at the first 10 time zones


# In[16]:

#用標準python liberary 寫一計數函數 get_counts()  


# In[17]:

def get_counts(seq):
    ocunts={}
    for x in seq:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts


# In[18]:

#用標準python liberary 寫一更精簡的計數函數 get_counts2()


# In[19]:

from collections import defaultdict #from collections import defaultdic


# In[24]:

def get_counts2(seq):
    counts=defaultdict(int)  # values will initialize to 0
    for x in seq:
        counts[x]+=1
    return counts


# In[25]:

counts_1=get_counts(time_zones)


# In[26]:

counts_1['America/New_York']


# In[23]:

len(time_zones)


# In[27]:

counts_2=get_counts2(time_zones)


# In[28]:

counts_2['America/Sao_Paulo']


# In[29]:

#If we wanted the top 10 time zones and their counts


# In[30]:

def top_counts(count_dict, n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:] 


# In[31]:

top_counts(counts_2)


# In[32]:

#使用python standard library collections.Counter class ,可以讓上述工作更容易


# In[33]:

from collections import Counter #import collections.Counter


# In[34]:

counts3=Counter(time_zones)


# In[35]:

counts3.most_common(10)


# In[ ]:



