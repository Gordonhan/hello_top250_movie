# -*- coding:utf-8 -*-
from crawler.link_crawler import link_crawler
from crawler.scraping_callback import ScrapingCallback

if __name__ == '__main__':
    link_crawler(
        'https://movie.douban.com/top250',
        delay=3,
        callback=ScrapingCallback()
    )
