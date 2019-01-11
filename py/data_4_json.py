#與XML模組不同,JSON有一個主要模組-->json
#建立一個python 資料結構 (字典) menu
menu={
"breakfast":{
        "hours":"7-11",
        "items":{
            "breakfast burritos":"$6.00",
            "pancakes":"$4.00"
        }
    },
"lunch":{
        "hours":"11-3",
        "items":{
            "hamburger":"$5.00"
        }
    },
"dinner":{
        "hours":"3-10",
        "items":{
            "spaghetti":"$8.00"
        }
    }
}

#python 資料結構 (字典) menu
print(menu)

#import json 模組
import json

#使用dumps() 將資料結構(menu) 編碼成JSON字串 (menu_json) 
menu_json=json.dumps(menu)
print(menu_json) #印出來看看
#--------------------------------------------------------
#寫到'json_file.json'檔
fout=open('json_file.json','wt')
fout.write(menu_json)
fout.close()

#---------------------------------------------------------
#讀取'json_file.json'檔
fin=open('json_file.json','rt')
#使用loads()將JSON字串(menu_json) 轉回Python資料結構 (menu2)
menu2=json.loads(fin.read()) #json.loads()
#python 資料結構 (字典):
for item in menu2.items():
    print(item)

