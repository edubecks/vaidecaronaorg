# coding: utf-8
__author__ = 'edubecks'

# coding: utf-8
from optparse import make_option

__author__ = 'edubecks'

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'clean older logs'

    # option_list = BaseCommand.option_list + (
    #     make_option('-r',
    #                 '--range_hours',
    #                 action='store',
    #                 dest='range_hours',
    #                 help='specify number of recent hours to crawl results in pending links'),
    # )

    def handle(self, *args, **options):
        ## execute robot
        return

