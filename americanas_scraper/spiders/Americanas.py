# -*- coding: utf-8 -*-
import scrapy


class AmericanasSpider(scrapy.Spider):
    name = 'Americanas'
    allowed_domains = ['americanas.com.br']
    start_urls = ['http://americanas.com.br/']

    def parse(self, response):
        pass
