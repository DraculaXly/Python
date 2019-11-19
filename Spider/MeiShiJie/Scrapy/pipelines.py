# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MsjPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.json', 'w', encoding='utf-8')
        self.result = []

    def close_spider(self, spider):
        json.dump(self.result, self.file, ensure_ascii=False, indent=4)
        self.file.close()

    def process_item(self, item, spider):
        self.result.append(dict(item))
        return item
