#web_scraping_06_regular_expressions_20160716
import re #import re (reqular expressions) module

#search() / findall() function, 取出匹配項目
source='My country is Taiwan, I love Taiwan'
if re.search('Taiwan',source): #字串'Taiwan'在 source 中,search()
    print('找到了!')

r=len(re.findall('Taiwan',source)) #'Taiwan' 在 source 中出現兩次
r                                  #findall() 回傳的是一list

#example 1: regular expression "aa*bbb(cc)*(d | )"
            #第一個字是 a
            #a* --> 零個到多個 a
            #bbb
            #(cc)* --> 零個到多個 'cc'
            #結尾是(d | ) --> 'd ' or ' '

if re.search('aa*bbb(cc)*(d | )','aaabbbccccd '):
    print("符合!")
else: 
    print("不符合!")

if re.search('aa*bbb(cc)*(d | )','abbbcc '):
    print("符合!")
else: 
    print("不符合!")
    
if re.search('aa*bbb(cc)*(d | )','aaaaaabbbcccd '):
    print("符合!")
else: 
    print("不符合!")
#----------------------------------------------------------------    
#練習1: b? --> 零個或一個 'b';  a* -->零個或多個 'a'; (d|e) --> 'd' or 'e'  
if re.search('a*b?(ccc)*(d|e)','aaabcccccce'):
    print("符合!")
else: 
    print("不符合!")

#----------------------------------------------------------------    
#練習2: 'Taiwanese', [Tt]--> 'T' or 't'; .--> '\n'之外任何單一字元
if re.search('[Tt]a..a?.s','Taiwanese'):
    print("符合!")
else: 
    print("不符合!") #不符合! -->請找出哪裡不符合?

#--------------------------------------------------------------------------------
#練習3: 'Taiwan No1!', '\d'-->一個數字字元; '\w'-->一個英數字元; '\s'-->一個空白字元
#                      '\W'-->一個非英數字元

source='Taiwan No1!'
m=re.search(r'\s.\w\d\W',source)  # r --> 不理會跳脫字元
if m:                             # m --> <_sre.SRE_Match object; span=(6, 11), match=' No1!'>
    print(m.group())              # group() method

#-----------------------------------------------------------------------------
#練習4: 'Taiwan No1!', '\b'--> 一個單字範圍
m=re.search(r'\b\s...!',source)
if m:
    print(m.group())
    
#-----------------------------------------------------------------------------
#re.compile() 說明:
#re.compile用來將regular expression轉換爲一個「pattern object」，我們可以稱之爲「模式物件」。
#將regular expression轉換爲模式對象的作用就是可以將其保存下來，已備後續之用。

#example of re.compile:
pattern01=re.compile('ab*') #將 regex 'ab*' 的樣式存成 pattern object --> pattern01

#使用pattern01:
if pattern01.match('abbb'):
    print('ok!')
else:
    print('ng!')
    
#再次使用pattern01:
if pattern01.match('bbbb'):
    print('ok!')
else:
    print('ng!')
    
#如果不利用re.compile() 將regex 存成 pattern object, 就必須每次寫一次, 如下例:
if re.match('ab*','abbbbbb'):
    print('ok!')
else:
    print('ng!')
    
if re.match('ab*','bbbbb'):
    print('ok!')
else:
    print('ng!')


