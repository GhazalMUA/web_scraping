import scrapy
from scrapy.crawler import CrawlerProcess

class MatalanSpider(scrapy.Spider):
    name='matalan'
    def start_requests(self):
        source = scrapy.Request('https://www.matalan.co.uk/womens/dresses.list')
        yield source
        
    def parse(self, response , **kwargs):
        # for dressitems in response.xpath('//*[@id="ProductList"]/div/div/div[6]/div[1]/ul/li[1]'):
          for dressitems in response.css('.jZZIZP'):
            title = dressitems.css('.kxkXPX::text').get() 
            print(200*'&')
            yield{'title':title}
            
process = CrawlerProcess(settings={
    'FEEDS':
        {'/Users/ghazalhafezi/Documents/web_scraping/matalan.json':{'format':'json' , 'encoding':'utf8'}
        }
})            

process.crawl(MatalanSpider)
process.start()
