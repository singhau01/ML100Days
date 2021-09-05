import scrapy


class PttWorldcupSpider(scrapy.Spider):
    name = 'ptt_worldcup'
    allowed_domains = ['www.ptt.cc/bbs/WorldCup/M.1625507063.A.0B6.html']
    start_urls = ['http://www.ptt.cc/bbs/WorldCup/M.1625507063.A.0B6.html/']

    def parse(self, response):
        pass
