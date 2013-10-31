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
            ['641749869191341_663694103663584','641749869191341','sao paulo/SP','sao carlos/SP','p',1,'PROCURO São Paulo -> São Carlos Amanhã (segunda), 28 de outubro. De manhã (até às 8 da manha).','2013-10-28 06:00:00','2013-10-28 08:00:00'],
            ['641749869191341_663666870332974','641749869191341','sao paulo/SP','sao carlos/SP','o',1,'OFEREÇO Osasco/São Paulo --> Sanca segunda-feira de manhã (horário a combinar - posso a partir das 10h30) Pego na Ponte do Piqueri, estação de trem Lapa ou Osasco Contato por inbox ou 11 97575 5098','2013-10-28 08:30:00','2013-10-28 23:59:00'],
            ['641749869191341_664807603552234','641749869191341','sao paulo/SP','sao carlos/SP','o',1,'Ofereço carona SP - SANCA, segunda(28/10), às 10h saindo da Barra Funda. 169 8838 5971(oi).','2013-10-28 10:00:00','2013-10-28 11:00:00'],
            ['641749869191341_663694026996925','641749869191341','sao carlos/SP','sao paulo/SP','o',1,'Ofereço carona de São Carlos PARA São Paulo amanhã, segunda-feira às 13h. Pego na rodoviária e em SP deixo no metrô Ana Rosa. R$ 30,00 Tratar pelo cel 011 991290479','2013-10-28 13:00:00','2013-10-28 14:00:00'],
            ['641749869191341_663666900332971','641749869191341','sao carlos/SP','sao paulo/SP','p',2,'Procuro Carona Sanca-> Sampa dia 28/10 por volta das 14 Preciso de 2 vagas. Obrigada','2013-10-28 14:00:00','2013-10-28 15:00:00'],
            ['641749869191341_663694086996919','641749869191341','sao paulo/SP','sao carlos/SP','o',1,'Ofereço carona Sampa --> Sanca, segunda-feira (28/10) ás 15 hrs. Pego na rodoviária tiete. Contato inbox ou sms (11) 98723-2189. Vlw!!','2013-10-28 15:00:00','2013-10-28 16:00:00'],
            ['641749869191341_663667053666289','641749869191341','sao paulo/SP','sao carlos/SP','p',1,'Procuro São Paulo --> São Carlos 28/10 a noite!','2013-10-28 18:00:00','2013-10-28 23:59:00'],
            ['641749869191341_663666923666302','641749869191341','sao paulo/SP','sao carlos/SP','o',2,'Ofereço carona SP ---SC segunda 28/10 as 19, saindo da barra funda. em sao carlos eu deixo em casa. 2 vagas 30 conto. 11 960761033','2013-10-28 19:00:00','2013-10-28 20:00:00']
        ]

        for c in caronas:
            CaronaModel.objects.create(
                fb_post_id			    =c[0],
                fb_group_id 			=c[1],
                origin 			        =c[2],
                destiny 			    =c[3],
                ofereco_procuro 		=c[4],
                num_vagas 			    =c[5],
                fb_content 			    =c[6],
                from_datetime 			= datetime.datetime.strptime(c[7], '%Y-%m-%d %H:%M:%S'),
                to_datetime 			= datetime.datetime.strptime(c[8], '%Y-%m-%d %H:%M:%S'),
            )
        return

    def test_caronas_path(self):
        persistence = PersistenceController()
        paths = persistence.get_carona_paths()
        pprint(paths)
        return

    def test_search(self):

        results = PersistenceController().search_carona('o', 'sao paulo','SP' ,'sao carlos', 'SP',
                                              datetime.datetime(2013, 10, 28, 11, 0, 0),
                                              datetime.datetime(2013, 10, 28, 11, 30, 0))
        pprint(results.values())
        results = PersistenceController().search_carona('o', 'sao paulo','SP' ,'sao carlos', 'SP',
                                              datetime.datetime(2013, 10, 28, 9, 0, 0),
                                              datetime.datetime(2013, 10, 28, 13, 0, 0))
        pprint(results.values())
        results = PersistenceController().search_carona('o', 'sao paulo','SP' ,'sao carlos', 'SP',
                                              datetime.datetime(2013, 10, 28, 8, 0, 0),
                                              datetime.datetime(2013, 10, 28, 11, 0, 0))
        pprint(results.values())
        results = PersistenceController().search_carona('o', 'sao paulo','SP' ,'sao carlos', 'SP',
                                              datetime.datetime(2013, 10, 28, 11, 0, 0),
                                              datetime.datetime(2013, 10, 28, 16, 0, 0))
        pprint(results.values())
        return