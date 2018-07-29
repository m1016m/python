import re

msg = 'John and Tom will attend my party tonight. John is my best friend.'
pattern = 'John|Tom'                # 搜尋John和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)
pattern = 'Mary|Tom'                # 搜尋Mary和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)