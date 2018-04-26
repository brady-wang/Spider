#coding=utf-8
import scrapy
import sqlite3

from ..items import  GanjiItem


class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    start_urls = ['http://yeves.cn/']


    def parse(self,response):
        print(response)
        ganji = GanjiItem()
        desc_list = response.xpath('//*[@id="article"]/div[@class="container"]/div/article/div/p[2]/text()').extract()
        title_list = response.xpath('//*[@id="article"]/div[@class="container"]/div/article/div/header/h2/a/text()').extract()
        for i,j in zip(title_list,desc_list):
             ganji['title'] = i
             ganji['desc'] = j
             yield ganji