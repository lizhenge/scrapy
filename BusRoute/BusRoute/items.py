# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BusrouteItem(scrapy.Item):
	# define the fields for your item here like:
	# 数字开头的线路
	# route_N = scrapy.Field()
	# 数字开头线路下的公交线路
	# route_N_bus= scrapy.Field()
	# 字母开头的线路
	# route_C = scrapy.Field()
	# 字母开头线路下的公交线路
	# route_C_bus = scrapy.Field()
	# 公交线路名称
	route_name = scrapy.Field()
	# 起点站
	starting_point = scrapy.Field()
	# 终点站
	ending_point = scrapy.Field()
	# 起点站首班末班时间
	start2end_begin = scrapy.Field()
	# 终点站首班末班时间
	start2end_end = scrapy.Field()
	# 汽车公司
	company = scrapy.Field()
	# 更新时间
	update_time = scrapy.Field()
	# 票制
	ticket_system = scrapy.Field()
	# 发车间隔
	car_interval = scrapy.Field()
	# 路线
	line = scrapy.Field()
	