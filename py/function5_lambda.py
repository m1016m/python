# -*- coding: utf-8 -*-
#匿名函數:lambda()
#我們先寫一個一般函數
#step1:定義一個edit_story() 函數
def edit_story(words,func): #words-->一串單字, func-->套用至words每一單字的函數
    for word in words:
        print(func(word))
        
#step2:宣告單字list --> stairs
stairs=['thud','meow','thud','hiss']

#step3:定義一個word加工函數 enliven(word)
def enliven(word):
    return word.capitalize()+'!' #字首大寫,字尾加'!'
    
#step4: 將step1,2,3 混合
edit_story(stairs,enliven)

#----------------------------------------------------------
print('----------------------------------------------------')
print('--將上述step1,2,3用lambda改寫--')
edit_story(stairs, lambda word: word.capitalize()+'!') #lambda 寫法,取代函數enlivne
                  #這個lambda會取用一個引數,在此是word。在:與)間的所有東西就是函數的定義                                     
#------------------------------------------------------------------------------
 
    