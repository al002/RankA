import scrapy;


from RankA.items import TorrentItem


class TorrentSpider(scrapy.Spider):
    name = '1337x'
    allowed_domains = ['1337x.to']
    start_urls = ['http://1337x.to/sub/42/0/']
    domain = 'http://1337x.to'


    def parse(self, response):
        for href in response.xpath('//div[@class="tab-detail"]/ul[@class="clearfix"]/li/div[@class="coll-1"]/strong/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_torrent)

        next_page_sel = response.xpath('//div[@class="pagging-box"]/ul/li/a[contains(.//text(), ">>")]')

        if next_page_sel:
            next_link = next_page_sel.xpath('@href').extract()[0]
            yield scrapy.Request(self.domain + next_link, callback=self.parse)


    def parse_torrent(self, response):
        for sel in response.css('div.domain-box'):
            item = TorrentItem()
            item['title'] = sel.css('div.top-row > strong::text').extract()[0]
            item['infoHash'] = sel.xpath('//div[@class="infohash-box"]/p/text()').extract()[1].replace(':', '').strip()
            item['seeders'] = sel.xpath('//ul/li/span[@class="green"]/text()').extract()[0]
            item['leechers'] = sel.xpath('//ul/li/span[@class="red"]/text()').extract()[0]
            item['size'] = sel.css('div.category-detail ul > li > span')[3].xpath('text()').extract()[0]
            yield item
