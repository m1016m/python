# -*- coding: utf-8 -*-
#function example:
#定義函數
def commentary(color): #定義函數 commentary
    if color=='red':
        return "It's a tomato."
    elif color=='green': #else if
        return "It's green pepper."
    elif color=='purple':
        return "I don't know what it is"
    else:
        return "??????"
#---------------------------------------
#呼叫函數
comment=commentary('red') #第一次呼叫函數
print(comment)
comment2=commentary('yellow') #再次呼叫函數
print(comment2)