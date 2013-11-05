# coding: utf-8
import datetime
import time
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

    def get_posts(self, last_time_checked=0):
        if not last_time_checked:
            return self.facebook_graph.get_connections(self.fb_group_id, 'feed')['data']
        else:
            last_time_checked = datetime.timedelta(minutes=last_time_checked)
            since = int(time.mktime((datetime.datetime.now() - last_time_checked).timetuple()))
            return self.facebook_graph.get_connections(self.fb_group_id, 'feed', since=since)['data']

    def get_comments(self, fb_post_id):
        return  self.facebook_graph.get_connections(fb_post_id, 'comments')['data']