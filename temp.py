# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
score = []
total = inscore =0
while(True) :
    inscore = input("Input Exam:")
    if(inscore==-1):
        break
    score.append(inscore)
print ("共有 %d 位學生 " % (len(score) ))
for i in range(0 , len(score)):
    total += score[i]
average = total / (len(score))
print ("本班總成績 %d 分,平均成績 %5.2f 分" % (total , average))