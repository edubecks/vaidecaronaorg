# coding: utf-8
import datetime
from djangoapp.apps.caronasbrasil.persistence_controller import PersistenceController

__author__ = 'edubecks'

from pprint import pprint
from djangoapp.apps.caronasbrasil.models import CaronaGroupModel, ParserErrorsModel, CaronaModel
from django.test import TestCase

class TestCase(TestCase):
    
    def setUp(self):
        fb_group_id = '641749869191341'
        city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
        city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']
        print ','.join(city1_list)
        print ','.join(city2_list)

        ## saving model
        CaronaGroupModel.objects.create(
            fb_group_id=fb_group_id,
            city1='sao paulo',
            city1_state='SP',
            city1_list=','.join(city1_list),
            city2='sao carlos',
            city2_state='SP',
            city2_list=','.join(city2_list)
        )
        
        
        
        caronas = [
        ['641749869191341_663694143663580','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-10-27 20:00:00','o',1],
        ['641749869191341_663694103663584','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-28 06:00:00','p',1],
        ['641749869191341_663694086996919','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-28 15:00:00','o',1],
        ['641749869191341_663694080330253','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-11-03 18:00:00','o',1],
        ['641749869191341_663694070330254','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-29 12:00:00','p',1],
        ['641749869191341_663694053663589','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-28 10:00:00','o',1],
        ['641749869191341_663694026996925','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-10-28 13:00:00','o',1],
        ['641749869191341_663693993663595','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-27 21:00:00','o',1],
        ['641749869191341_663667053666289','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-28 18:00:00','p',1],
        ['641749869191341_663667020332959','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-11-01 15:00:00','p',1],
        ['641749869191341_663666973666297','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-29 18:00:00','p',1],
        ['641749869191341_663666950332966','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-29 09:00:00','o',1],
        ['641749869191341_663666923666302','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-28 19:00:00','o',2],
        ['641749869191341_663666900332971','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-10-28 14:00:00','p',2],
        ['641749869191341_663666870332974','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-28 08:00:00','o',1],
        ['641749869191341_659260847440243','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-20 20:00:00','p',1],
        ['641749869191341_659260817440246','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-15 06:00:00','p',1],
        ['641749869191341_659260787440249','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-10-15 15:30:00','o',1],
        ['641749869191341_659260767440251','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-15 08:00:00','o',1],
        ['641749869191341_656572881042373','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-10-15 22:00:00','p',1],
        ['641749869191341_656572837709044','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-15 10:30:00','o',1],
        ['641749869191341_656572817709046','641749869191341','Sao Carlos/SP','Sao Paulo/SP','2013-10-15 00:00:00','p',1],
        ['641749869191341_656572744375720','641749869191341','Sao Paulo/SP','Sao Carlos/SP','2013-10-15 18:00:00','p',1],
        ]

        for c in caronas:
            CaronaModel.objects.create(
                fb_post_id			    =c[0],
                fb_group_id 			=c[1],
                origin 			        =c[2],
                destiny 			    =c[3],
                date 			        = datetime.datetime.strptime(c[4], "%Y-%m-%d %H:%M:%S"),
                ofereco_procuro 		=c[5],
                num_vagas 			    =c[6],
            )
        return

    def test_caronas_path(self):
        persistence = PersistenceController()
        paths = persistence.get_carona_paths()
        pprint(paths)
        return

    def test_search(self):
        results = PersistenceController().search_carona('o', 'sao paulo','SP' ,'sao carlos', 'SP',
                                              datetime.datetime(2013, 10, 15, 8, 0, 0),
                                              datetime.datetime(2013, 10, 15, 12, 0, 0))
        pprint(results.values())
        return