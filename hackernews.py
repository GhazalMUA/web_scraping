'''
    hameye etelaat tooye hackernews be sorate row tooye jadval hastan. on avalin element ke
    title khabar hasetsh ba tag `athing` nevehste shode vali khode khabar ha k zire title hastan
    hich tag nadaran. bayad ba regular expression beheshon dastresi peyda konim.
'''
from bs4 import BeautifulSoup
import requests
import re

url='https://news.ycombinator.com/news'
r = requests.get(url)
articles=[]
content=BeautifulSoup(r.text, 'html.parser')

for item in content.find_all('tr' , class_='athing'):
    item_a = item.find('span' , class_ = 'titleline').find('a')
    print(f'Item: {item}')
    print(f'Item A: {item_a}')
    item_link = item_a.get('href') if item_a else None
    item_text = item_a.get_text(strip=True) if item_a else None         # strip=True yani age faseleeye ezafi aval ya akhare matn bod pakesh kon
    
    
    '''
    ye tag <tr> dige baad az `athing` hastesh ke emtiazha va commentharo dare. 
    emtiaz ha ba class `score` moshakhas hsodan valii commentha tooye tag <a> hastan
    ke hich class i nadaran dar vaghe ye href dare k oon ham dynamic hasteseh va 
    hichjore nemishe beehsh eshare kard vase scraping faghat y rah hast k onam regular
    expression hastesh.
    tooye CSS tag hai k kenare hamdige hastand beehshon migim sibling.
    
    '''
    next_row = item.find_next_sibling('tr')
    item_score = next_row.find('span' , class_='score')
    item_score = item_score.get_text(strip=True) if item_score else '0 point'
    '''
    \d yani ba digit(adad) shoro mishe. + yani ba chandta adad shoro mishe
    &nbsp tooye html maanie space ro mide. pip line yani ya \s yani har no white space i ghabole
    comment(s?) yani kalameye comment hatman bayaad bashe (s?) in ham yani momkene akharesh s dashte bashe comments ya nadashte bashe comment
    '''
    item_comment= next_row.find('a' , string=re.compile(r'\d+(&nbsp;|\s)comment(s?)'))
    item_comment= item_comment.get_text(strip=True).replace('\xa0' , ' ') if item_comment else '0 comments'
    
    articles.append(
        {
            'link' : item_link , 
            'title' : item_text ,
            'score' :item_score ,
            'comments' : item_comment
        }
    )
    
for article in articles:
    print('*'*120)
    print (article)