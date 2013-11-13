# coding: utf-8
from pprint import pprint
import datetime
from djangoapp.apps.caronasbrasil.model.fb_groups.fb_groups_controller import FBGroupsController
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, CaronaModel
from djangoapp.apps.caronasbrasil.robots.crawler import Crawler

__author__ = 'edubecks'

class MainController(object):

    def __init__(self):
        return

    def crawl_post(self, time_interval=10):
        ## run crawler every 10 minutes
        crawler = Crawler(time_interval)
        carona_groups = CaronaGroupModel.objects.all()
        # pprint(carona_groups.values())
        for carona_group in carona_groups:
            crawler.retrieve_posts(carona_group.fb_group_id)
        return

    def clean_deleted_posts(self):
        fb_groups_controller  = FBGroupsController(0)
        ## getting posts in the last 24h
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        caronas = CaronaModel.objects.filter(from_datetime__gte=yesterday)
        for c in caronas:
            if not fb_groups_controller.exists_post(c.fb_post_id):
                # print 'Deleting post', c.fb_post_id
                c.delete()
        return
    
    def search_carona(self, from_city, from_city_state, to_city, to_city_state, from_time, to_time):

        return