import requests

url = 'https://www.google.com'
response = requests.get(url)



print(type(response))
print '-'*40
print('url: ', response.url)
print '-'*40

print('status code: ', response.status_code)
print('-'*40)


print('Requests message URL:', response.request.url)
print('-'*50)
print('Requests message Method:', response.request.method)
print('-'*50)
print('Requests message body:', response.request.body)

print response.text

print requests.__version__



 
    
