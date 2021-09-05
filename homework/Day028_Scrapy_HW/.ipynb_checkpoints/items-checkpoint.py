# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Day028ScrapyHwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    allowed_domains = ['www.ptt.cc/bbs/WorldCup/M.1625507063.A.0B6.html']
    start_urls = ['https://www.ptt.cc/bbs/WorldCup/M.1625507063.A.0B6.html']
    def parse(self, response):
        title = response.xpath('//*[@id="main-content"]/div[3]/span[2]').get()
        content = response.xpath('//*[@id="main-content"]//span').getall()
        print(title)
        print(content)
        pass
