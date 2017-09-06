# -*- coding: utf-8 -*-
import scrapy
from TianQi.items import TianqiItem
# from TianQi.TianQi.items import TianqiItem


class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://lishi.tianqi.com']

    def parse(self, response):
        # 获取所有地区名列表
        area_list = response.xpath('//div[@id="tool_site"]/div[2]/ul/li/a/text()').extract()
        # 获取所有地区链接列表
        url_list = response.xpath('//div[@id="tool_site"]/div[2]/ul/li/a/@href').extract()

        for area, url in zip(area_list, url_list):
            if url == "#":
                continue
            yield scrapy.Request(url, callback=self.parse_area, meta={"area1": area})
            # yield scrapy.Request(url, callback=self.parse_area, meta={"area_1": area})

    def parse_area(self, response):
        area = response.meta["area1"]
        url_detail_list = response.xpath('//*[@id="tool_site"]/div[2]/ul/li/a/@href').extract()
        for url in url_detail_list:
            yield scrapy.Request(url, callback=self.parse_data, meta={"area2":area})

    def parse_data(self, response):
        area = response.meta["area2"]

        data_list = response.xpath('//*[@id="tool_site"]/div[@class="tqtongji2"]/ul')

        for data in data_list[1:]:
            item = TianqiItem()
            item['area'] = area
            item['url'] = response.url
            item['date'] = data.xpath('./li[1]/text()').extract_first()
            if item['date'] == None:
                item['date'] = data.xpath('./li[1]/a/text()').extract_first()
            item['max_tem'] = data.xpath('./li[2]/text()').extract_first()
            item['min_tem'] = data.xpath('./li[3]/text()').extract_first()
            item['weather'] = data.xpath('./li[4]/text()').extract_first()
            item['wind_d'] = data.xpath('./li[5]/text()').extract_first()
            item['wind_p'] = data.xpath('./li[6]/text()').extract_first()
            # print(item['wind_p'])
            yield item




