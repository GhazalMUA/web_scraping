'''
    az request mikhaym estefade bokonim ke bad az inke docharkhe 
    ro gereft request bzane b link rooye docharkhe va varede safeye
    detail e on docharkhe beshe va price ro bekhone vasamon.
'''            
import scrapy
from w3lib.html import remove_tags
from scrapy.linkextractors import LinkExtractor

class RequesttSpider(scrapy.Spider):
    name = 'requestt'
    start_urls =['https://www.bike-discount.de/de/e-bike-kaufen']
    
    l=LinkExtractor()                                                    #ye instance az linkextractors misazim.
    
    def parse(self,response,**kwargs):
        for bike in response.css('div.product--info'):
            link = bike.css('a.product--title::attr(href)').get()
            yield scrapy.Request(url=link,callback=self.parse_bike)      #parse_bike vazife ash ine ke az dakhele safeye joziyat eetelaat ro bekeshe biron
    
    def parse_bike(self,response,**kwargs):
        price = remove_tags(response.css('span.price--content::text').get()).strip()
        yield {'price':price}