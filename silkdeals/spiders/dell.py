import scrapy
from scrapy_selenium import SeleniumRequest

class DellSpider(scrapy.Spider):
    name = 'dell'
    def start_requests(self):
        i =1
        for i in range(11):
            urls=[  'dell-laptops/sr/laptops/xps-laptops',
                    'dell-laptops/sr/laptops/inspiron-laptops',
                    'dell-laptops/sr/laptops/alienware-laptops',
                    'dell-laptops/sr/laptops/g-series',
                    'dell-laptops/sr/laptops/chromebook-laptops',
                    'desktop-computers/sr/desktops/xps-desktops',
                    'desktop-computers/sr/desktops/inspiron-desktops',
                    'desktop-computers/sr/desktops/alienware-desktops',
                    'gaming-laptops/sr/game-laptops/alienware-laptops',
                    'gaming-laptops/sr/game-laptops/g-series',
                    'gaming-and-games/sr/game-desktops/alienware-desktops',
]
        
            yield SeleniumRequest(
                url=f'https://www.dell.com/en-us/shop/{urls[i]}?page=1',
                wait_time=5,
                callback=self.parse_data
            )

    # def parse(self, response):
    #     products = response.xpath("//div[@class='bottom-offset-small']/div[1]/article/div[2]/ul/li/a")
    #     for product in products:
    #         link = response.urljoin(product.xpath(".//@href").get())
    #         if link:
    #             yield response.follow(url=link, callback=self.parse_data)
            
    def parse_data(self, response):
        products = response.xpath('//*[@id="ps-wrapper"]/article/section[1]')
        for product in products:
            Product_name = product.xpath(".//h3/a/text()").get()
            Harddrive_size = product.xpath(".//div[7]/div[1]/div[5]/text()").get()
            RAM_size = product.xpath("div[7]/div[1]/div[4]/text()").get()
            CPU_name = product.xpath(".//div[7]/div[1]/div[1]/text()").get()
            Discrete_GPU_name = product.xpath("div[7]/div[1]/div[3]/text()").get()
            Screen_size = product.xpath(".//div[7]/div[2]/div[1]/text()").get()
            # Model_number = product.xpath("").get()
            Price = product.xpath(".//div[5]/div[2]/span[2]/text()").get()
            rating = product.xpath(".//div[@class='ps-ratings-and-reviews']/a/span[4]/text()").get()
        
            yield{
                'Product name':Product_name,
                'Storage':Harddrive_size,
                'RAM size':RAM_size,
                'CPU name':CPU_name,
                'Discrete GPU name':Discrete_GPU_name,
                'Screen size and resolution':Screen_size,
                # 'Model number':Model_number,
                'Price':Price,
                'Ratings':rating,
            }