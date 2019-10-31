# -*- coding: utf-8 -*-
import scrapy
import json

class AmericanasSpider(scrapy.Spider):
    name = 'Americanas'
    allowed_domains = ['americanas.com.br/']
    #Celular da primeira busca availability = 'http://schema.org/InStock'
    #start_urls = ['http://americanas.com.br/produto/134186808']
    #Fritadeira para verificação de voltagem availability = 'http://schema.org/OutOfStock'
    start_urls = ['http://americanas.com.br/produto/133659765']

    def parse(self, response):
        html_body = response.css('div#content script::text').getall()
        html_body = [i.replace('\\\"', '').replace('\\', '') for i in html_body ]
        jsonresponse = json.loads(html_body[0])

        code   = jsonresponse["@graph"][2]["url"].replace('https://www.americanas.com.br/produto/', '')
        breadcrumb = []
        for position in jsonresponse["@graph"][3]["itemListElement"]:
            breadcrumb.append(position["item"]["name"])
        name   = jsonresponse["@graph"][4]["name"]
        img    = jsonresponse["@graph"][4]["image"]["url"]
        seller = jsonresponse["@graph"][0]["name"]
        price  = jsonresponse["@graph"][4]["offers"]["availability"]


        yield {"id": code, "breadcrumb": breadcrumb, "name": name, "img": img, "seller": seller, "price": price}