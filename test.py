from urllib.request import urlopen
import re
import ssl
import bs4
import certifi
import requests


print('\npost login')
# http://pythonscraping.com/pages/cookies/login.html
payload = {'username': 'm1016m', 'password': 'Meng0614'}
r = requests.post('https://github.com/', data=payload)
print(r.cookies.get_dict())
# http://pythonscraping.com/pages/cookies/profile.php
r = requests.get('https://github.com/', cookies=r.cookies)
print(r.text)

data={'firstname':'Shuhui','lastname':'Meng'}
r=requests.post('http://pythonscraping.com/pages/files/processing.php',data=data)
print(r.text)