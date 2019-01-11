#module_7_stdlib_OrderDict.py 2016.4.17
#stand liberary, collection.OrderedDict()--> 使用鍵與OrderedDict()對字典排序
#dict 中,鍵的順序是無法預測的,
#An OrderedDict is a dict that remembers the order that keys were first inserted. 

#example:
#step1:一般字典 week
week={'星期一':'Monday','星期二':'Tuesday','星期三':'Wednesday','星期四':'Thursday'}
for day in week:
    print(day)
    
#      星期四
#      星期三
#      星期一
#      星期二    -->並未排序
#--------------------------------------------------------------------------------
#OrderedDict()
from collections import OrderedDict
week=OrderedDict([('星期一','Monday'),
                  ('星期二','Tuesday'),
                  ('星期三','Wednesday'),
                  ('星期四','Thursday')])
for day in week:
    print(day)
    
#星期一
#星期二
#星期三
#星期四   --> 會記得輸入順序

type(week) #collections.OrderedDict

    