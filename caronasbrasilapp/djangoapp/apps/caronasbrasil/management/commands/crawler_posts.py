# coding: utf-8
__author__ = 'edubecks'
from djangoapp.apps.caronasbrasil.main_controller import MainController
from optparse import make_option
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    # option_list = BaseCommand.option_list + (
    #     make_option('-r',
    #                 '--range_hours',
    #                 action='store',
    #                 dest='range_hours',
    #                 help='specify number of recent hours to crawl results in pending links'),
    # )

    def handle(self, *args, **options):
        ## execute robot
        MainController().crawl_post()
        return

