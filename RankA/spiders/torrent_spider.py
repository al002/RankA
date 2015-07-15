import scrapy;

class TorrentSpider(scrapy.Spider):
    name = '1337x'
    allowed_domains = ['1337x.to']
    start_urls = ['http://1337x.to/sub/42/0/']


    def parse(self, response):
        for sel in response.xpath('//ul[@class="clearfix"]/li'):
            title = sel.xpath('div[@class="coll-1"]/strong/a/text()').extract();
            print(title)
