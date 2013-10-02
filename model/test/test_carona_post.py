# coding: utf-8
from caronasbrasil.carona_post import CaronaPost

__author__ = 'edubecks'

from pprint import pprint
from unittest import TestCase


class CaronaPostTestCase(TestCase):
    def setUp(self):
        self.posts_dict = [
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20 de outubro Por volta do 7:31hrs Saindo do metro consolação. 1 vaga'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7:31 hrs Saindo do metro consolação. 1 vaga'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - segunda 20 Por volta do 7:31 h Saindo do metro consolação. 1 vaga'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 2da feira Por volta do 7:31h Saindo do metro consolação. 1 vaga'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 2 feira Por volta do 7:31pm Saindo do metro consolação. 1 vaga'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 3ca feira Por volta do 7:31am Saindo do metro consolação. 1 vaga'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 4ta feira Por volta do 7h31 am Saindo do metro consolação. duas  vagas'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 5ta feira Por volta do 7:31 horas Saindo do metro consolação. três  vagas'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 6ta feira Por volta do 10 horas Saindo do metro consolação. quatro  vagas'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - sabado Por volta do 10pm Saindo do metro consolação. 2  vagas'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - domingo Por volta do 10 am Saindo do metro consolação. 2  vagas'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 10 p.m. Saindo do metro consolação. 2  vagas'''},
            {'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 10 pm. Saindo do metro consolação. 2  vagas'''},
            {'message': u'''Busco São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 15:10 hrs Saindo do metro consolação. 3   lugares'''},
            {'message': u'''procuro São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 am Saindo do metro consolação. Carro com 4   pessoas'''},
            {'message': u'''ofereco São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 pm Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''ofereco São Paulo -> São Carlos Sexta feira - 20/09 Por volta das 10 da manha Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''ofereco São Paulo -> São Carlos Sexta feira - 20/09 Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
        ]

        self.tags = [
            u'São Paulo -> São Carlos',
            u'São Paulo > São Carlos' ,
            u'São Paulo -> SC'        ,
            u'SP -> SC'               ,
            u'SP - SC'                ,
            u'SÃO CARLOS para SÃO PAULO',
            u'SÃO PAULO ==> SÃO CARLOS',
            u'SP >>> Sanca',
            u'Sampa --> Sanca',
            u'São Carlos - São Paulo',
            u'Sanca 》São Paulo',
            u'SP->SC',
        ]

        self.cities = [
            [u'Sanpa', u'Sampa',u'Sao Paulo', u'SP' ],
            [u'Sanca', u'Samca',u'Sao Carlos', u'SC' ]
        ]
        return

    def test_ofereco_procuro(self):
        for p in self.posts_dict:
            post = CaronaPost(p)
            self.assertTrue(post.retrieve_ofereco_procuro_tag(), "found ofereco/procuro tag")
            # pprint(post.content_clean)
            # pprint(post.tag_ofereco_procuro)
        return

    def test_vagas(self):
        for p in self.posts_dict:
            post = CaronaPost(p)
            # self.assertTrue(post.retrieve_vagas(), "found number of vagas tag")
            # pprint(post.content_clean)
            # pprint(post.tag_num_vagas)
        return

    def test_time(self):
        for p in self.posts_dict:
            post = CaronaPost(p)
            # pprint(post.content_clean)
            self.assertTrue(post.retrieve_time_tags(), "found time tag")
            # pprint(post.tag_time)
        return

    def test_origin_destiny(self):

        example_posts = [
            {'message': u'''São Paulo -> São Carlos',  go Por volta do 10 am Saindo do metro consolação. 2  vagas'''},
            {'message': u'''São Paulo > São Carlos' ,   Por volta do 10 p.m. Saindo do metro consolação. 2  vagas'''},
            {'message': u'''São Paulo -> SC'        ,   Por volta do 10 pm. Saindo do metro consolação. 2  vagas'''},
            {'message': u'''SP -> SC'               ,  or volta do 15:10 hrs Saindo do metro consolação. 3   lugares'''},
            {'message': u'''SP - SC'                ,   Por volta do 7 am Saindo do metro consolação. Carro com 4   pessoas'''},
            {'message': u'''SÃO CARLOS para SÃO PAULO', Por volta do 7 pm Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''SÃO PAULO ==> SÃO CARLOS',  Por volta das 10 da manha Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''SP >>> Sanca',              Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''Sampa --> Sanca',           Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''São Carlos - São Paulo',    Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''Sanca 》São Paulo',          Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
            {'message': u'''SP->SC',                    Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
        ]

        for p  in example_posts:
            post = CaronaPost(p)
            post.city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
            post.city2_list = [u'Sao Carlos',u'Sanca', u'Samca', u'SC']
            post.retrieve_origin_destiny()
        return