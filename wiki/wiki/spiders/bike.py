import scrapy
from w3lib.html import remove_tags


class BikeDetailSpider(scrapy.Spider):
    name = "bikedetail"
    start_urls = ["https://www.bike-discount.de/de/e-bike-kaufen"]


    def parse(self, response , **kwargs):
        for bike in response.css('div.product--box'):
            name = remove_tags(bike.css('a.product--title').get()).strip()
            price = remove_tags(bike.css('.product--price').get()).strip()
            print('*'*200)
            yield {'name':name ,'price':price}
            
        next_page = response.css('a.page-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

        # Logging
        self.log(f"Scraped {response.url}")
            
            
            
            
            
            
            
            
            
