#stand liberary, OrderedDict()--> 使用鍵與OrderedDict()對字典排序
#example:
#step1:一般字典 quotes
quotes={'Moe':'A wise guy','Larry':'Ow!','Curly':'Nyuk nyuk!'} #dictionary quotes
for stooge in quotes:
    print(stooge)
    
#      Curly
#      Moe
#      Larry     -->並未排序
#--------------------------------------------------------------------------------
#OrderedDict()
from collections import OrderedDict
quotes2=OrderedDict([('Moe','A wise guy'),('Larry','Ow!'),('Curly','Nynk nynk')])
for stooge in quotes2:
    print(stooge) 
    