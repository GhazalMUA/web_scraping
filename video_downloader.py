import requests
from bs4 import BeautifulSoup
import re


qualities={
    '1080':0,
    '720':1,
    '480':2,
    '360':3,
    '240':4,
    '144':5
}


class VideoDownloadException(Exception):
    pass
class QualityError(VideoDownloadException):
    pass


class Scraper:
    def __init__(self,url,quality):
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
        quali = list(qualities.keys())
        links = self.get_all_links()
        available_qualities=[]
        for i in range(len(links)):
            available_qualities.append((quali[i]))
        return available_qualities
    
    '''
        hala ba get_qualities() ma hameye keyfiat haro show mikonim vali dar 
        akhar on quality ro ke karbar mikhaad ro bayad behesh show konim
        baraye error ha bayad y exception bsazim
        tooye sherkatha ma mamoolan exception hay khodemon ro mineviism 
        va kheili mavaaghe hastesh ke masalan mikhay error e QualityError 
        bedi valii  python hamchin exception i be sorate default nadare k 
        raise koni pas bayad khodet yedone dorost koni injori:

        >>> class VideoDownloadError(Exception):
        >>>  	pass
        >>> class QualityError(VideoDownloadError):
        >>>		pass

        ***nokte inke oni k gharare raise konim dar nahayat nabayd kalameye 
        exception dashte bashe fahat error bayad dashte bashe (mesle quality error) 
        nokteye baadi hatmna bayd in class qualityerror az y class vaalede dge ers 
        bari bokone k on khodesh az Exception e built-in e python ers bari kardeeee.

    '''
    
    def get_link(self):
        available_qualities = self.get_qualities()
        links = self.get_all_links()
        if self.quality not in available_qualities:
            raise QualityError(f'This quality in not available \n available qualities are {available_qualities}')
        
        else:
            '''
                mige in self.quality k quality i hastesh k karbar mikhad  ro az dictionary 
                qualities peyda kon masalan age 240 bashe value esh mishe 2 hala in index
                e 2 yani dovomin item az lkist links ro biar vasamon
            '''
            link = links[qualities[self.quality]]
            return link




class Main:
    def __init__(self,url,quality):
        self.url = url
        self.quality = quality
        self.scraper = Scraper(self.url,self.quality)
        
    def download(self):
        '''
            noktei k haast hajme video ha mamoolan ziade va nemikhaym
            be sorate yeja tooye badaneye request harchi hast (link e download e video) 
            download beshe. 
            ye file baz mikonim esmesho mizarim video.mp4 va halati k mikhyam in file baz beshe
            ro wb mizarim yani write-binary beshe. kolan ax,video,ahang hatmn bayad be sorate binary baz beshe. 
            baad az inke print('downloading....') kardim ye darkhaste get be url i ke darim mifrestim
            va stream=true mizarim ke etesali k bargharar kard ro dige ghaat esh nakone dar nazar
            dashte bashim result video ro doenload nmikone faghat etesal ro bargharaar mikonee.
            az result mitonim estefde konim hajme header haro begirim tooye header ha ye item
            darim be esme content_lengthk hajme response ro bhmon mide.
        '''
        
        video_link = self.scraper.get_link()    
        
        with open ('video.mp4' , 'wb') as f:
            print ('downloading............')
            result = requests.get(video_link , stream=True)
            total = result.headers.get('content-length')
            if total is None:
                '''
                    mige age tooye on header e hichi nabod yani response et khali bod haminjori bia y chizi benvis
                '''
                f.write(result.content)
            else:
                for data in result.iter_content(chunk_size= 4096):
                    f.write(data)
                
        
            print(result.headers)
        
        
s=Main(url='https://www.namasha.com/v/y5kreMJe' , quality='720')
s.download()       
