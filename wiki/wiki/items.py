# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst , MapCompose
 
class WikiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



def to_strip(value):
    return value.strip()

def to_upper(value):
    return value.upper()

class CountrydetailItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags,to_strip,to_upper) , output_processor=TakeFirst())
    capital = scrapy.Field(input_processor=MapCompose(remove_tags,to_strip) , output_processor=TakeFirst())
    population = scrapy.Field(output_processor=TakeFirst())
    