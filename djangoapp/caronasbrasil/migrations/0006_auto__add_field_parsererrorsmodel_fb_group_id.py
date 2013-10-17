# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ParserErrorsModel.fb_group_id'
        db.add_column(u'caronasbrasil_parsererrorsmodel', 'fb_group_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ParserErrorsModel.fb_group_id'
        db.delete_column(u'caronasbrasil_parsererrorsmodel', 'fb_group_id')


    models = {
        u'caronasbrasil.caronagroupmodel': {
            'Meta': {'object_name': 'CaronaGroupModel'},
            'city1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fb_group_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'caronasbrasil.caronamodel': {
            'Meta': {'object_name': 'CaronaModel'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'destiny': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fb_group_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fb_post_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_vagas': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ofereco_procuro': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'caronasbrasil.parsererrorsmodel': {
            'Meta': {'object_name': 'ParserErrorsModel'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'fb_group_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fb_post_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['caronasbrasil']