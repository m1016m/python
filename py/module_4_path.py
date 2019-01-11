#模組搜尋路徑
#Python會使用sys標準模組的path變數內的目錄名稱及zip保存檔案
import sys 
for place in sys.path:
    print(place)
    
#Python會使用第一個找到的對象，如果你自行定義一個random模組且置放於標準程式庫之前，
#你就無法存取標準程式庫的random模組