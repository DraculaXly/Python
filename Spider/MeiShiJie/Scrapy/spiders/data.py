# -*- coding: utf-8 -*-
import scrapy
import json
from msj.items import MsjItem

class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['meishij.net']

    def start_requests(self):
        for i in range(1, 10):
            url = 'http://www.meishij.net/chufang/diy/jiangchangcaipu/?&page=' + str(i)
            yield scrapy.Request(url=url, encoding='utf-8', callback=self.parse)
            yield

    def parse(self, response):
        item = MsjItem()
        for i in response.xpath("//div[@class='listtyle1']"):
            title = i.xpath(".//div[@class='c1']//strong/text()").extract_first()
            img_url = i.xpath(".//img/@src").extract_first()
            make_url = i.xpath(".//a/@href").extract_first()
            item['title'] = title
            item['img_url'] = img_url
            item['make_url'] = make_url
            yield item
        pass