# coding: utf-8
from djangoapp.apps.caronasbrasil.persistence_controller import PersistenceController

__author__ = 'edubecks'

from pprint import pprint
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, ParserErrorsModel
from django.test import TestCase

class TestCase(TestCase):
    
    def setUp(self):
        fb_group_id = '641749869191341'
        city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']
        print ','.join(city1_list)
        print ','.join(city2_list)

        ## saving model
        CaronaGroupModel.objects.create(
            fb_group_id=fb_group_id,
            city1='sao paulo',
            city1_state='SP',
            city1_list=','.join(city1_list),
            city2='sao carlos',
            city2_state='SP',
            city2_list=','.join(city2_list)
        )
        return

    def test_caronas_path(self):
        persistence = PersistenceController()
        paths = persistence.get_carona_paths()
        pprint(paths)
        return