import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

s = json.loads(response.text)

with open('music_show.json', 'w') as outfile:
    json.dump(s, outfile)


with open('music_show.txt','w', encoding ='utf-8') as p:
    for i in range(5):
        a =   s[i]['title'] + ":" + s[i]['startDate'] + "~" + s[i]['endDate']
        p.write(a)
        print (a)