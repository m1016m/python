#設定檔
#本範例使用標準的 configparser 解析器,來處理Windows的 *.ini檔案
#範例檔案: settings.cfg

#example:
import configparser #import standard liberary configparser
cfg1=configparser.ConfigParser() #
cfg1.read('settings.cfg') #使用cfg1.read() 
print(cfg1) #cfg1 是一個 configparser.ConfigParser 物件
print(cfg1['french'])
print(cfg1['french']['greeting']) 
print(cfg1['files']['bin'])