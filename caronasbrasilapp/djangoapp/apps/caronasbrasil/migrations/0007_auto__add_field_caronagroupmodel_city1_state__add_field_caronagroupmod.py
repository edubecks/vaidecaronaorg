# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CaronaGroupModel.city1_state'
        db.add_column(u'caronasbrasil_caronagroupmodel', 'city1_state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2),
                      keep_default=False)

        # Adding field 'CaronaGroupModel.city1_list'
        db.add_column(u'caronasbrasil_caronagroupmodel', 'city1_list',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=200),
                      keep_default=False)

        # Adding field 'CaronaGroupModel.city2_state'
        db.add_column(u'caronasbrasil_caronagroupmodel', 'city2_state',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=2),
                      keep_default=False)

        # Adding field 'CaronaGroupModel.city2_list'
        db.add_column(u'caronasbrasil_caronagroupmodel', 'city2_list',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=200),
                      keep_default=False)


        # Changing field 'CaronaGroupModel.city2'
        db.alter_column(u'caronasbrasil_caronagroupmodel', 'city2', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'CaronaGroupModel.city1'
        db.alter_column(u'caronasbrasil_caronagroupmodel', 'city1', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):
        # Deleting field 'CaronaGroupModel.city1_state'
        db.delete_column(u'caronasbrasil_caronagroupmodel', 'city1_state')

        # Deleting field 'CaronaGroupModel.city1_list'
        db.delete_column(u'caronasbrasil_caronagroupmodel', 'city1_list')

        # Deleting field 'CaronaGroupModel.city2_state'
        db.delete_column(u'caronasbrasil_caronagroupmodel', 'city2_state')

        # Deleting field 'CaronaGroupModel.city2_list'
        db.delete_column(u'caronasbrasil_caronagroupmodel', 'city2_list')


        # Changing field 'CaronaGroupModel.city2'
        db.alter_column(u'caronasbrasil_caronagroupmodel', 'city2', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'CaronaGroupModel.city1'
        db.alter_column(u'caronasbrasil_caronagroupmodel', 'city1', self.gf('django.db.models.fields.CharField')(max_length=200))

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