'''
    mikhaym berim tamame jadval haye safeye gameofthrones ro tooye wikipedia begirim biarim
    be sorate list zakhirashoon konim
    etelaate kole jadval ha
'''

import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')

#dictionary hayi k gharrae tolid bokonim ro miarrim tooye in liste zakhire mikoniim
#tooye in inspect e jadval hai k darim hameye jadval ha ye kelasi daran be esme "wikitable plainrowheaders wikiepisodetable" harkodom az kalamehay tooy in kelas ro bezari ok e
#bayad be content emon aval ye tag bedim moshakhas konim tag table hast bad esme on kelasi k too hameye table ha moshtarake. az find_all ham estefade mikonim ke hameye table ha ba in tag ro biarae
episodes = []
ep_tables= content.find_all('table' , class_='wikiepisodetable')
#ep_tables=content.select('table.wikiepisodetable') inam mishe jaye balai benevisim

#ghadame badi gereftane header hastesh hameeye header hay hameye table ham bararbar hastand. az tarafi tooye source code har table tr yani table-row ke maanie radif ro mide va avalin row har table hamon header esh mishe.
#th ham mishe column haye on row e header

for table in ep_tables:
    headers=[]
    rows = table.find_all('tr')
    
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
        
    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
            
        if values:
            episode_dict={headers[i]:values[i] for i in range(len(values))}    
            episodes.append(episode_dict)
            
for ep in episodes:
    print (ep)            