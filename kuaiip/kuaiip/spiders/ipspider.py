# -*- coding: utf-8 -*-
import scrapy
from kuaiip.items import KuaiipItem


class IpspiderSpider(scrapy.Spider):
    name = 'ipspider'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/inha/']
    for i in range(2, 100):
        url = 'http://www.kuaidaili.com/free/inha/' + str(i)
        start_urls.append(url)

    def parse(self, response):
        addr_urls = response.xpath('//*[@id="list"]/table/tbody')
        for addr in addr_urls:
            item = KuaiipItem()
            item['ip'] = addr.xpath('//td[1]/text()').extract()
            item['port'] = addr.xpath('//td[2]/text()').extract()
            item['ty'] = addr.xpath('//td[4]/text()').extract()
            item['location'] = addr.xpath('//td[5]/text()').extract()
            item['speed'] = addr.xpath('//td[6]/text()').extract()
            yield item
