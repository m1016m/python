# coding: utf-8
#p3_example6, 從程式串列中找出以 'c'開頭的程式語言
import re #import re, regular expression module
#list TIOBE_list
TIOBE_list=['Java','C','C++','C#','Python','Objective-C'] 

c_head_list=[]
for ln in TIOBE_list:
    if re.search('^[c|C]',ln):
        c_head_list.append(ln)

c_head_list 
#另一種解法, 串列生成式
[ln for ln in TIOBE_list if re.search('^[c|C]',ln)]



