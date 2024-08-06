from typing import Any
import scrapy
from scrapy.http import Response



class Wikipedia(scrapy.Spider):
    name='wiki'
    start_urls=[
        'https://en.wikipedia.org/wiki/Michael_Jackson'
    ]
    
    def parse(self, response: Response, **kwargs: Any) -> Any:
        title = response.css('title').extract()
        yield {'titleeeeeeeeeeeeeeeeeeeeeeeeeeee':title}