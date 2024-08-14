import requests
from bs4 import BeautifulSoup

url='https://github.com/{}'
username='ghazalmua'

'''
    az session ha estefade mikonim
    chon gharare be yek host chandta request ersal bokonim
'''

session = requests.Session()
r= session.get(url.format('login'))
content = BeautifulSoup(r.text ,'html.parser')

data={}
forms= content.find_all('form')
for form in forms:
    for input in form.select('input[type=hidden]'):
        data[input.get('name')] = input.get('value')
    
    '''
        login va password i ke in zir hastan name e form ha hastan ke az source code bardashtim
        field hayi k hidden hastan ro gereftim rikhtim dakhele dictionary va field hayi ke name
        dashtan ro ham ferestadim be hamon dictionary ke etelaat ro kamel befrestim.
    '''    
    data.update({'login':'*******' , 'password':'*******'})    

# tooye source code neevshte bod ke action=session yani etelaat e method e post mikhaym bere toooye session ha. pas inja ham ma etelaat ro mifrestim be session ha
r = session.post(url.format(session) , data=data)    

#bad az inke ba method e post vared shodim mikhyam berim too safeye amir big 
r=session.get(url.format(username))
# hala source code e khate bala ro mifrestim be beautifulsoup

content = BeautifulSoup(r.text , 'html.parser')

user_information = content.find(class_='vcard-details')
user_information = user_information.get_text(strip=True)
print(user_information)
