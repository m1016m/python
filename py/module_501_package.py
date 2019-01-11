#module_501_package.py 
#package, 套件
#statement-->function-->module-->package

#將模組(module)架構為套件(package)
#以下我們將建立一個目錄-->source01
#並在source01目錄下建立兩個模組檔-->module01.py , module02.py
#最後在source01目錄中必須有一個 __init__.py , 才能夠成一個 package 如下所示:
#
#                      source01 <dir>
#                          ----->module01.py <module file>
#                          ----->module02.py <module file>
#                          ----->__init__.py <file>, (空的也可以)
#----------------------------------------------------------------------
#
#example of package--> source01
from source01 import module01,module02 #從套件(目錄source01)中 
                                       #import 模組module01(檔案module01.py)和
                                       #module02(modulw02.py)
print("使用 source01.module01.fun01") #使用source01\module01\fun01()
module01.fun01()

print("使用 source01.module01.fun02") #使用source01\module01\fun02()
module01.fun02()

#叫用 source01\module02\fun03() 
print("使用 source01.module02.fun03") #使用source01\module01.fun02()
module02.fun03()

#如果 source01\module02 常用, -->指定別名 m2
from source01 import module02 as m2
#叫用 source01\module02\fun04()
m2.fun04()
