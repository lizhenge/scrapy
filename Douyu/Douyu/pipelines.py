# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import image
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_link'])

    def item_completed(self, results, item, info):
        # 获取图片的路径
        image = [data['path'] for ok, data in results if ok]
        # 拼接原始图片的路径
        old_name = self.IMAGES_STORE + os.sep + image[0]
        # 拼接
        new_name = self.IMAGES_STORE + os.sep + image[0].split(os.sep)[0] + os.sep + item['nick_name'] + '.jpg'

        os.rename(old_name, new_name)
        item['image_path'] = new_name

        return item