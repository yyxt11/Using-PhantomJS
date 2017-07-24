# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from PhantomJS_Crawler.items import JOBItem
from selenium import webdriver

class NovelCrawler(Spider):
    name= 'JobSearch'
    allowed_domains = ['zhaopin']
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python%20%E7%88%AC%E8%99%AB&sm=0&p=1&source=0"
        ]



    def parse(self, response):
        pass