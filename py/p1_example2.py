
# coding: utf-8

# In[1]:

#p1_example2 資策會 "http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm"


# In[2]:

from urllib.request import urlopen 


# In[3]:

from bs4 import BeautifulSoup


# In[4]:

import re


# In[5]:

html=urlopen("http://www.iiiedu.org.tw/ites/ites/ind_roomRent.htm")


# In[6]:

bsObj=BeautifulSoup(html,"lxml") #轉成 BeautifulSoup Object


# In[7]:

list_a=bsObj.findAll("a") #找出所有的 tag <a>


# In[8]:

#regular string " [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net) "


# In[9]:

for la in list_a:
    if re.search("[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)",la.get_text()):
        print(la.get_text())


# In[ ]:



