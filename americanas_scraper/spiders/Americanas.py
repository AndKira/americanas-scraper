# -*- coding: utf-8 -*-
import scrapy
import json
from americanas_scraper.items import AmericanasScraperItem

class AmericanasSpider(scrapy.Spider):
    name = 'Americanas'
    allowed_domains = ['americanas.com.br/']
    #Celular da primeira busca availability = 'http://schema.org/InStock'
    #start_urls = ['http://americanas.com.br/produto/134186808']
    #Fritadeira para verificação de voltagem availability = 'http://schema.org/OutOfStock'
    start_urls = ['https://www.americanas.com.br/produto/44852639/turbofryer-philips-walita?api=b2wads&chave=b2wads_5cd48f779049080541bf899b_436042004752_44852639_d5985a5c-b71a-4d1c-88ab-d0960a7c512a&pos=2&sellerId=436042004752&sellerName=Polishop&sellerid=436042004752&sellername=Polishop&voltagem=110']

    def parse(self, response):
        html_body = response.css('div#content script::text').getall()
        html_body = [i.replace('\\\"', '').replace('\\', '') for i in html_body ]
        jsonresponse = json.loads(html_body[0])

        code   = jsonresponse["@graph"][2]["url"].replace('https://www.americanas.com.br/produto/', '')
        breadcrumb = []
        for position in jsonresponse["@graph"][3]["itemListElement"]:
            breadcrumb.append(position["item"]["name"])
        name            = jsonresponse["@graph"][4]["name"]
        img             = jsonresponse["@graph"][4]["image"]["url"]
        seller          = jsonresponse["@graph"][0]["name"]
        availability    = jsonresponse["@graph"][4]["offers"]["availability"]
        if (availability == 'http://schema.org/InStock'):
            price    = jsonresponse["@graph"][4]["offers"]["price"]
        elif (availability == 'http://schema.org/OutOfStock'):
            price    = "Fora de estoque"


        informacoes = AmericanasScraperItem(code=code, breadcrumb=breadcrumb, name=name, img=img, seller=seller, price=price)
        yield informacoes