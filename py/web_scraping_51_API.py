# -*- coding: utf-8 -*-
"""
web_scraping_51_API.py
"""
import json
from urllib.request import urlopen

#定義函數 getCountry()
def getCountry(ipAddress):
    response=urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson=json.loads(response) #將傳回資料以 json.load() 轉成
    return responseJson.get("country_code")

print(getCountry("36.237.64.190"))

#python json 解析: web_scraping_52_JSON.py

    
