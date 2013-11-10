# coding: utf-8
from pprint import pprint
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel
from djangoapp.apps.caronasbrasil.robots.crawler import Crawler

__author__ = 'edubecks'

class MainController(object):

    def __init__(self):

        return

    def crawl_post(self):
        ## run crawler every 10 minutes
        crawler = Crawler(time_interval=10)
        carona_groups = CaronaGroupModel.objects.all()
        pprint(carona_groups.values())
        for carona_group in carona_groups:
            crawler.retrieve_posts(carona_group.fb_group_id)
        return
    
    def search_carona(self, from_city, from_city_state, to_city, to_city_state, from_time, to_time):

        return