import scrapy


class ScrapeScrapy27aprilSpider(scrapy.Spider):
    name = "scrape_scrapy_27April"
    allowed_domains = ["www.actualized.org"]
    start_urls = ["http://www.actualized.org/"]

    def parse(self, response):
        pass
