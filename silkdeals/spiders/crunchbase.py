import scrapy
from scrapy_selenium import SeleniumRequest

class CrunchbaseSpider(scrapy.Spider):
    name = 'crunchbase'
    def start_requests(self):
        i =1
        for i in range(3):
            urls=[  'meditell',
                    'hopper',
                    'flynumber-com',
                    'ecomchef',
                    'medical-systems-ltd',
                  'yelowsoft',
                  'inunison-b628',
                  'blockace-daf1',
                  'tag-world-exchange',
                  'joom-0ef8',
                  'ester-digital',
                  'cybertrust-c7d9',
                  'chatnels',
                  'beerhouse-dd6e',
                  'barobo',
                  'wishplz',
                  'twende-3864',
                  'meditap-llc',
                  'trend45',
                  'workzeit',
                  'aspire-australia',
                  'shots-no-chaser',
                  'resonian-inc',
                  'spondyr',
                  'blockchain-hanoi',
                  'basis-365-accounting',
                  'yourcabs',
                  'holroyds',
                  'alta-digital',
                  'rotaville',
                  'sofrep',
                  'marathon-studios',
                  'olive-branch',
                  'one-commute',
                  'musejam',
                  'mobileplay',
                  'turnkey-management-gmbh',
                  'spigot-labs',
                  'the-campus-companion',
                  'apptimi',
                  'f8-enterprises-holdings-group',
                  'terrapro-solutions',
                  'columbery',
                  'hq-network',
                  'askdigital',
                  'bluescheme',
                  'bracken-marketing',
                  'cookhub',
                  'emerge-energy-services',
                  'foodchain-f134',
                  'hellopickups',
                  'the-lcf-group',
                  'manner-e489',
                  'o-2-nails-india',
                  'harmari-by-ltas-technologies',
                  'twyns',
                  'meta-outdoor',
                  'bitcaribe',
                  'feels',
                  'sandhelden-gmbh-co-kg',
                  'flamebait-ab',
                  'paradiso-software',
                  'bourbon-and-boweties',
                  'ced-systems',
                  'appsinvo',
                  'bail-2-go',
                  'ttba-group',
                  'cloudvandana-solutions',
                  '8-ways-media-sa',
                  'healthy-matters',
                  'tinyrex-games',
                  'ejn',
                  'goroom',
                  'quandex-374e',
                  'us-fund-source',
                  'foyer-8229',
                  'bizboards-international-inc',
                  'vendium-ab',
                  'eat2save',
                  'bioextrax-ab',
                  'oviview',
                  'instream-adtech',
                  'stoebich',
                  'feedbackoutlook',
                  'ducovest',
                  'allerio',
                  'digicomm',
                  'bank-yogi',
                  'bikecleanse',
                  'cloudgenie-corp',
                  'kpis-pvt-ltd',
                  'nature-herbal-life',
                  'complete-structural-consulting',
                  'agribela',
                  'utility-avenue',
                  'epic-research-pte-ltd',
                  'q-market-makers',
                  'muhurtmaza',
                  'fuel-media-solutions-pvt-ltd',
]
        
            yield SeleniumRequest(
                url=f'https://www.crunchbase.com/organization/{urls[i]}/technology',
                wait_time=5,
                callback=self.parse
            )

    def parse(self, response):
        OrganizationName = response.xpath("//html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/profile-header/div/header/div/div/div/div[2]/div[1]/h1/text()").get()
        OrganizationNameURL = response.xpath("//html/head/link[5]/@href").get()
        TotalProductActive = response.xpath("//div[@class='section-content']/anchored-values/div[1]//a/div/field-formatter/span/text()").get()
        DownloadsLast30Days = response.xpath("//div[@class='section-content']/anchored-values/div[2]//a/div/field-formatter/span/text()").get()
        ActiveTechCount = response.xpath("//div[@class='section-content']/anchored-values/div[3]//a/div/field-formatter/span/text()").get()
        MonthlyVisits = response.xpath("//div[@class='section-content']/anchored-values/div[4]//a/div/field-formatter/span/text()").get()
        MonthlyVisitsGrowth = response.xpath("//div[@class='section-content']/anchored-values/div[5]//a/div/field-formatter/span/text()").get()
        MonthlyDownloadGrowth = response.xpath("(//div[@class='section-content'])[5]/tabs-card/mat-tab-group/div/mat-tab-body/div/profile-section/section-card/mat-card/div/div/big-values-card/div[2]/field-formatter/span/text()").get()
        GlobalTrafficRank = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/big-values-card/div[1]/field-formatter/span/text()").get()
        MonthlyRankGrowth = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/big-values-card/div[2]/field-formatter/span/text()").get()
        VisitDuration = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/fields-card/ul/li[1]/field-formatter/span/text()").get()
        VisitDurationGrowth = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/fields-card/ul/li[2]/field-formatter/span/text()").get()
        PageViews = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/fields-card/ul/li[3]/field-formatter/span/text()").get()
        PageViewsGrowth = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/fields-card/ul/li[4]/field-formatter/span/text()").get()
        BounceRate = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/fields-card/ul/li[5]/field-formatter/span/text()").get()
        BounceRateGrowth = response.xpath("(//div[@class='section-content'])[11]/tabs-card/mat-tab-group/div/mat-tab-body[2]/div/profile-section/section-card/mat-card/div/div/fields-card/ul/li[6]/field-formatter/span/text()").get()
        yield{
                'OrganizationName': OrganizationName,
                'OrganizationNameURL': OrganizationNameURL,
                'TotalProductActive':TotalProductActive,
                'DownloadsLast30Days':DownloadsLast30Days,
                'ActiveTechCount':ActiveTechCount,
                'MonthlyVisits':MonthlyVisits,
                'MonthlyVisitsGrowth':MonthlyVisitsGrowth,
                'MonthlyDownloadGrowth':MonthlyDownloadGrowth,
                'GlobalTrafficRank':GlobalTrafficRank,
                'MonthlyRankGrowth':MonthlyRankGrowth,
                'VisitDuration':VisitDuration,
                'VisitDurationGrowth':VisitDurationGrowth,
                'PageViews':PageViews,
                'PageViewsGrowth':PageViewsGrowth,
                'BounceRate':BounceRate,
                'BounceRateGrowth':BounceRateGrowth,
            }
        yield SeleniumRequest(
                url='https://www.crunchbase.com/organization/hopper/technology',
                wait_time=10,
                callback=self.start_requests
            )