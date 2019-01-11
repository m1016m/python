#p3_example8_dict_20160723
#dictionary
empty_dict={} #用 {} 建立空的字典
empty_dict

#建立字典
program_language={'C':'Dennis Ritchie,1972','Python':'Guido van Rossum,1991',
                  'Java':'James Gosling,1995'} #以逗點隔開的 key:value 對

program_language #display dict. progrma_language
program_language['C'] #以[key] 當註標

#更改元素內容
program_language['Java'] = 'James Gosling,1995, top 1 now' 
program_language #key 'Java', 內容已更改

#dict() function,將雙值序列轉換成字典
#只要 "雙值序列" 樣式的都可以
#list of lists
lol=[[1.0,'aaa'],[2.0,'bbb'],[3.0,'ccc']] #list of lists
dict_lol=dict(lol)
dict_lol
dict_lol[2.0] #dict_lol is a dict., 以 [key] 當註標, 不是[offset]
            # 2.0 是 key

#list of tuples
lot=[('111','aaa'),('222','bbb'),('333','ccc')]
dict_lot=dict(lot)
dict_lot
dict_lot['222']='bbbb'

#tuple of lists
tol=(['11','aa'],['22','bb'],['33','cc'])
dict_tol=dict(tol) 
dict_tol

#含有雙字元字串的list, list of string
los=['3a','2b','1c'] 
dict_los=dict(los)
dict_los #注意!dict. 是以key排序

#含有雙字元字串的tuple, tuple of string
tos=('a1','b2','c3')
dict(tos)

#用[key]來添加或變更項目
pop_language={'C':'Dennis Ritchie,1972','Python':'Guido van Rossum,1991',
                  'Java':'James Gosling,1995'} #dictionary pop_language

pop_language['Java']='James Gosling,1995, No. 1 in 2016' #藉由[key],指定值 
pop_language
pop_language['Go']='Robert Griesemer,2009' #如果[key] 不存在,就新增此 key:value pair
pop_language

#dict. 中的 key 必須 unique,如果多次使用,最後一個值勝出
pop_language['Java']='一種程式語言' 
pop_language

#用update() method,合併字典
another_language={'C#':'microsoft','Java':'James Gosling,1995'} #another dict.
pop_language.update(another_language) #使用update() method 將一dict. 併入
pop_language #['Java'] 重複,後者勝出, [C#]新增

#用 del 指令與鍵來刪除項目
del pop_language['Go'] #Go 語言不再流行,刪除
pop_language

#使用 in 指令來測試鍵
'Python' in pop_language #['Python'] 是否在dict. pop_language 中
'Go' in pop_language #['Go'] 是否在dict. pop_language 中

#用clear() method 來刪除所有項目 
another_language.clear() #clear() method
another_language

#用[key]來取得一個項目
pop_language['Java'] #['Java'] 
pop_language['COBOL'] #如果 key 不存在,你會得到一個例外
                      #但是如果 pop_language['COBLO']='一個古老的語言' --> OK.

pop_language['COBOL']='一個古老的語言' #在指定時['COBOL'] key不存在,此時會變新增

#get() function
pop_language.get('PROLOG','not exists') #改用get() method, 如果key不存在,出現替代值
pop_language.get('Java') #可以get() 來取得一個項目
pop_language.get('PROLOG') #沒有替代值時,以none出現,不會出現例外

#keys(), values(), items() method

#用keys() method,取得所有鍵
pop_language_list=list(pop_language.keys()) #用keys()取得字典所有鍵,以list() function
                                            #轉成list 
pop_language_list #list pop_language_list

#用values() method,取得所有值
pop_language_value_list=list(pop_language.values()) #用values() 取得字典所有值,
                                                    #以list() 轉成list
pop_language_value_list

#用items() method,取得所有 key/value pair , 將以list of tuple ('key','value') 傳回
pair_list=list(pop_language.items()) 
pair_list #以list of tuple ('key','value') 傳回

#綜合範例:從dict pop_language 中,將三個字母以上的程式
#        (['key'] 長度大於三) 的 item 取出


pop_language #dict. pop_language
[(d[0],d[1]) for d in pop_language.items()] #使用串列生成式,將pop_language.items() 
                                            #轉為 list of tuple

lot=[(d[0],d[1]) for d in pop_language.items() if len(d[0])>=3] #在串列生成式中使用 if 
lot
dict03=dict(lot) #再以dict() 將list of tuple 轉成 dict
dict03

#更快的解法:字典生成式:
dict04={d[0]:d[1] for d in pop_language.items() if len(d[0]>=3)}    



#用copy() method來複製 
pop_language_2=pop_language.copy() #copy() 一份新的dict.
pop_language_2
pop_language_2['Java']='James Gosling,1995, Top 1 in 2016'
pop_language_2
pop_language

