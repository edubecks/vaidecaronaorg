# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CaronaModel'
        db.create_table(u'caronasbrasil_caronamodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fb_post_id', self.gf('django.db.models.fields.IntegerField')()),
            ('fb_group_id', self.gf('django.db.models.fields.IntegerField')()),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('destiny', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ofereco_procuro', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('num_vagas', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'caronasbrasil', ['CaronaModel'])

        # Adding model 'CaronaGroupModel'
        db.create_table(u'caronasbrasil_caronagroupmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fb_group_id', self.gf('django.db.models.fields.IntegerField')()),
            ('city1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city2', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'caronasbrasil', ['CaronaGroupModel'])


    def backwards(self, orm):
        # Deleting model 'CaronaModel'
        db.delete_table(u'caronasbrasil_caronamodel')

        # Deleting model 'CaronaGroupModel'
        db.delete_table(u'caronasbrasil_caronagroupmodel')


    models = {
        u'caronasbrasil.caronagroupmodel': {
            'Meta': {'object_name': 'CaronaGroupModel'},
            'city1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fb_group_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'caronasbrasil.caronamodel': {
            'Meta': {'object_name': 'CaronaModel'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'destiny': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fb_group_id': ('django.db.models.fields.IntegerField', [], {}),
            'fb_post_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_vagas': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ofereco_procuro': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['caronasbrasil']