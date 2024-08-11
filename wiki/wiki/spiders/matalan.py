import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MatalanSpider(CrawlSpider):
    name = "matalan"
    allowed_domains = ["www.matalan.co.uk"]
    start_urls = ["https://www.matalan.co.uk/womens/dresses.list"]

    rules = (Rule(LinkExtractor(allow=r"/clothing/"), callback="parse_item", follow=False),)

    def parse_item(self, response):
        item = {}
        # item['product_id'] = response.xpath('//*[@id="productDetails-b0766f1d-0ebe-49ce-920c-3a29fd34e9e5"]/text()').get()        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item['product_id'] = response.xpath('//*[@id="productDetails"]/@data-product-id').get()   
        # item['product_id'] = response.xpath('//*[contains(@id, "productDetails")]/div/section//div[@data-product-id]/@data-product-id').get()
        item['product_id'] = response.xpath('//*[contains(@id, "productDetails")]/div/section/div/div[4]/div/text()').get()

        #item["name"] = response.xpath('//div[@id="name"]').get()
        
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item
