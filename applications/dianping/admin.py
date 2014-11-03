# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from applications.dianping.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_id', 'name', 'phone', 'phone2', 'address']


admin.site.register(Shop, ShopAdmin)