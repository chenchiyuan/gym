# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
from applications.dianping.models import Shop
import requests

base_url = "http://www.dianping.com/search/category/2/45/g147"

headers = {
    "referer": "http://www.dianping.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = self.gen_pages()
        for url in urls:
            self.parse_url(url)

    def gen_pages(self):
        pages = range(1, 51)
        urls = []
        for page in pages:
            urls.append("%sp%d" % (base_url, page))
        return urls

    def parse_url(self, url):
        content = requests.get(url, headers=headers).content
        soup = BeautifulSoup(content)
        tag_as = soup.find_all(class_="shopname")
        for tag_a in tag_as:
            href = tag_a.attrs.get("href", "")
            shop_id = href.replace("/shop/", "")
            name = tag_a.attrs.get("title", "")

            if Shop.objects.filter(shop_id=shop_id).exists():
                continue

            print(shop_id)
            print(name)
            Shop(shop_id=shop_id, name=name).save()