
import scrapy


BOT_NAME = 'silkdeals'

SPIDER_MODULES = ['silkdeals.spiders']
NEWSPIDER_MODULE = 'silkdeals.spiders'

# USER_AGENT = 'hopper (+http://www.crunchbase.com)'


ROBOTSTXT_OBEY = True


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'silkdeals.middlewares.UserAgentRotatorMiddleware': 400,
}

#SELENIUM
from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # '-headless' if using firefox instead of chrome


FEED_EXPORT_ENCODING = 'utf-8'