# coding: utf-8
from fb_groups.fb_groups_controller import FBGroupsController

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