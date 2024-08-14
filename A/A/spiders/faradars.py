import scrapy
from ..items import AItem

class FaradarsSpider(scrapy.Spider):
    name = "faradars"
    allowed_domains = ["faradars.org"]
    start_urls = ["https://faradars.org/how-to-learn/python-programming"]

    def parse(self, response,**kwargs):
        items = AItem()
        image_url = []
        for fara in response.css('.w-full flex flex-wrap'):
            img_url= fara.css('img').attrib['src']
            image_url.append(img_url)
        items['file_urls']=image_url
        yield items
            

        