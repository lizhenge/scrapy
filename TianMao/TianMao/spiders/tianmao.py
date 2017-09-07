# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from TianMao.items import TianmaoItem


class TianmaoSpider(scrapy.Spider):
    name = 'tianmao'
    # 设置域名限制
    allowed_domains = ['gxg.tmall.com']
    # 设置起始的url,将页码数据用｛｝括起来，在之后改动
    start_urls = ['https://gxg.tmall.com/i/asynSearch.htm?_ksTS=1504700307943_364&callback=jsonp365&mid=w-14439341247-0&wid=14439341247&path=/search.htm&search=y&spm=a1z10.3-b-s.w4011-14439341247.285.46f16db0BsfqV8&scene=taobao_shop&pageNo={}&tsearch=y']
    # 设置起始的页码，没写时指第一页
    num = 2

    def parse(self, response):
        # 通过response获取到整个网站总页码数
        max_page = str(response.xpath(r'''//div[@class='\"filter']/p/b/text()''').extract_first()).split("/")[1]
        # 将单个页面中的所有节点全部取出来
        node_list1 = response.xpath(r'''//div[@class='\"item4line1\"']/dl''')[:-8]
        for node_list2 in node_list1:
            # 构造一个空的列表
            goods_list = []
            # 把所有的节点添加到列表中
            goods_list.append(node_list2)
            # 遍历节点列表获得所有节点
            for goods in goods_list:
                # 创建一个ｉｔｅｍ对象
                item = TianmaoItem()
                # 获取商品名字，节点取到的为名字+＃+ｉｄ的字符串，用ｓｐｌｉｔ方法以＃切割取到下标为0的元素
                item['goods_name'] = str(goods.xpath('./dd[2]/a/text()').extract_first()).split("#")[0]
                # 获取商品价格，用ｓｔｒｉｐ方法去掉空格
                item['goods_price'] = str('￥')+str(goods.xpath('./dd[2]/div/div[1]/span[2]/text()').extract_first()).strip()
                # 获取商品数量
                item['goods_volume'] = str(goods.xpath('./dd[2]/div/div[2]/span/text()').extract_first()).strip()
                # 获取评论量
                item['comment'] = goods.xpath('./dd[3]/div/h4/a/span/text()').extract_first()
                try:
                    # 在商品中有个别商品名和id没有#链接，而是直接链接的
                    item['goods_id'] = str(goods.xpath('./dd[2]/a/text()').extract_first()).split("#")[1]
                except Exception as e:
                    # 如果遇到没有#链接的数据则直接用切片取出ｉｄ
                    item['goods_id'] = str(goods.xpath('./dd[2]/a/text()').extract_first()[-10:]).strip()
                    # 使用切片取出商品名
                    item['goods_name'] = goods.xpath('./dd[2]/a/text()').extract_first()[:-10]
                    print(e)
               # 返回ｉｔｅｍ
                yield item
        # 设置ｎｅｘｔ_ｕｒｌ，这里的下一页标签无法取到链接地址所以要自己设置下一页的ｕｒｌ
        next_url = self.start_urls[0].format(self.num)
        print(next_url)
        try:
            print("next_url is {}".format(next_url))
            # 进行判断，如果页码比页码最大值小，则回调解析函数,如果大于的话则停止回调
            if self.num <= int(max_page):
                self.num += 1
                yield Request(url=next_url, callback=self.parse)
                print("开始第{}页的下载".format(self.num))
            else: print("所有页面已打印完成")
        except Exception as e:
            print(e)
            return













