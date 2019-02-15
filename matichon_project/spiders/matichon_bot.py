# -*- coding: utf-8 -*-
# Import libraries
import scrapy
from scrapy.http import Request

class MatichonBotSpider(scrapy.Spider):
    name = 'matichon_bot'
    allowed_domains = ['https://www.matichon.co.th/']
    max_id = 4000

    #### Pagination ####
    def start_requests(self):
        for i in range(1, self.max_id):
                yield Request('https://www.matichon.co.th/politics/page/{}/'.format(i),
                              callback=self.parse)
    #### Collect links and metadata ####
    def parse(self, response):
        url = response.css('div#td-outer-wrap div.td-main-content-wrap.td-container-wrap div div div.td-pb-span8.td-main-content div div div.item-details h3.entry-title.td-module-title a::attr(href)').extract()
        title =  response.css('div#td-outer-wrap div.td-main-content-wrap.td-container-wrap div div div.td-pb-span8.td-main-content div div div.item-details h3.entry-title.td-module-title a::attr(title)').extract()
        time = response.css('div#td-outer-wrap div.td-main-content-wrap.td-container-wrap div div div.td-pb-span8.td-main-content div div div.item-details div.td-module-meta-info span.td-post-date time::attr(datetime)').extract()
        for item in zip(url,title,time):
            yield Request(item[0], callback=self.parse_unitpage, dont_filter=True, meta={'url' : item[0], 'title' : item[1], 'time' : item[2]})  
            
    #### Scrape info on individual page and compile ####
    def parse_unitpage(self, response):        
        scraped_info = {
            'url' : response.meta['url'],
            'title' : response.meta['title'],
            'time' : response.meta['time'],
            'text' : "".join(response.css('.td-post-content p::text').extract())
        }
        yield scraped_info
