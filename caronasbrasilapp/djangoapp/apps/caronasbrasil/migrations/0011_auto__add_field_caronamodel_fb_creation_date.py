# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CaronaModel.fb_creation_date'
        db.add_column(u'caronasbrasil_caronamodel', 'fb_creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 12, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CaronaModel.fb_creation_date'
        db.delete_column(u'caronasbrasil_caronamodel', 'fb_creation_date')


    models = {
        u'caronasbrasil.caronagroupmodel': {
            'Meta': {'object_name': 'CaronaGroupModel'},
            'city1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city1_list': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city1_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'city2': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city2_list': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city2_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fb_group_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'caronasbrasil.caronamodel': {
            'Meta': {'object_name': 'CaronaModel'},
            'destiny': ('django.db.models.fields.CharField', [], {'max_length': '33'}),
            'fb_content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'fb_creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'fb_group_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fb_post_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fb_user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'from_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_vagas': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ofereco_procuro': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '33'}),
            'to_datetime': ('django.db.models.fields.DateTimeField', [], {})
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