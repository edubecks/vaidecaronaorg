# coding: utf-8
import os
import facebook

__author__ = 'edubecks'

class FBGroupsController(object):

    def __init__(self, fb_group_id):
        self.fb_group_id = fb_group_id
        self.fb_token = None
        return

    def generate_token(self):
        ## todo
        self.fb_token = os.getenv('LONG_LIVED_OAUTH_TOKEN')
        return

    @property
    def facebook_graph(self):
        ## todo improve token
        if not self.fb_token:
            self.generate_token()
        return facebook.GraphAPI(self.fb_token)

    def get_posts(self):
        return self.facebook_graph.get_connections(self.fb_group_id, 'feed')['data']
