# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

'''
class TianmaoPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('goods.csv', "a", newline="", encoding='utf-8')
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        # 写入文件
        self.writer.writerow((item['good_id'], item['good_name'], item['good_price'], item['good_sales']))
        return item

    def close_spider(self, spider):
        # 关闭文件
        self.file.close()
'''
# 存为json格式


class TianmaoPipeline(object):
    def __init__(self):
        # 打开一个文件
        self.file = open('goods.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()
