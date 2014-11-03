# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
from applications.dianping.models import Shop
import requests
import json

base_url = "http://www.dianping.com/ajax/json/shop/wizard/BasicHideInfoAjaxFP?"

headers = {
    "referer": "http://www.dianping.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        shops = Shop.objects.all()
        for shop in shops:
            try:
                self.parse_shop(shop)
            except Exception, err:
                print(err)
                continue

    def parse_shop(self, shop):
        if shop.info:
            return

        print("parse shop %s" % shop.name)
        url = "%sshopId=%s" % (base_url, shop.shop_id)
        content = requests.get(url).content
        json_data = json.loads(content)

        shop.phone = json_data['msg']['shopInfo']['phoneNo']
        shop.phone2 = json_data['msg']['shopInfo']['phoneNo2']
        shop.address = json_data['msg']['shopInfo']['address']
        shop.info = content
        shop.save()