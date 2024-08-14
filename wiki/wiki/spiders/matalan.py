import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MatalanSpider(CrawlSpider):
    name = "matalan"
    allowed_domains = ["www.matalan.co.uk"]
    start_urls = ["https://www.matalan.co.uk/womens/dresses.list"]

    rules = (Rule(LinkExtractor(allow=r"/clothing/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        item['product_id'] = response.xpath('//*[contains(@id, "productDetails")]/div/section/div/div[4]/div/text()').get()

        return item
