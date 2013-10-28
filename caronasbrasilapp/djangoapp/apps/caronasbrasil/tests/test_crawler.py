# coding: utf-8
# from unittest import TestCase
from django.test import TestCase
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, ParserErrorsModel
from djangoapp.apps.caronasbrasil.robots.crawler import Crawler

__author__ = 'edubecks'


class TestCrawler(TestCase):

    def setUp(self):
        fb_group_id = '641749869191341'
        city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']
        print ','.join(city1_list)
        print ','.join(city2_list)

        ## saving model
        CaronaGroupModel.objects.create(
            fb_group_id=fb_group_id,
            city1 = 'sao paulo',
            city1_state = 'SP',
            city1_list=','.join(city1_list),
            city2 = 'sao carlos',
            city2_state = 'SP',
            city2_list=','.join(city2_list)
        )

    def test_crawler(self):
        fb_group_id = '641749869191341'

        crawler = Crawler()
        crawler.retrieve_posts(fb_group_id)

        ## test log
        self.assertEquals(ParserErrorsModel.objects.all().count(), 2)
        return