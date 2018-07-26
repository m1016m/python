from requests_html import HTMLSession
session = HTMLSession()
response = session.get('http://quotes.toscrape.com/')
print(response) # status_code, example: 200, 404...
print(response.html.text)


element = response.html.find('div.text itemprop .text')
elements = response.html.find('.quote')[0].find('.tag')
for element in elements :
    print (element.attrs['href'])