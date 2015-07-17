# -*- coding: utf-8 -*-
import scrapy
import re
import json


class MovieDoubanSpider(scrapy.Spider):
    name = "movie.douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://www.douban.com/tag/科幻/movie',
    )


    def parse(self, response):
        if response.css('div.movie-list dl'):
            for href in response.css('div.movie-list dl dd a').xpath('.//@href'):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse_movie)

            next_page_sel = response.css('div.paginator span.next a').xpath('.//@href')
            next_page_link = response.urljoin(next_page_sel.extract_first())
            yield scrapy.Request(next_page_link, callback=self.parse)


    def parse_movie(self, response):
        pass