# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianmaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    # 设置字段名
    # 商品名称
    goods_name = scrapy.Field()
    # 商品id
    goods_id = scrapy.Field()
    # 商品价格
    goods_price = scrapy.Field()
    # 商品销量
    goods_volume = scrapy.Field()
    # 评论数
    comment = scrapy.Field()