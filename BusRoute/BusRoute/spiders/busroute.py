# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from BusRoute.items import BusrouteItem

# 1---导入scrapy_redis类
from scrapy_redis.spiders import RedisCrawlSpider

# ----2 修改类的继承


class BusroutSpider(RedisCrawlSpider):
    name = 'busroute'
    allowed_domains = ['bus.mapbar.com']
    # ----3 修改初始URL
    # start_urls = ['http://bus.mapbar.com/beijing/xianlu/']
    # url_list = []
    rules = (
        # 获取列表页面的url
        Rule(LinkExtractor(allow=r'/beijing/xianlu_.'), follow=True),
        # 获取详情页面的url
        Rule(LinkExtractor(allow=r'/beijing/xianlu/(\d\d\d)+lu'), callback='parse_item',follow=False),
    )

    # ----5 编写redis_key
    redis_key = 'crawlspider:start_urls'

    def parse_item(self, response):
        # 创建一个item实例
        item = BusrouteItem()
        # 获取公交线路名
        item['route_name'] = response.xpath(r'//h1/text()').extract_first()
        # 获取起点站
        item['starting_point'] = response.xpath(r'//h3/b[1]/text()').extract_first()
        # 获取终点站
        item['ending_point'] = response.xpath(r'//h3/b[2]/text()').extract_first()
        # 起点站首末班时间
        item['start2end_begin'] = response.xpath(r"//ul[@class='clr']/p[2]/text()").extract_first()
        # 终点站首末班时间
        item['start2end_end'] = response.xpath(r"//ul[@class='clr']/p[3]/text()").extract_first()
        # 汽车公司
        item['company'] = response.xpath(r'//dd/ul/li[4]/text()').extract_first()
        # 更新时间
        item['update_time'] = response.xpath(r"//div[@class='publicBox']/span/text()").extract_first().split(':')[-1]
        # 获取站点名
        name_list = response.xpath(r"//ul[@id='scrollTr']/li/a/em/text()").extract()
        res = []
        # 循环匹配站点序号
        for index, name in enumerate(name_list, 1):
            name = str(index) + '.' + name 
            res.append(name)
        item['line'] = res

        # 发车间隔
        item['car_interval'] = response.xpath(r'//dd/ul/p[1]/text()').extract_first()

        yield item

