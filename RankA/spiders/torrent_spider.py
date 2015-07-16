import scrapy;


from RankA.items import TorrentItem


class TorrentSpider(scrapy.Spider):
    name = '1337x'
    allowed_domains = ['1337x.to']
    start_urls = ['http://1337x.to/sub/42/0/']


    def parse(self, response):
        for href in response.xpath('//ul[@class="clearfix"]/li/div[@class="coll-1"]/strong/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_torrent)


    def parse_torrent(self, response):
        for sel in response.css('div.domain-box'):
            item = TorrentItem()
            item['title'] = sel.css('div.top-row > strong::text').extract()[0]
            item['infoHash'] = sel.xpath('//div[@class="infohash-box"]/p/text()').extract()[1].replace(':', '').strip()
            item['seeders'] = sel.xpath('//ul/li/span[@class="green"]/text()').extract()[0]
            item['leechers'] = sel.xpath('//ul/li/span[@class="red"]/text()').extract()[0]
            item['size'] = sel.css('div.category-detail ul > li > span')[3].xpath('text()').extract()[0]
            yield item

