import scrapy
from scrapy_selenium import SeleniumRequest

class NeweggSpider(scrapy.Spider):
    name = 'newegg'
    def start_requests(self):
        for i in range(1,100): 
            yield SeleniumRequest(
                url=f'https://www.newegg.com/Laptops-Notebooks/SubCategory/ID-32/Page-{i}?Tid=6740&source=f',
                wait_time=12,
                callback=self.parse
            )

    def parse(self, response):
        products = response.xpath("//div[@class='page-content']/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/div/div/a")
        for product in products:
            link = response.urljoin(product.xpath(".//@href").get())
            yield response.follow(url=link, callback=self.parse_data)
            
    def parse_data(self, response):
        Product_name = response.xpath("//div[@class='product-wrap']/h1/text()[1]").get()
        # Harddrive_size = response.xpath("//div[@class='product-bullets']/ul/li[2]/text()").get()
        # CPU_name = response.xpath("//div[@class='product-bullets']/ul/li[1]/text()").get()
        # Discrete_GPU_name = response.xpath("//div[@class='product-bullets']/ul/li[3]/text()").get()
        # Screen_size = response.xpath("//*[@id='product-details']/div[2]/div[2]/table[3]/tbody/tr[4]/td/text()").get()
        # Model_number = response.xpath("//*[@id='product-details']/div[2]/div[2]/table[2]/tbody/tr[3]/td/text()").get()
        Price = response.xpath("//div[@class='product-price']/ul/li[@class='price-current']/strong/text()").get()
        field1 = response.xpath("(//div[@class='product-bullets']/ul/li/text())[1]").get()
        field2 = response.xpath("(//div[@class='product-bullets']/ul/li/text())[2]").get()
        field3 = response.xpath("(//div[@class='product-bullets']/ul/li/text())[3]").get()
        # rating = response.xpath("//div[@class='product-price']/ul/li[@class='price-current']/strong/text()").get()
        # Resolution = response.xpath("//div[@class='product-price']/ul/li[@class='price-current']/strong/text()").get()
        
        yield{
            'Product title':Product_name,
            'Price (USD)':Price,
            'Field1':field1,
            'Field2':field2,
            'Field3':field3,
            # 'Ratings':rating,
            # 'CPU name':CPU_name,
            # 'Ram and Storage':Harddrive_size,
            # 'Discrete GPU name':Discrete_GPU_name,
            # 'Screen size':Screen_size,
            # 'Model number':Model_number,
            # 'Resolution':Resolution,
        }     
