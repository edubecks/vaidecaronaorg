# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CaronaModel.fb_content'
        db.add_column(u'caronasbrasil_caronamodel', 'fb_content',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)


        # Changing field 'CaronaModel.origin'
        db.alter_column(u'caronasbrasil_caronamodel', 'origin', self.gf('django.db.models.fields.CharField')(max_length=33))

        # Changing field 'CaronaModel.destiny'
        db.alter_column(u'caronasbrasil_caronamodel', 'destiny', self.gf('django.db.models.fields.CharField')(max_length=33))

    def backwards(self, orm):
        # Deleting field 'CaronaModel.fb_content'
        db.delete_column(u'caronasbrasil_caronamodel', 'fb_content')


        # Changing field 'CaronaModel.origin'
        db.alter_column(u'caronasbrasil_caronamodel', 'origin', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'CaronaModel.destiny'
        db.alter_column(u'caronasbrasil_caronamodel', 'destiny', self.gf('django.db.models.fields.CharField')(max_length=30))

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
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'destiny': ('django.db.models.fields.CharField', [], {'max_length': '33'}),
            'fb_content': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'fb_group_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fb_post_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_vagas': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ofereco_procuro': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '33'})
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