import scrapy;


from RankA.items import TorrentItem


class TorrentSpider(scrapy.Spider):
    name = '1337x_update'
    allowed_domains = ['1337x.to']
    start_urls = ['http://1337x.to/sub/42/0/', 'http://1337x.to/sub/41/0/', 'http://1337x.to/cat/Anime/0/']


    def parse(self, response):
        for href in response.xpath('//div[@class="tab-detail"]/ul[@class="clearfix"]/li/div[@class="coll-1"]/strong/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_torrent)

        next_page_sel = response.xpath('//div[@class="pagging-box"]/ul/li/a[contains(.//text(), ">>")]')

        limit = response.css('div.pagging-box ul li.active a::text').extract_first()

        if next_page_sel and int(limit) < 5:
            next_link = response.urljoin(next_page_sel.xpath('@href').extract_first())
            yield scrapy.Request(next_link, callback=self.parse)


    def parse_torrent(self, response):
        for sel in response.css('div.domain-box'):
            item = TorrentItem()
            item['title'] = sel.css('div.top-row > strong::text').extract_first()
            item['magnet_uri'] = sel.xpath('.//ul[@class="download-links"]/li[1]/a/@href').extract_first()
            item['seeders'] = sel.xpath('.//ul/li/span[@class="green"]/text()').extract_first()
            item['leechers'] = sel.xpath('.//ul/li/span[@class="red"]/text()').extract_first()
            item['size'] = sel.css('div.category-detail ul > li > span')[3].xpath('text()').extract_first()
            item['category'] = sel.xpath('.//ul[@class="category-name"]/li/a/text()').extract()
            yield item

