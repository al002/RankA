import scrapy;

class TorrentSpider(scrapy.Spider):
    name = "1337x"
    allowed_domains = ["1337x.to"]
    start_urls = ["http://1337x.to/sub/42/0/"]


    def parse(self, response):
        print(response.body)
