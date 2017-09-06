# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 地区名
    area = scrapy.Field()
    # 采集地址
    url = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 最高气温
    max_tem = scrapy.Field()
    # 最低气温
    min_tem = scrapy.Field()
    # 天气
    weather = scrapy.Field()
    # 风向
    wind_d = scrapy.Field()
    # 风力
    wind_p = scrapy.Field()
