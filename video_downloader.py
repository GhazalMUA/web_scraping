import requests
from bs4 import BeautifulSoup
import re




qualities={
    '144':0,
    '240':1,
    '360':2,
    '480':3,
    '720':4,
    '1080':5
}



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
    
    
    '''
        tooye website namasha keyfiatha az pain be bala ziad mishan va 
        age y keyfiati vojod nadashte bashe, az bala vojod nadare.
        baray inkar miaym dictionary quality misazim va avale codemon mizarimesh
        hala mikhaym keyfiat haye mojod ro be karbar neshon bedim va mikhyam addae
        keyfiat neshon dade beshe masalan adade 720 ya adade 1080 .
         
    '''
    
    def get_qualities(self):
        quali = qualities.keys()
        links = self.get_all_links()
        available_qualities=[]
        for i in links:
            available_qualities.append(list(qualities[i]))
    