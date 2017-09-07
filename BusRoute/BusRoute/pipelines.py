# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class BusroutePipeline(object):
	def __init__(self):
		# 创建存储数据的文件
		self.file = open('BusRoute.json','w',encoding='utf-8')

	# 定义对数据的操作
	def process_item(self, item, spider):
		# 将item数据转换成字典
		data = dict(item)
		# 将字典转化为字符串
		res = json.dumps(data, ensure_ascii=False) + ',\n'
		# 写入文件
		self.file.write(res)
		return item


	def close_spider(self, spider):
		# 关闭存储数据的文件
		self.file.close()