import opening
import ending
import zoo
import config
import calcA
from words import GREETING

GREETING

opening.say()
ending.say()

zoo.cat()
zoo.tiger()
zoo.duck()

for i in range(config.range1[0],config.range1[1]+1):
    for j in range(config.range2[0],config.range2[1]+1) :
        for y in calcA.calc(i,j):
            print str(i),str(y['sign']),str(j),'=',str(y['result']),"\t",
print "\n"

dict1 = {1:2,2:4}
dict1[1] = 3
print dict1[1]
    

