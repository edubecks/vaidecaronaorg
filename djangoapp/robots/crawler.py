# coding: utf-8
from fb_api_manager import FBAPIManager
from fbgroups.

__author__ = 'edubecks'

class Crawler(object):

    def __init__(self):

        return

    def retrieve_posts(self):

        group_id = '641749869191341'

        ## gettings feed
        fb_manager = FBAPIManager()
        feed = fb_manager.read_group_feed(group_id)

        ## persistence
        persistence = PersistenceController()

        for post in feed:

            ## check if exists






        return
