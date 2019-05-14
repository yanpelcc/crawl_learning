# -*- coding: utf-8 -*-
import scrapy
import bs4
from pyjobs.items import PyjobsItem


class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['https://www.liepin.com/']
    start_urls = [
        'https://www.liepin.com/zhaopin/?init=-1&headckid=6be958a6dd2c8bf4&fromSearchBtn=2&ckid=6be958a6dd2c8bf4&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=python&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=46667eaa46f490a84c0f7ca24358a6b4&d_curPage=1&d_pageSize=40&d_headId=46667eaa46f490a84c0f7ca24358a6b4&curPage=0']
    for i in range(1, 48):
        start_urls.append(
            'https://www.liepin.com/zhaopin/?init=-1&headckid=6be958a6dd2c8bf4&fromSearchBtn=2&ckid=6be958a6dd2c8bf4&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=python&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=46667eaa46f490a84c0f7ca24358a6b4&d_curPage=1&d_pageSize=40&d_headId=46667eaa46f490a84c0f7ca24358a6b4&curPage=%d' % i)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.body, 'lxml')
        job_list = soup.find_all('div', class_='job-info')
        for job in job_list:
            item = PyjobsItem()
            item['job'] = job.find('h3').get_text().strip()
            detail = job.find(class_='condition clearfix')
            item['salary'] = detail.find(class_='text-warning').get_text()
            item['area'] = detail.find(class_='area').get_text()
            item['edu'] = detail.find(class_='edu').get_text()
            try:
                item['exp'] = detail.find_all('span')[3].get_text()
            except IndexError:
                item['exp'] = detail.find_all('span')[2].get_text()
            yield item
