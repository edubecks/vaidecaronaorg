# coding: utf-8
__author__ = 'edubecks'
from djangoapp.apps.caronasbrasil.main_controller import MainController
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, CaronaModel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'manually add group'

    def handle(self, *args, **options):

        ## Test
        ## https://www.facebook.com/groups/641749869191341/
        fb_group_id = '641749869191341'
        city1 = 'sao paulo'
        city1_state = 'SP'
        city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        city2 = 'sao carlos'
        city2_state = 'SS'
        city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']

        ## saving model
        CaronaGroupModel.objects.create(
            fb_group_id=fb_group_id,
            city1=city1,
            city1_state=city1_state,
            city1_list=','.join(city1_list),
            city2=city2,
            city2_state=city2_state,
            city2_list=','.join(city2_list)
        )
        return

