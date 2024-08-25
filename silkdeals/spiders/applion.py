# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest

class ApplionSpider(scrapy.Spider):
    name = 'applion'
    
    def start_requests(self):
        yield SeleniumRequest(
            url='https://applion.jp/android/word/3D/',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//ul[@class='rownormal']/li/a")
        for product in products:
            link = response.urljoin(product.xpath(".//@href").get())
            name = product.xpath(".//div/div[2]/div[1]/p[1]/text()").get()
            developer = product.xpath(".//div/div[2]/div[3]/p/text()").get()
            category = product.xpath(".//div/div[2]/div[4]/p/span/text()").get()
            yield response.follow(url=link, callback=self.parse_apps, meta={'app_name': name, 'developer': developer, 'category':category})
            
    def parse_apps(self, response):
        name = response.request.meta['app_name']
        developer = response.request.meta['developer']
        category = response.request.meta['category']
        apps = response.xpath("(//div[@class='container'])[3]")
        for app in apps:   
            yield {
                'app_name': name,
                'url': response.urljoin(app.xpath(".//div[@class='marea_main']/div[1]/div[1]/table/tbody/tr/td/div/div[2]/a/@href").get()),
                'developer': developer,
                'description': app.xpath(".//div[2]/p/text()").get(),
                'category':category,
                'recommended_age': app.xpath(".//div[3]/div/div[34]/div[2]/div/dl[3]/dd/text()").get(),
                'in_app_purchase': app.xpath(".//div[3]/div/div[34]/div[2]/div/dl[4]/dd/text()").get(),
                'update_date': app.xpath(".//div[3]/div/div[34]/div[2]/div/dl[5]/dd/text()").get(),
                'number_of_installations': app.xpath(".//div[3]/div/div[34]/div[2]/div/dl[6]/dd/text()").get(),
            }