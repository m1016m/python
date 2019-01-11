# coding: utf-8
#regular_expressions_20160723
import re #import re (reqular expressions) module

#re module 中定義的函數:
#match() /search() / findall() /compile() function, 取出匹配項目
source='My country is Taiwan, I love Taiwan'

if re.search('Taiwan',source): #字串'Taiwan'在 source 中
    print('找到了!')

r=len(re.findall('Taiwan',source)) #'Taiwan' 在 source 中出現兩次
                                   #re.findAll() 回傳的是 list object

r #print r

#example 1: regular expression "aa*bbb(cc)*(d | )"
            #第一個字是 a
            #第二個字 a* --> 零個到多個 a
            #bbb
            #(cc)* --> 零個到多個 'cc'
            #結尾是(d | ) --> 'd ' or ' '

if re.search('aa*bbb(cc)*(d | )','aaabbbccccd '):
    print("符合!")

if re.search('aa*bbb(cc)*(d | )','abbbcc '):
    print("符合!")

if re.search('aa*bbb(cc)*(d | )','aaaaaabbbcccd '):
    print("符合!")
else:
    print("不符合!")

#練習1: b? --> 零個或一個 'b';  a* -->零個或多個 'a'; (d|e) --> 'd' or 'e'  

#解答:
if re.search('a*b?(ccc)*(d|e)','aaabcccccce'):
    print("符合!")

#練習2: 'Taiwanese', [Tt]--> 'T' or 't'; .--> '\n'之外任何單一字元

#解答:
if re.search('[Tt]a..a?....','Taiwanese'):
    print("符合!")


#練習3: 'Taiwan No1!', '\d'-->一個數字字元; '\w'-->一個英數字元; '\s'-->一個空白字元
#                      '\W'-->一個非英數字元

#解答: 

source='Taiwan No1!'
m=re.search(r'\s.\w\d\W',source)  # r --> 不理會跳脫字元
if m:
    print(m.group())

#練習4: 'Taiwan No1!', '\b'--> 一個單字範圍

#解答: 

m=re.search(r'\b\s...!',source)
if m:
    print(m.group())

