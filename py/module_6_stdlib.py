#Python 標準程式庫
#模組文件(http://docs.python.org/3/library)
#教學課程(http://bit.ly/library-tour)
#以下討論一些標準的通用模組

#setdefault(),defaultdict() -->處理遺漏的鍵
#setdefault()
#example1: 正常情況
periodic_table={'Hydrogen':1,'Helium':2} #宣告週期表字典
print(periodic_table)

#example2: 如果鍵沒有在字典裡，就會使用新值
carbon=periodic_table.setdefault('Carbon',12)
print(carbon) # 12
print(periodic_table) #{'Helium': 2, 'Carbon': 12, 'Hydrogen': 1}

#example3: 如果我們試著指派不同的預設值給一個已存在的鍵，將不會改變原值
helium=periodic_table.setdefault('Helium',947) #指派不同的預設值給一個已存在的鍵
print(helium) # 2,將不會改變原值
print(periodic_table) #{'Helium': 2, 'Carbon': 12, 'Hydrogen': 1},將不會改變原值

#------------------------------------------------------------------------------

#defaultdict()
#在字典被建立時，為任何新鍵指定預設值
from collections import defaultdict #from module collections import function defaultdict
periodic_table=defaultdict(int) #defalutdic()的引數是個函式,這裡我們給int(),將會回傳整數 0

periodic_table['Hydrogen']=1 #有給定鍵值 1
periodic_table['Lead'] #沒有給定鍵值, 將採預設值 0
periodic_table['Gold'] #沒有給定鍵值, 將採預設值 0

print(periodic_table) # defaultdict(<class 'int'>, {'Lead': 0, 'Gold': 0, 'Hydrogen': 1})












