# coding: utf-8
from djangoapp.apps.caronasbrasil.model.fb_groups.fb_groups_controller import FBGroupsController

__author__ = 'edubecks'

from pprint import pprint
from unittest import TestCase

class FBGroupsControllerTestCase(TestCase):

    def setUp(self):
        return

    def test_get_posts(self):
        ## test
        ## caronas sao carlos sao paulo
        group_id = '641749869191341'

        fbgroups_controller = FBGroupsController(group_id)
        posts  = fbgroups_controller.get_posts()
        pprint(posts)
        return

    def test_get_posts_with_pagination(self):
        group_id = '641749869191341'
        fbgroups_controller = FBGroupsController(group_id)

        ## last 24 hours
        posts = fbgroups_controller.get_posts(last_time_checked=1440)
        pprint(posts)

        ## all time posts
        print('\n\n\n\n\n\n-------------------------------------------------------------')
        posts = fbgroups_controller.get_posts(last_time_checked=10080)
        pprint(posts)
        return

    def test_get_comments(self):
        group_id = '641749869191341'
        fbgroups_controller = FBGroupsController(group_id)
        comments = fbgroups_controller.get_comments('641749869191341_666135846752743')
        pprint(comments)

        return

    def test_exists_post(self):
        fb_group_id = '144978565569620'
        fb_post_id = '144978565569620_602785809788891'
        fbgroups_controller = FBGroupsController(fb_group_id)
        comments = fbgroups_controller.exists_post(fb_post_id)
        return