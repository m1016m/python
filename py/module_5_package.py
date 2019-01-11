#module_5_package.py 2016.4.15
#package, 套件
#statement-->function-->module-->package

#將模組(module)架構為套件(package)
#以下我們將建立一個目錄-->source
#並在source目錄下建立兩個模組檔-->daily.py , weekly.py
#最後在source目錄中必須有一個 __init__.py , 才能夠成一個 package 如下所示:
#
#                      source <dir>
#                          ----->dayly.py <module file>
#                          ----->weekly.py <module file>
#                          ----->__init__.py <file>, (空的也可以)
#----------------------------------------------------------------------
#
#example of package--> source
from source import daily,weekly #從套件(目錄source)中 import 模組daily(檔案daily.py)和weekly(weekly.py)
print("明日天氣預測:",daily.forecast()) #使用daily.forecast()
print('--------------------------------------------------------------------------------------------')
print("下周天氣預測:")
for number, outlook in enumerate(weekly.forecast(),1):
    print(number,outlook)

#----------------------------------------------------------------------------------------------------
#enumerate()函數說明
#enumerate(iterable, start=0)
#Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports #iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from #start which defaults to 0) and the values obtained from iterating over iterable.
 
