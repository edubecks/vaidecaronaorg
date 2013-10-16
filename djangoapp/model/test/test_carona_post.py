# coding: utf-8
import datetime
from model.caronasbrasil.carona_post import CaronaPost

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

        example_posts = [
            {'message': u'''Por volta do 10 am Saindo do metro consolação. 1  vaga'''},
            {'message': u'''r volta do 10 p.m. Saindo do metro consolação. uma  lugar'''},
            {'message': u'''r volta do 10 pm. Saindo do metro consolação. 1pessoa'''},
            {'message': u'''volta do 15:10 hrs Saindo do metro consolação. duas vagas'''},
            {'message': u'''r volta do 7 am Saindo do metro consolação. Carro com 2 pessoas'''},
            {'message': u'''r volta do 7 pm Saindo do metro consolação. Sobram 2 lugares'''},
            {'message': u'''r volta das 10 da manha Saindo do metro consolação.3 pessoas'''},
            {'message': u'''r volta das 3 da tarde Saindo do metro consolação. três lugares'''},
            {'message': u'''r volta das 3 da tarde Saindo do metro consolação. tres vagas'''},
            {'message': u'''r volta das 3 da tarde Saindo do metro consolação. quatro lugares'''},
            {'message': u'''r volta das 3 da tarde Saindo do metro consolação. 4 lugares'''},
            {'message': u'''r volta das 3 da tarde Saindo do metro consolação. 4vagas'''},
        ]


        for p in example_posts:
            post = CaronaPost(p)
            self.assertTrue(post.retrieve_vagas(), "found number of vagas tag")
            # pprint(post.content_clean)
            # pprint(post.tag_num_vagas)
        return

    def test_time(self):

        example_posts = [
            [{'message': u'''hoje (quinta-feira, 10/10), as 19hs.'''}, datetime.time(19, 0)],
            [{'message': u'''sp\nsabado, 12/10, as 15h\nbusco '''}, datetime.time(15, 0)],
            [{'message': u'''Por volta do 7:31hrs S. 1 vaga'''},        datetime.time(7,31)],
            [{'message': u'''a do 7:31 hrs Saindo da'''},               datetime.time(7,31)],
            [{'message': u''' volta do 7:31 h Saindvaga'''},            datetime.time(7,31)],
            [{'message': u'''volta do 7:31h Saindo ga'''},              datetime.time(7,31)],
            [{'message': u'''lta do 7:31pm Saindo da'''},               datetime.time(19,31)],
            [{'message': u'''volta do 7:31pm Saindoaga'''},             datetime.time(19,31)],
            [{'message': u'''volta do 7h31 pm Saindas  vagas'''},       datetime.time(19,31)],
            [{'message': u'''volta do 17:31 horas S. três  vagas'''},   datetime.time(17,31)],
            [{'message': u'''volta do 10 horas Sainuatro  vagas'''},    datetime.time(10,0)],
            [{'message': u'''ta do 10pm Saindo do m'''},                datetime.time(22,0)],
            [{'message': u'''lta do 10 am Saindo doas'''},              datetime.time(10,0)],
            [{'message': u'''a do 10 p.m. Saindo doas'''},              datetime.time(22,0)],
            [{'message': u'''a do 10:06 p.m. Saindomegas'''},           datetime.time(22,6)],
            [{'message': u'''a do 10:06p.m. Saindo egas'''},            datetime.time(22,6)],
            [{'message': u'''a do 10 pm. Saindo do s'''},               datetime.time(22,0)],
            [{'message': u''' do 15:10 hrs Saindo dugares'''},          datetime.time(15,10)],
            [{'message': u'''a do 7 am Saindo do me 4   pessoas'''},    datetime.time(7,0)],
            [{'message': u'''a do 7 pm Saindo do me lugares'''},        datetime.time(19,0)],
            [{'message': u'''a das 10 da manha Sainobram 2  lugares'''},datetime.time(10,0)],
            [{'message': u'''a das 3 da tarde Saindbram 2  lugares'''}, datetime.time(15,0)],
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            # pprint(post.content_clean)
            self.assertTrue(post.retrieve_time_tags(), 'found tag time')
            # pprint(post.tag_time)
            self.assertEqual(post.tag_time, p[1], 'correct time')
        return

    def test_origin_destiny(self):

        example_posts = [
            {'message': u'''São Paulo -> São Carlos',  go Por v 2  vagas'''},
            {'message': u'''São Paulo > São Carlos' ,   Por vol 2  vagas'''},
            {'message': u'''São Paulo -> SC'        ,   Por vol2  vagas'''},
            {'message': u'''SP -> SC'               ,  or volta 3   lugares'''},
            {'message': u'''SP - SC'                ,   Por volrro com 4   pessoas'''},
            {'message': u'''SÃO CARLOS para SÃO PAULO', Por volbram 2  lugares'''},
            {'message': u'''SÃO PAULO ==> SÃO CARLOS',  Por volação. Sobram 2  lugares'''},
            {'message': u'''SP >>> Sanca',              Por volção. Sobram 2  lugares'''},
            {'message': u'''Sampa --> Sanca',           Por volção. Sobram 2  lugares'''},
            {'message': u'''São Carlos - São Paulo',    Por volção. Sobram 2  lugares'''},
            {'message': u'''Sanca 》São Paulo',          Por volção. Sobram 2  lugares'''},
            {'message': u'''SP->SC',                    Por volção. Sobram 2  lugares'''},
        ]

        for p  in example_posts:
            post = CaronaPost(p)
            post.city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
            post.city2_list = [u'Sao Carlos',u'Sanca', u'Samca', u'SC']
            self.assertTrue(post.retrieve_origin_destiny(), 'found origin and destiny')
        return


    def test_date_tags(self):
        example_posts = [
            [{'message': u''' 10 de outubro'''},                          datetime.date(2013, 10, 10)],
            [{'message': u''' 15 outubro'''},                             datetime.date(2013, 10, 15)],
            [{'message': u''' 20/10'''},                                  datetime.date(2013, 10, 20)],
            [{'message': u'''Sexta, dia 04 outubro '''},                  datetime.date(2013, 10, 4)],
            [{'message': u'''04/Out (Sexta-feira)'''},                    datetime.date(2013, 10, 4)],
            [{'message': u'''QUINTA 03/10'''},                            datetime.date(2013, 10, 3)],
            [{'message': u'''sexta 04/10/2013'''},                        datetime.date(2013, 10, 4)],
            [{'message': u'''sexta feira(04/10)'''},                      datetime.date(2013, 10, 4)],
            [{'message': u'''sexta, dia 4, 12:00.'''},                    datetime.date(2013, 10, 4)],
            [{'message': u'''na sexta, 4'''},                             datetime.date(2013, 10, 4)],
            [{'message': u''' sexta, 04,'''},                             datetime.date(2013, 10, 4)],
            [{'message': u''' 6a feira'''},                             datetime.date(2013, 10, 4)],
            [{'message': u'''SEXTA FEIRA DIA 4'''},                       datetime.date(2013, 10, 4)],
            [{'message': u'''amanha'''},                                  datetime.date(2013, 10, 3)],
            [{'message': u'''sexta após às 18:00 ou sábado de manha'''},  datetime.date(2013, 10, 4)],
            [{'message': u'''sexta a noite ou sábado'''},                 datetime.date(2013, 10, 4)],
            [{'message': u'''sexta-feira, apos as 22h30 ou sabado o mais cedo possivel!'''},datetime.date(2013, 10, 4)],
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            post.creation_date = datetime.date(2013, 10, 2)
            self.assertTrue(post.retrieve_date_tags(), 'retrieve date tags')
            self.assertEquals(post.tag_date, p[1], 'retrieve correct tag date')
        return

    def test_entire_post(self):
        example_posts = [
            {
                'post': {
                    'message':('Minha amiga OFERECE carona SP -> SC.\n'
                      'Dia: 10/10 (Quinta Feira)\n'
                      'Hora: 11:30\n'
                      'Vagas: 2\n'
                      'Pega: Metro Barra Funda\n'
                      'Deixa: Em casa.\n'
                      'Preço: R$ 30,00\n'
                )},
                 'datetime':datetime.datetime(2013,10,10,11,30),
                 'vagas': 2,
                 'ofereco_procuro': 'oferecer',
                 'origin': 'sao paulo',
                 'destiny': 'sao carlos'
            },
            {
                'post': {
                    'message':"""Procuro carona! Quinta-Feira, dia 10/10.
São Paulo -> São Carlos
Depois do almoço !"""},
                 'datetime':datetime.datetime(2013,10,10,11,30),
                 'ofereco_procuro': 'procurar',
                 'origin': 'sao carlos',
                 'destiny': 'sao paulo'
            },
        ]

        cities = [
            [u'sao paulo',  u'Sanpa', u'Sampa', u'Sao Paulo', u'SP'],
            [u'sao carlos', u'Sanca', u'Samca', u'Sao Carlos', u'SC']
        ]

        for p in example_posts:
            post = CaronaPost(p['post'])
            ## settings cities
            post.city1_list = cities[0]
            post.city2_list = cities[1]
            ## datetime
            self.assertTrue(post.retrieve_time_tags(), 'retrieve time tags')
            self.assertTrue(post.retrieve_date_tags(), 'retrieve date tags')
            print post.tag_time, post.tag_date
            self.assertEquals(post.tag_datetime, p['datetime'], 'retrieve date tags')
            ## vagas
            self.assertTrue(post.retrieve_vagas(), 'retrieve vagas')
            print post.tag_num_vagas
            self.assertEquals(post.tag_num_vagas, p['vagas'], 'retrieve date tags')
            ## ofereco / procuro
            self.assertTrue(post.retrieve_ofereco_procuro_tag(), 'ofereco/procuro vagas')
            print post.tag_ofereco_procuro
            self.assertEquals(post.tag_ofereco_procuro, p['ofereco_procuro'], 'retrieve date tags')
            ## origin / destiny
            self.assertTrue(post.retrieve_origin_destiny(), 'origin/destiny vagas')
            print post.tag_origin, '-->', post.tag_destiny
            self.assertEquals(post.tag_origin, p['origin'], 'origin tags')
            self.assertEquals(post.tag_destiny, p['destiny'], 'destiny tags')



        return