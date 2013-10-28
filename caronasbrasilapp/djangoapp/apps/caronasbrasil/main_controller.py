# coding: utf-8
from pprint import pprint
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel
from djangoapp.apps.caronasbrasil.robots.crawler import Crawler

__author__ = 'edubecks'

class MainController(object):

    def __init__(self):

        return

    def crawl_post(self):
        crawler = Crawler()
        carona_groups = CaronaGroupModel.objects.all()
        pprint(carona_groups)
        for carona_group in carona_groups:
            print('crawling '+carona_group.fb_group_id)
            crawler.retrieve_posts(carona_group.fb_group_id)

        return