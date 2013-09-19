# coding: utf-8
from admin import Admin
from datetime_post import DateTimePost
from fb_api_manager import FBAPIManager
from post import Post
from reader import Reader

__author__ = 'edubecks'


from pprint import pprint
from unittest import TestCase

class ControllerTestCase(TestCase):

    def setUp(self):
        self.posts_dict = [
            {'message': u'''Ofereço carona São Carlos - SP
Saio sexta feira, dia 20/09, as 19 horas. Deixo no Metro Ana Rosa e cobro 30 reais. Interessados favor entrar em contato INBOX.'''}
        ]
        return

    def test_controller(self):

        fb_api_manager = FBAPIManager()
        feed = fb_api_manager.read_group_feed('123134')

        reader = Reader(feed)
        admin = Admin('1')
        print(admin.tags)

        post = DateTimePost(self.posts_dict[0])
        post.set_admin_tags(admin.tags)
        print(post.tags)

        post.retrieve_time_tags()
        print(post.tag_time)

        post.retrieve_date_tags()
        print(post.tag_date)
        return