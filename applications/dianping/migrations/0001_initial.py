# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shop'
        db.create_table(u'dianping_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop_id', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('address', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, null=True, blank=True)),
            ('phone2', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(default=u'', max_length=16384, null=True, blank=True)),
        ))
        db.send_create_signal(u'dianping', ['Shop'])


    def backwards(self, orm):
        # Deleting model 'Shop'
        db.delete_table(u'dianping_course')


    models = {
        u'dianping.shop': {
            'Meta': {'object_name': 'Shop', 'db_table': "u'dianping_course'"},
            'address': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "u''", 'max_length': '16384', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'shop_id': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dianping']