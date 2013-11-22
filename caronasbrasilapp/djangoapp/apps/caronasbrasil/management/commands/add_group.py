# coding: utf-8
__author__ = 'edubecks'
from djangoapp.apps.caronasbrasil.main_controller import MainController
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, CaronaModel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'manually add group'

    def handle(self, *args, **options):

        ## clean
        CaronaGroupModel.objects.all().delete()


        ## Test
        ## https://www.facebook.com/groups/641749869191341/
        # fb_group_id = '641749869191341'
        # city1 = 'sao paulo'
        # city1_state = 'SP'
        # city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        # city2 = 'sao carlos'
        # city2_state = 'SP'
        # city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']


        ## Caronas sao carlos
        ## https://www.facebook.com/groups/caronascsp/
        fb_group_id = '144978565569620'
        city1 = 'sao paulo'
        city1_state = 'SP'
        city2 = 'sao carlos'
        city2_state = 'SP'
        city1_list = [u'Sanpa', u'Sampa', ur'SP', ur'sao\s*paulo\s?(\(.*?\))?',
                           'sao paulo, sp, br', 'spaulo']
        city2_list = [u'Sanca', u'Samca', ur'Sao\s*Carlos', u'SC', 'sao carlos, sp, br',
                           'scarlos']

        ## saving model
        CaronaGroupModel.objects.create(
            fb_group_id=fb_group_id,
            city1=city1,
            city1_state=city1_state,
            city1_list=':'.join(city1_list),
            city2=city2,
            city2_state=city2_state,
            city2_list=':'.join(city2_list)
        )
        return

