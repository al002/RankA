# -*- coding: utf-8 -*-
import scrapy
import re


from RankA.items import MovieIdItem


class MovieDoubanSpider(scrapy.Spider):
    name = "movie.douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://movie.douban.com/tag/',
    )


    def parse(self, response):
        for href in response.css('table.tagCol td a').xpath('.//@href'):
            tag_url = response.urljoin(href.extract())
            yield scrapy.Request(tag_url.replace('?focus=', ''), callback=self.parse_id)


    def parse_id(self, response):
        if response.css('div.movie-list dl'):
            for href in response.css('div.movie-list dl dd a').xpath('.//@href'):
                item = MovieIdItem()
                movie_url = response.urljoin(href.extract())
                movie_id = re.search('\d+', movie_url).group(0)
                item['movie_id'] = movie_id
                yield item

            next_page_sel = response.css('div.paginator span.next a').xpath('.//@href')
            next_page_link = response.urljoin(next_page_sel.extract_first())
            yield scrapy.Request(next_page_link, callback=self.parse_id)


