# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models


class Shop(models.Model):
    class Meta:
        app_label = "dianping"
        db_table = "dianping_course"
        verbose_name_plural = verbose_name = u"健身会所"


    shop_id = models.CharField(u"点评网id", max_length=128, default="", blank=True, null=True)
    name = models.CharField(u"店铺名称", max_length=128, default="")
    address = models.CharField(u"店铺地址", max_length=128, default="", blank=True, null=True)

    phone = models.CharField(u"手机号1", max_length=32, default="", blank=True, null=True)
    phone2 = models.CharField(u"手机号2", max_length=32, default="", blank=True, null=True)

    info = models.TextField(u"额外信息", max_length=16384, default="", blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)