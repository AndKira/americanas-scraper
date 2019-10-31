# -*- coding: utf-8 -*-
import scrapy
import json

class AmericanasSpider(scrapy.Spider):
    name = 'Americanas'
    allowed_domains = ['americanas.com.br/']
    start_urls = ['http://americanas.com.br/produto/134186808']

    def parse(self, response):
        html_body = response.css('div#content script::text').getall()
        html_body = [i.replace('\\\"', '').replace('\\', '') for i in html_body ]
        jsonresponse = json.loads(html_body[0])

        code   = jsonresponse["@graph"][2]["url"].replace('https://www.americanas.com.br/produto/', '')
        name   = jsonresponse["@graph"][4]["name"]
        img    = jsonresponse["@graph"][4]["image"]["url"]
        seller = jsonresponse["@graph"]["name"]

        yield {"id": code, "name": name, "img": img, "seller": seller, "json": jsonresponse["@graph"][4]}