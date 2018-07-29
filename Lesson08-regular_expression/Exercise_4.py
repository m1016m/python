from bs4 import BeautifulSoup
import urllib2
import re



html_doc = "https://www.google.com/"
req = urllib2.Request(html_doc)  
webpage = urllib2.urlopen(req)  
html = webpage.read()




soup = BeautifulSoup(html, 'html.parser')   




for k in soup.find_all('a'):
    print(k)
    print(k['href'])#查a標籤屬性的href
    print(k.string)#查a標籤屬性的string