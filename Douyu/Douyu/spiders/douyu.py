# -*- coding: utf-8 -*-
import json

import scrapy

from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    page_num = 1
    host = 'https://www.douyu.com/gapi/web/getCid2list?isAjax=1&cid=201&page='
    start_urls = [host]

    def parse(self, response):

        res = json.loads(response.body)
        data_list = res['data']['list']
        for data in data_list:
            item = DouyuItem()
            item['nick_name'] = data['nick_name']
            item['room_name'] = data['room_name']
            item['uid'] = data['owner_uid']
            item['image_link'] = data['room_src']

            yield item

        if len(data_list) != 0:
            self.page_num += 1
            next_url = self.host + str(self.page_num)

            yield scrapy.Request(next_url, callback=self.parse)


