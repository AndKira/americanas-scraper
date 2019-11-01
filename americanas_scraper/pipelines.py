# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AmericanasScraperPipeline(object):
    def open_spider(self, spider):
      self.file = open('produto.json', 'w')

    def close_spider(self, spider):
      self.file.close()

    def process_item(self, item, spider):
      line =  json.dumps(dict(item), ensure_ascii=False) + '\n'
      self.file.write(line)
      return item