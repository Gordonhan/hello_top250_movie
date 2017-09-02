# -*- coding:utf-8 -*-
import lxml.html
import csv


class ScrapingCallback(object):
    def __init__(self):
        self.writer = csv.writer(open('top250.csv', 'wb'))
        self.writer.writerow(['ranking', 'movie'])

    def __call__(self, html):
        tree = lxml.html.fromstring(html)

        lis = tree.xpath(".//div[@class='article']/ol[@class='grid_view']/li")
        for li in lis:
            ranking = li.xpath("./div[@class='item']/div[@class='pic']/em")[0].text_content()
            movie_name = li.xpath("./div[@class='item']/div[@class='info']//span[@class='title']")[0].text_content()
            self.writer.writerow([ranking.encode('utf-8'), movie_name.encode('utf-8')])

        link = tree.xpath(".//div[@class='article']/div[@class='paginator']/span[@class='next']/a")
        return link[0].get('href') if len(link) > 0 else None
