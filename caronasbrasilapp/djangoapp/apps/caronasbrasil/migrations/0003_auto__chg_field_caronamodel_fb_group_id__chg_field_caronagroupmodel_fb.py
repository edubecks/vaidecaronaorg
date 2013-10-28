# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CaronaModel.fb_group_id'
        db.alter_column(u'caronasbrasil_caronamodel', 'fb_group_id', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'CaronaGroupModel.fb_group_id'
        db.alter_column(u'caronasbrasil_caronagroupmodel', 'fb_group_id', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'CaronaModel.fb_group_id'
        db.alter_column(u'caronasbrasil_caronamodel', 'fb_group_id', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'CaronaGroupModel.fb_group_id'
        db.alter_column(u'caronasbrasil_caronagroupmodel', 'fb_group_id', self.gf('django.db.models.fields.CharField')(max_length=30))

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
            'fb_post_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_vagas': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ofereco_procuro': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['caronasbrasil']