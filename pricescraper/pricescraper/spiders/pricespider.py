import scrapy


class PricespiderSpider(scrapy.Spider):
    name = "pricespider"
    allowed_domains = ["www.rightmove.co.uk"]
    start_urls = ["https://www.rightmove.co.uk"]

    def parse(self, response):
        pass
