# -*- coding:utf-8 -*-
import requests
import urlparse
import chardet
from datetime import datetime
import time

from util.header import get_header


class Downloader(object):
    def __init__(self, delay):
        self.throttle = Throttle(delay)

    def __call__(self, url):
        self.throttle.wait(url)

        print 'Downloading', url
        header = get_header()
        r = requests.get(url, headers=header)
        r.encoding = chardet.detect(r.content)['encoding']
        if r.status_code == 200:
            return r.text
        else:
            r.raise_for_status()


class Throttle(object):
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_time = self.delay \
                         - (datetime.now() - last_accessed).seconds
            if sleep_time > 0:
                time.sleep(sleep_time)
        self.domains[domain] = datetime.now()
