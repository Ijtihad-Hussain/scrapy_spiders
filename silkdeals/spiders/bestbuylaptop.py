from unittest import skipUnless
import scrapy
from scrapy_selenium import SeleniumRequest

class BestbuylaptopSpider(scrapy.Spider):
    name = 'bestbuylaptop'
    def start_requests(self):
        urls = [
                'https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?id=pcmcat138500050001&intl=nosplash',
                'https://www.bestbuy.com/site/desktop-computers/all-desktops/pcmcat143400050013.c?id=pcmcat143400050013&intl=nosplash'
                ]
        for i in range(2):
            yield SeleniumRequest(
                url=urls[i],
                wait_time=12,
                callback=self.parse
            )

    def parse(self, response):
        products = response.xpath("//h4[@class='sku-header']/a")
        for product in products:
            # link = product.xpath(".//@href").get()
            # yield{
            #     'link':link
            # }
            link = response.urljoin(product.xpath(".//@href").get())
            yield response.follow(url=link, callback=self.parse_data)
            
        next_page = response.urljoin(response.xpath("//div[@class='footer-pagination']/a[2]/@href").get())
        if next_page:
             yield scrapy.Request(url=next_page, callback=self.parse)
            
    def parse_data(self, response):
        Product_name = response.xpath("//div[@class='sku-title']/h1/text()").get()
        # Harddrive_size = response.xpath("(//ul[@class='specifications-list'])[1]/li[5]/div[2]/text()").get()
        # RAM_size = response.xpath("")
        # CPU_name = response.xpath("")
        # Discrete_GPU_name = response.xpath("")
        # Screen_size = response.xpath("")
        Model_number = response.xpath("//div[@class='model product-data']/span[@class='product-data-value body-copy']/text()").get()
        Price = response.xpath("(//div[@class='priceView-hero-price priceView-customer-price'])[1]/span[1]/text()").get()
        Review = response.xpath("//div[@class='c-ratings-reviews flex c-ratings-reviews-small align-items-center gap-50 ugc-ratings-reviews flex-wrap small-gaps text-center']/span[1]/text()").get()
        sku = response.xpath("//div[@class='sku product-data']/span[2]/text()").get()
        
        yield{
            'Product title':Product_name,
            'Price':Price,
            'Model number':Model_number,
            'Ratings':Review,
            'SKU':sku,
            # 'Harddrive size':Harddrive_size,
            # 'RAM size':RAM_size,
            # 'CPU name':CPU_name,
            # 'Discrete GPU name':Discrete_GPU_name,
            # 'Screen size and resolution':Screen_size,
        }
        
