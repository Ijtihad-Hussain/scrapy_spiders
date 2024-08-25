import scrapy
from scrapy_selenium import SeleniumRequest

class WalmartSpider(scrapy.Spider):
    name = 'walmart'
    def start_requests(self):
        yield SeleniumRequest(
            url='https://www.walmart.com/browse/electronics/laptops/3944_3951_1089430?sort=best_match&cat_id=3944_3951_1089430_1230091_132960&stores=3081&ps=40',
            wait_time=12,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//div[@class='flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3']/div/div/div/a")
        for product in products:
            link = product.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_data)
            
        next_page = response.urljoin(response.xpath("//a[@data-testid='NextPage']/@href").get())
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)    
            
    def parse_data(self, response):
        Product_name = response.xpath("//*[@id='__next']/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/section/h1/text()").get()
        # Harddrive_size = response.xpath("(//ul[@class='specifications-list'])[1]/li[5]/div[2]/text()").get()
        # RAM_size = response.xpath("")
        # CPU_name = response.xpath("")
        # Discrete_GPU_name = response.xpath("")
        # Screen_size = response.xpath("")
        # Model_number = response.xpath("")
        Price = response.xpath("//*[@id='__next']/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]/span/span[2]/text()").get()
        rating = response.xpath("//*[@id='__next']/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[1]/section/div/div[2]/span[2]/text()").get()
        data1 = response.xpath("((//div[@class='w_AM expand-collapse-content'])[2]/div/div/div/p/span/text())[1]").get()
        field1 = response.xpath("((//div[@class='w_AM expand-collapse-content'])[2]/div/div/div/h3/text())[1]").get()
        
        yield{
            'Product name':Product_name,
            'Price':Price,
            'Ratings':rating,
            field1:data1,
            # 'Harddrive size':Harddrive_size,
            # 'RAM size':RAM_size,
            # 'CPU name':CPU_name,
            # 'Discrete GPU name':Discrete_GPU_name,
            # 'Screen size and resolution':Screen_size,
            # 'Model number':Model_number,
        }
        

        