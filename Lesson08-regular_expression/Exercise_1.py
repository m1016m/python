import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

# get status code
print('Requests message URL:', response.request.url)
print('-'*50)
print('Requests message Method:', response.request.method)
print('-'*50)
print('Requests message body:', response.request.body)

with open('music_show.json', 'w') as outfile:
    json.dump(response.text, outfile)