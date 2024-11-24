from typing import Iterable

import scrapy
from scrapy import Request
from scrapy_selenium import SeleniumRequest

class ZooplaSpiderSpider(scrapy.Spider):
    name = "zoopla_spider"

    def start_requests(self):
        url = "https://zoopla.co.uk"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        source = response.css("body").get()
        return source
    