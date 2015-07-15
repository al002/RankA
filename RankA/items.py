# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TorrentItem(scrapy.Item):
    title = scrapy.Field();
    infoHash = scrapy.Field();
    seeders = scrapy.Field();
    leechers = scrapy.Field();
    size = scrapy.Field();
    category = scrapy.Field();
    # define the fields for your item here like:
    # name = scrapy.Field()
