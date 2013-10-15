# coding: utf-8
from caronasbrasil.models import CaronaGroupModel

__author__ = 'edubecks'

# coding: utf-8
from optparse import make_option

__author__ = 'edubecks'

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'manually add group'

    # option_list = BaseCommand.option_list + (
    #     make_option('-r',
    #                 '--range_hours',
    #                 action='store',
    #                 dest='range_hours',
    #                 help='specify number of recent hours to crawl results in pending links'),
    # )

    def handle(self, *args, **options):
        fb_group_id = '641749869191341'
        city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']

        ## saving model
        CaronaGroupModel(
            fb_group_id = fb_group_id,
            city1 = ','.join(city1_list),
            city2 = ','.join(city2_list)
        ).save()
        return

