import requests
from bs4 import BeautifulSoup
import re

class Scraper:
    def __init__(self,url,quality=None):
        self.url= url
        self.quality=quality
        
    def get_all_links(self):
        result= requests.get(self.url)
        content = BeautifulSoup(result.text , 'html.parser')
        video_links = content.find_all('a' , href=re.compile('.mp4'))
        links = [link['href'] for link in video_links]
        return links
    
    
s=Scraper('https://www.namasha.com/v/y5kreMJe')   
print(s.get_all_links()) 