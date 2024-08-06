import scrapy
from ..items import CountrydetailItem
from scrapy.loader import ItemLoader


class CountrydetailSpider(scrapy.Spider):
    name = "countrydetail"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]


    def parse(self, response):
        for country in response.css('div.country'):
            l=ItemLoader(item=CountrydetailItem(),selector=country)
            l.add_css('name' , 'h3.country-name')
            l.add_css('capital' , 'span.country-capital::text')
            l.add_css('population' , 'span.country-population::text')
            
            yield l.load_item()
            
