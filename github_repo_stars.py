'''
this will get the repositories lists with the language and stars
'''

import requests
from bs4 import BeautifulSoup
import re

url = 'https://github.com/{}'
username = 'amirbigg'

response = requests.get(url.format(username) , params={'tab':'repositories'})
content = BeautifulSoup(response.text , 'html.parser')

repository_elements = content.find(attrs={'id':"user-repositories-list"})
repositories = repository_elements.find_all('li') if repository_elements else []

for repo in repositories:
    title= repo.find('h3').find('a').get_text(strip=True)
    language=repo.find('span', attrs={'itemprop':"programmingLanguage"})
    language=language.get_text(strip=True) if language else 'unknown'
    stars=repo.find('a' , attrs={'href':re.compile('\/stargazers')})
    stars=int(stars.get_text(strip=True)) if stars else 0
    
    print(title,language,stars)