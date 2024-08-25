import scrapy
from scrapy_selenium import SeleniumRequest


class ZameenSpider(scrapy.Spider):
    name = 'zameen'
    def start_requests(self):
       yield SeleniumRequest(
            url='https://www.zameen.com/new-projects/saddar_cooperative_market-2208.html',
            wait_time=5,
            callback=self.parse_data
        )
            
    def parse_data(self, response):
        # products = response.xpath('//*[@id="ps-wrapper"]/article/section[1]')
        # for product in products:
            # Product_name = product.xpath(".//h3/a/text()").get()
        Product_name = response.xpath("//*[@id='topContents']/div/div/div[1]/h1/text()").get()
        
        yield{
                'Product name':Product_name,
            }

        # next_page = response.urljoin(response.xpath("//a[@data-testid='NextPage']/@href").get())
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)        
