#module_3_alias.py 2016/2/5
#import 模組使用別名
#example:
import report as rep #alias rep, 將模組report(其實就是report.py程式) import,並給定別名 rep
description=rep.get_description()
print("今日天氣:",description)

#另一種寫法:
from report import get_description #從模組report (report.py)中 import function get_descroiption
description2=get_description()
print("今日天氣2:",description2)

#再另一種寫法:
from report import get_description as r3 #r3 是 report.get_description的別名
description3=r3()
print("今日天氣3:",description3)