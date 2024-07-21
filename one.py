import requests
url='https://soft98.ir/'
response=requests.delete(url)
print(response.status_code)
dir(response)