import scrapy

'''
    mikhaym ba scrapy login koni toye github
    hameye vorodi haye forme github ro handle konim
    befrestim be forme login esh
    username o password ke mibinim dare vase login
    kardan vali y seri input ba type hidden ham dare k maa
    nmibinim tooye inspect esh hastand.
    ona ro ham baayd handle konim
    baazi az in hidden ha ham value nadaran baayad in ghazie ro
    ham handle konim va vaseye onai k value nadraan `unknown` befrestim.
    tooye inspect ha ghesmate form ha chizi k ahamiat dare name e on field e input hasatesh hastesh
'''

class GithubloginwithscrapySpider(scrapy.Spider):
    name = "githubloginwithscrapy"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]
    '''
        in custom settings i ke in paain neveshtam vase ine ke tooye settings
        e in porojeye scrapy ke alan baze man pipeline daram ke faal shode va
        makhsose population hastesh vase file e countrydetail.py ke population e
        country haro raftim crawl kardim alan chon tooye hamon poroje ye file
        spider sakhtim, error i ke mide mide fekr mikone on pipeline male in file.
        so vaseye inke on pipeline ro dar nazar nagirim settings emon ro override kardim.
    '''
    custom_settings = {
        'ITEM_PIPELINES': {}
    }
    def parse(self, response , **kwargs):
        data = {'login':'ghazalmua' , 'password':'*******'}
        
        for hidden in response.css('input[type="hidden"]'):
            data[hidden.attrib['name']]=hidden.attrib.get('value','unknown')
        
        #ba in do khate pain mitonestim bebinim tooye data chi hast(key va vlue) esh ro mitonestim bbinim
        # print(200*'&')    
        # yield data    

        '''
            url bayad behesh bedi. mige in formi k alan poresh kardam be che addressi submitsh konam?
            address mishe hamon safeye   https://github.com   slash session hala chera session? age berimm
            tooye inspect e safeye login e githunb, tooye bakhshe form action ro gozashgte session. yani mire 
            dakhele session pas addresse url nahaimon mishe https://github.com/session   
            
            ye arguman e dige ham formdata hastesh ke bayad hamin dictionary ke haavie user,pass,field 
            haye hidden hastesh ro behesh bedim
            
            akharin arguman callback hastesh mige hala k in dictionary e data ro be addressi ke dadi ferestadam, bayad badesh chekar konam?
            migim boro karai k tooye function e after_login() behet goftim ro anjam bede.
            
             
        '''
        return scrapy.FormRequest(url='https://github.com/session', formdata=data, callback=self.after_login)
    
    def after_login(self,response):
        '''
            plan ine vaghti login shod bere tooye saafeye profile am va email am ro az tooye bio am bekhoone
        '''
        yield response.follow(url='https://github.com/GhazalMUA' ,callback=self.profile )
        
    def profile(self,response):
        email = response.xpath('/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[3]/div[2]/ul/li[2]/a/text()').get()
        print(100*'%')
        yield {'info':email}    
        