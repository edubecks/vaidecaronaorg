# coding: utf-8
from django.test import TestCase
from caronasbrasil.main_controller import MainController
from caronasbrasil.models import CaronaGroupModel

__author__ = 'edubecks'


class TestMainController(TestCase):



    def setUp(self):
        fb_group_id = '641749869191341'
        city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']

        ## saving model
        CaronaGroupModel(
            fb_group_id=fb_group_id,
            city1=','.join(city1_list),
            city2=','.join(city2_list)
        ).save()

    def test_crawl_post(self):
        MainController().crawl_post()
        MainController().crawl_post()

