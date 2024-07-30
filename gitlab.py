'''
    estefade az cookie ha
'''

import requests
url='https://github.com'
response =requests.get(url)
print(response.text)