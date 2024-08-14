'''
    estefade az cookie ha
    age be http://github.cim request e gert befresti ye source code beehet mide, 
    age ba etelaate ezafie cookie behesh darkhaste get bedi y chizi dg neshon mide.
    tooye har site i ke login kardi, khodesh vasat cookie set mikone az toooye tanzhimate 
    moroorgaret miri ghesmate cookie ha on website ro peyda mikoni vaa va y key value i dare 
    be esme `remember_user_token` ke ye value e pichide dare onaro besorate key value tooye ye 
    dictionary zakhire mikoni bad miari be onvane etelaate ezafi midi b darkhaste get et. 
'''

import requests
url='https://github.com'
response =requests.get(url)
print(response.text)