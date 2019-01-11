#YAML (http://www.yaml.org)
#尚未納入幫準python liberary, third party liberary --> yaml (http://pyyaml.org/wiki/PyYAML)
#load(): 將YAML字串轉換成Python資料; dump(): 將Python資料轉成YAML字串
#最好以 safe_load() 取代 load()
#install yaml: c:>conda install yaml 
#yaml 範例檔案: mcintyre.yaml


#example:
import yaml #import yaml

#將mcintyre.yaml 交給file handler : fin
with open('mcintyre.yaml','rt') as fin: 
    text=fin.read()

yaml_data=yaml.safe_load(text) #將YAML字串轉換成Python資料 yaml_data

#print yaml_data 中 'details' 部分
print(yaml_data['details']) 

#print yaml_data 中 'poems' 部分
print(yaml_data['poems'])

#使用這個 字典/串列/字典 參考,取得第二首詩 [1]的title
print(yaml_data['poems'][1]['title'])

#使用這個 字典/串列/字典 參考,取得第一首詩 [0]的text
print(yaml_data['poems'][0]['text'])  