# coding: utf-8
from djangoapp.apps.caronasbrasil.main_controller import MainController
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, CaronaModel, ParserErrorsModel

__author__ = 'edubecks'

# coding: utf-8

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
        ## crawl
        CaronaModel.objects.all().delete()
        ParserErrorsModel.objects.all().delete()
        MainController().crawl_post(time_interval=60)
        return

