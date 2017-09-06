# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from pymongo import MongoClient


class TianqiPipeline(object):
    def __init__(self):
        ip = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        database_name = settings['DATABASE_NAME']
        collection_name = settings['COLLECTION_NAME']

        # 链接数据库
        self.handler = MongoClient(ip, port)
        # 选择数据
        self.db = self.handler[database_name]
        # 选择集合
        self.col = self.db[collection_name]

    def process_item(self, item, spider):
        # 将item转换成字典
        data = dict(item)
        self.col.insert(data)
        return item

    def close_spider(self, spider):
        self.handler.close()