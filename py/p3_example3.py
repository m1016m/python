
# coding: utf-8
#p3_example3.py ,文字遊戲
#poem
poem='''There was a Youg Lady of Norway,
        who casually sat in a doorway;
        when the door squeezed her flat
        She exclaimed,"What of that?"
        This courageous Youg Lady of Norway.'''

#開頭是否為 'There'
poem.startswith('There') #開頭是否為 'There'
#結尾是否為 'norway.'
poem.endswith('norway') #False, 'Norway.'
#總共幾個字元(含空格與換行符號)
len(poem) #len() function
#取得前面15個字元
poem[0:15] #offset 0~14
#'who' 第一次出現的位移植
poem.find('who')
#練習a: 取出從第一個 'when' 到最後
#print(poem...)
#'of' 總共出現幾次
poem.count('of')




#練習a 參考解答: poem[poem.find('when'):]