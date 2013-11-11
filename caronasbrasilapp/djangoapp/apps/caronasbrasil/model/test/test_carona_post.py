# coding: utf-8
import datetime
from pprint import pprint
from djangoapp.apps.caronasbrasil.model.caronasbrasil.carona_post import CaronaPost

__author__ = 'edubecks'

from unittest import TestCase


class CaronaPostTestCase(TestCase):
    def setUp(self):
        self.posts_dict = [
            {
            'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20 de outubro Por volta do 7:31hrs Saindo do metro consolação. 1 vaga'''},
            {
            'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7:31 hrs Saindo do metro consolação. 1 vaga'''},
            {
            'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - segunda 20 Por volta do 7:31 h Saindo do metro consolação. 1 vaga'''},
            {
            'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 2da feira Por volta do 7:31h Saindo do metro consolação. 1 vaga'''},
            {
            'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 2 feira Por volta do 7:31pm Saindo do metro consolação. 1 vaga'''},
            {
            'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 3ca feira Por volta do 7:31am Saindo do metro consolação. 1 vaga'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 4ta feira Por volta do 7h31 am Saindo do metro consolação. duas  vagas'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 5ta feira Por volta do 7:31 horas Saindo do metro consolação. três  vagas'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 6ta feira Por volta do 10 horas Saindo do metro consolação. quatro  vagas'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - sabado Por volta do 10pm Saindo do metro consolação. 2  vagas'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - domingo Por volta do 10 am Saindo do metro consolação. 2  vagas'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 10 p.m. Saindo do metro consolação. 2  vagas'''},
            {
            'message': u'''Procuro São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 10 pm. Saindo do metro consolação. 2  vagas'''},
            {
            'message': u'''Busco São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 15:10 hrs Saindo do metro consolação. 3   lugares'''},
            {
            'message': u'''procuro São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 am Saindo do metro consolação. Carro com 4   pessoas'''},
            {
            'message': u'''ofereco São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 pm Saindo do metro consolação. Sobram 2  lugares'''},
            {
            'message': u'''ofereco São Paulo -> São Carlos Sexta feira - 20/09 Por volta das 10 da manha Saindo do metro consolação. Sobram 2  lugares'''},
            {
            'message': u'''ofereco São Paulo -> São Carlos Sexta feira - 20/09 Por volta das 3 da tarde Saindo do metro consolação. Sobram 2  lugares'''},
        ]

        self.tags = [
            u'São Paulo -> São Carlos',
            u'São Paulo > São Carlos',
            u'São Paulo -> SC',
            u'SP -> SC',
            u'SP - SC',
            u'SÃO CARLOS para SÃO PAULO',
            u'SÃO PAULO ==> SÃO CARLOS',
            u'SP >>> Sanca',
            u'Sampa --> Sanca',
            u'São Carlos - São Paulo',
            u'Sanca 》São Paulo',
            u'SP->SC',
        ]

        self.cities = [
            [u'Sanpa', u'Sampa', u'Sao Paulo', u'SP'],
            [u'Sanca', u'Samca', u'Sao Carlos', u'SC']
        ]
        return

    def test_ofereco_procuro(self):

        example_posts = [
            [{
             'message': u''' alguma alma caridosa que mora aqui em sp vai pra la nesse dia e pode me dar uma carona'''},
             'procurar'],
            [{'message': u''' Ofereço São Paulo -> São Carlos Se'''}, 'oferecer'],
            [{'message': u''' Busco São Paulo -> São Carlo'''}, 'procurar'],
            [{'message': u''' Procuro São Paulo -> São Carlos Sex'''}, 'procurar'],
            [{'message': u''' alguem indo de sao carlos para sao paulo na quarta feira? --> procurar'''},
             'procurar'],
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            self.assertTrue(post.retrieve_ofereco_procuro_tag(), "not found ofereco/procuro tag")
            # pprint(post.content_clean)
            # pprint(post.tag_ofereco_procuro)
            self.assertEquals(post.tag_ofereco_procuro, p[1], 'retrieve correct tag date')
        return

    def test_vagas(self):

        example_posts = [
            [{
             'message': u'''ofereco carona sp ---sc segunda 28/10 as 19, saindo da barra funda. em sao carlos eu deixo em casa. 2 vagas 30 conto. 11 960761033'''},
             2],
            [{'message': u'''Por volta do 10 am Saindo do metro consolação. 1  vaga'''}, 1],
            [{'message': u'''r volta do 10 p.m. Saindo do metro consolação. uma  lugar'''}, 1],
            [{'message': u'''r volta do 10 pm. Saindo do metro consolação. 1pessoa'''}, 1],
            [{'message': u'''volta do 15:10 hrs Saindo do metro consolação. duas vagas'''}, 2],
            [{'message': u'''r volta do 7 am Saindo do metro consolação. Carro com 2 pessoas'''}, 2],
            [{'message': u'''r volta do 7 pm Saindo do metro consolação. Sobram 2 lugares'''}, 2],
            [{'message': u'''r volta das 10 da manha Saindo do metro consolação.3 pessoas'''}, 3],
            [{'message': u'''r volta das 3 da tarde Saindo do metro consolação. três lugares'''}, 3],
            [{'message': u'''r volta das 3 da tarde Saindo do metro consolação. tres vagas'''}, 3],
            [{'message': u'''r volta das 3 da tarde Saindo do metro consolação. quatro lugares'''}, 4],
            [{'message': u'''r volta das 3 da tarde Saindo do metro consolação. 4 lugares'''}, 4],
            [{'message': u'''r volta das 3 da tarde Saindo do metro consolação. 4vagas'''}, 4]
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            self.assertTrue(post.retrieve_vagas(), 'found number of vagas tag')
            pprint(post.content_clean)
            pprint(str(p[1]) + ' vs ' + str(post.tag_num_vagas))
            self.assertEqual(post.tag_num_vagas, p[1],
                             'correct number of vagas\n****' + post.content_clean)
        return

    def test_time(self):

        datetime_today = datetime.datetime.now()

        example_posts = [
            [
                {
                'message': u'''segunda-feira de manhã (horário a combinar - posso a partir das 8h30)'''},
                datetime.datetime.combine(datetime_today, datetime.time(8, 30)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 59))
            ],
            [
                {'message': u'''pela manha'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(12, 0))
            ],
            [
                {'message': u'''por volta das 18:30 19:00hrs'''},
                datetime.datetime.combine(datetime_today, datetime.time(18, 30)),
                datetime.datetime.combine(datetime_today, datetime.time(19, 30))
            ],
            [
                {'message': u'''por volta das 14 '''},
                datetime.datetime.combine(datetime_today, datetime.time(14, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(15, 0))
            ],
            [
                {'message': u'''sao carlos hoje, 27/10, as 21h. '''},
                datetime.datetime.combine(datetime_today, datetime.time(21, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(22, 0))
            ],
            [
                {'message': u'''ate as 8 da manha'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(8, 0))
            ],
            [
                {'message': u'''saindo as 20h.'''},
                datetime.datetime.combine(datetime_today, datetime.time(20, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(21, 0))
            ],
            [
                {'message': u'''de preferencia no periodo da manha.'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(12, 0))
            ],
            [
                {'message': u'''sanca segunda-feira de manha'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(12, 0))
            ],
            [
                {'message': u'''segunda 28/10 as 19,'''},
                datetime.datetime.combine(datetime_today, datetime.time(19, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(20, 0))
            ],
            [
                {'message': u'''hoje (quinta-feira, 10/10), as 19hs.'''},
                datetime.datetime.combine(datetime_today, datetime.time(19, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(20, 0))
            ],
            [
                {'message': u'''sp\nsabado, 12/10, as 15h\nbusco '''},
                datetime.datetime.combine(datetime_today, datetime.time(15, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(16, 0))
            ],
            [
                {'message': u'''Por volta do 7:31hrs S. 1 vaga'''},
                datetime.datetime.combine(datetime_today, datetime.time(7, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(8, 31))
            ],
            [
                {'message': u'''a do 7:31 hrs Saindo da'''},
                datetime.datetime.combine(datetime_today, datetime.time(7, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(8, 31))

            ],
            [
                {'message': u''' volta do 7:31 h Saindvaga'''},
                datetime.datetime.combine(datetime_today, datetime.time(7, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(8, 31))
            ],
            [
                {'message': u'''volta do 7:31h Saindo ga'''},
                datetime.datetime.combine(datetime_today, datetime.time(7, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(8, 31))
            ],
            [
                {'message': u'''lta do 7:31pm Saindo da'''},
                datetime.datetime.combine(datetime_today, datetime.time(19, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(20, 31))
            ],
            [
                {'message': u'''volta do 7:31pm Saindoaga'''},
                datetime.datetime.combine(datetime_today, datetime.time(19, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(20, 31))
            ],
            [
                {'message': u'''volta do 7h31 pm Saindas  vagas'''},
                datetime.datetime.combine(datetime_today, datetime.time(19, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(20, 31))
            ],
            [
                {'message': u'''volta do 17:31 horas S. três  vagas'''},
                datetime.datetime.combine(datetime_today, datetime.time(17, 31)),
                datetime.datetime.combine(datetime_today, datetime.time(18, 31))
            ],
            [
                {'message': u'''volta do 10 horas Sainuatro  vagas'''},
                datetime.datetime.combine(datetime_today, datetime.time(10, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(11, 0))
            ],
            [
                {'message': u'''ta do 10pm Saindo do m'''},
                datetime.datetime.combine(datetime_today, datetime.time(22, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 0))
            ],
            [
                {'message': u'''lta do 10 am Saindo doas'''},
                datetime.datetime.combine(datetime_today, datetime.time(10, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(11, 0))
            ],
            [
                {'message': u'''a do 10 p.m. Saindo doas'''},
                datetime.datetime.combine(datetime_today, datetime.time(22, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 0))
            ],
            [
                {'message': u'''a do 10:06 p.m. Saindomegas'''},
                datetime.datetime.combine(datetime_today, datetime.time(22, 6)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 6))
            ],
            [
                {'message': u'''a do 10:06p.m. Saindo egas'''},
                datetime.datetime.combine(datetime_today, datetime.time(22, 6)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 6))
            ],
            [
                {'message': u'''a do 10 pm. Saindo do s'''},
                datetime.datetime.combine(datetime_today, datetime.time(22, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 0))
            ],
            [
                {'message': u''' do 15:10 hrs Saindo dugares'''},
                datetime.datetime.combine(datetime_today, datetime.time(15, 10)),
                datetime.datetime.combine(datetime_today, datetime.time(16, 10))
            ],
            [
                {'message': u'''a do 7 am Saindo do me 4   pessoas'''},
                datetime.datetime.combine(datetime_today, datetime.time(7, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(8, 0))
            ],
            [
                {'message': u'''a do 7 pm Saindo do me lugares'''},
                datetime.datetime.combine(datetime_today, datetime.time(19, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(20, 0))
            ],
            [
                {'message': u'''a das 10 da manha Sainobram 2  lugares'''},
                datetime.datetime.combine(datetime_today, datetime.time(10, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(11, 0))
            ],
            [
                {'message': u'''a das 3 da tarde Saindbram 2  lugares'''},
                datetime.datetime.combine(datetime_today, datetime.time(15, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(16, 0))
            ],
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            ## just for testing
            post.tag_date = datetime_today
            pprint(post.content_clean)
            self.assertTrue(post.retrieve_time_tags(), 'found tag time')
            print(str(post.tag_time), 'vs', str(p[1]))
            self.assertEqual(post.tag_time, p[1], 'correct from datetime')
            print(str(post.tag_time_to), 'vs', str(p[2]))
            self.assertEqual(post.tag_time_to, p[2], 'correct to datetime')
        return

    def test_origin_destiny(self):

    
        example_posts = [
            {'message': u'''carona sao carlos / sao paulo''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''São Paulo -->> São Carlos',      go Por v 2  vagas''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''São Paulo -> São Carlos',       go Por v 2  vagas''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''São Paulo > São Carlos' ,        Por vol 2  vagas''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''São Paulo -> SC'        ,        Por vol2  vagas''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''SP -> SC'               ,       or volta 3   lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''SP - SC'                ,        Por volrro com 4   pessoas''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''SÃO CARLOS para SÃO PAULO',      Por volbram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''SÃO PAULO ==> SÃO CARLOS',       Por volação. Sobram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''SP >>> Sanca',                   Por volção. Sobram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''Sampa --> Sanca',                Por volção. Sobram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''São Carlos - São Paulo',         Por volção. Sobram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''Sanca 》São Paulo',               Por volção. Sobram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
            {'message': u'''SP->SC',                         Por volção. Sobram 2  lugares''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
        ]

        for p in example_posts:
            post = CaronaPost(p)
            post.city1 = 'sao paulo'
            post.city1_state = 'SP'
            post.city2 = 'sao carlos'
            post.city2_state = 'SP'
            post.city1_list = [u'Sao Paulo', u'Sanpa', u'Sampa', u'SP']
            post.city2_list = [u'Sao Carlos', u'Sanca', u'Samca', u'SC']
            self.assertTrue(post.retrieve_origin_destiny(), 'found origin and destiny')
            print(post.content_clean)
            print(post.tag_origin, ' --> ', post.tag_destiny)
        return


    def test_date_tags(self):
        example_posts = [
            [{'message': u''' sao paulo hoje, dia 27 ''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 27)],
            [{'message': u''' 4a feira''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 2)],
            [{'message': u''' terça-feira,''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 8)],
            [{'message': u''' quarta-feira,''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 2)],
            [{'message': u''' 10 de outubro''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 10)],
            [{'message': u''' 15 outubro''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 15)],
            [{'message': u''' 20/10''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 20)],
            [{'message': u'''Sexta, dia 04 outubro ''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''04/Out (Sexta-feira)''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''QUINTA 03/10''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 3)],
            [{'message': u'''sexta 04/10/2013''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''sexta feira(04/10)''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''sexta, dia 4, 12:00.''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''na sexta, 4''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u''' sexta, 04,''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u''' 6a feira''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''SEXTA FEIRA DIA 4''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''amanha''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 3)],
            [{'message': u'''sexta após às 18:00 ou sábado de manha''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''sexta a noite ou sábado''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}}, datetime.datetime(2013, 10, 4)],
            [{'message': u'''sexta-feira, apos as 22h30 ou sabado o mais cedo possivel!''', 'created_time': '2013-10-10T00:11:02+0000','from': {'id': '1'}},
             datetime.datetime(2013, 10, 4)],
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            post.creation_date = datetime.datetime(2013, 10, 2)
            self.assertTrue(post.retrieve_date_tags(), 'retrieve date tags')
            print(post.content_clean)
            print(post.tag_date)
            self.assertEquals(post.tag_date, p[1], 'retrieve correct tag date')
        return

    def test_entire_post(self):
        example_posts = [
            {
                'post': {
                    'message': ('Minha amiga OFERECE carona SP -> SC.\n'
                                'Dia: 10/10 (Quinta Feira)\n'
                                'Hora: 11:30\n'
                                'Vagas: 2\n'
                                'Pega: Metro Barra Funda\n'
                                'Deixa: Em casa.\n'
                                'Preço: R$ 30,00\n'
                    ),
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from':{
                        'id': '1'
                    }
                },
                'tag_time': datetime.datetime(2013, 10, 10, 11, 30),
                'tag_time_to': datetime.datetime(2013, 10, 10, 12, 30),
                'vagas': 2,
                'ofereco_procuro': 'oferecer',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
            {
                'post': {
                    'message': 'preciso de carona de sao carlos pra sao paulo  tel 98106 9357 tim valeu',
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 10, 10, 6, 0),
                'tag_time_to': datetime.datetime(2013, 10, 10, 23, 59),
                'ofereco_procuro': 'procurar',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': 'preciso de carona de sao carlos pra sao paulo  tel 98106 9357 tim valeu',
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 10, 10, 6, 0),
                'tag_time_to': datetime.datetime(2013, 10, 10, 23, 59),
                'ofereco_procuro': 'procurar',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': 'ofereco carona de sao paulo --->>>> sao carlos dia 08/11 (sexta feira) '
                               'saio as 16:00 horas , do metro trianom masp r$30,00 - com 3 no carro '
                               'contato face ou (16)9 9734-3553 - tim',
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 8, 16, 0),
                'tag_time_to': datetime.datetime(2013, 11, 8, 17, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
            {
                'post': {
                    'message': 'ofereco : sao paulo ----> sao carlos  domingo (10/11) as 16:00 no metro '
                               'vila madalena , linha verde . deixo em casa em sao carlos  4 pessoas '
                               'no carro  valor : 30 reais  tratar por inbox',
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 10, 16, 0),
                'tag_time_to': datetime.datetime(2013, 11, 10, 17, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
            {
                'post': {
                    'message': 'procuro sao carlos------->sao paulo  amanha 08/11 saindo entre '
                               '12h30 e 16h  2 vagas, contato inbox ou (11)963392565',
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 8, 12, 00),
                'tag_time_to': datetime.datetime(2013, 11, 8, 16, 0),
                'vagas': 2,
                'ofereco_procuro': 'procurar',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': 'ofereco sao carlos -> sao  paulo amanha (08/11) as 18h deixo na rodoviaria do tiete contato inbox',
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 8, 18, 00),
                'tag_time_to': datetime.datetime(2013, 11, 8, 19, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': 'ofereco carona sao carlos --------- sao paulo amanha as 10 da manha sexta dia 08  deixo no metro carrao',
                    'created_time': '2013-11-05T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 8, 10, 00),
                'tag_time_to': datetime.datetime(2013, 11, 8, 11, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': 'procuro sampa a sanca na quinta feira 14.11 a tarde duas vagas !!!!',
                    'created_time': '2013-11-05T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 14, 12, 00),
                'tag_time_to': datetime.datetime(2013, 11, 14, 18, 0),
                'ofereco_procuro': 'procurar',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
            {
                'post': {
                    'message': 'ofereco carona de sao paulo (tiete) para sao carlos. sexta dia 08/11 as 19hrs. tel. 17_9 91870878 vlw',
                    'created_time': '2013-11-05T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 8, 19, 00),
                'tag_time_to': datetime.datetime(2013, 11, 8, 20, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
            {
                'post': {
                    'message': 'procuro carona de: sao carlos, sp, br ate: sao paulo, sp, br dia '
                               '10/11/2013 (domingo). chegando pelas 13hs (1h a mais 1h a '
                               'menos seria botimo) em sampa. valeu. use https://caronas.co',
                    'created_time': '2013-11-05T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 10, 13, 00),
                'tag_time_to': datetime.datetime(2013, 11, 10, 14, 0),
                'ofereco_procuro': 'procurar',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': 'ofereco carona hoje sexta-feira as 14 horas!!!   '
                               'sao paulo pra sao carlos!!!   ponto de encontro paulista com a '
                               'rua frei caneca em frente ao banco itau  em sanca deixo em casa  '
                               'valor 30 reais!!!   016 99786 6449',
                    'created_time': '2013-11-08T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 8, 14, 00),
                'tag_time_to': datetime.datetime(2013, 11, 8, 15, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
            {
                'post': {
                    'message': 'so tenho mais 1 vaga carona sao carlos para sao paulo amanha '
                               'domingo 20:00h. saio rodoviaria sao carlos, ao lado da padaria da '
                               'esquina de frente para a saida dos onibus. deixo metro butanta resta '
                               '1 vaga. r$ 30,00. so que estou com acesso restrito ao fb. '
                               '(11) 98311-5595 (tim). (11) 9 9499-2776 claro e (11) 7741-6683 '
                               'abs mario erba',
                    'created_time': '2013-11-09T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }

                },
                'tag_time':    datetime.datetime(2013, 11, 10, 20, 00),
                'tag_time_to': datetime.datetime(2013, 11, 10, 21, 0),
                'ofereco_procuro': 'oferecer',
                'origin': 'sao carlos/SP',
                'destiny': 'sao paulo/SP'
            },
            {
                'post': {
                    'message': u"""Procuro carona! Quinta-Feira, dia 10/10.
São Paulo -> São Carlos
Depois do almoço !""",
                    'created_time': '2013-10-10T00:11:02+0000',
                    'from': {
                        'id': '1'
                    }
                },
                'datetime': datetime.datetime(2013, 10, 10, 12, 0),
                'tag_time': datetime.datetime(2013, 10, 10, 12, 0),
                'tag_time_to': datetime.datetime(2013, 10, 10, 18, 0),
                'ofereco_procuro': 'procurar',
                'origin': 'sao paulo/SP',
                'destiny': 'sao carlos/SP'
            },
        ]

        cities = [
            [u'sao paulo', u'Sanpa', u'Sampa', ur'Sao\s*Paulo', u'SP', ur'sao paulo\s?\(.*?\)', 'sao paulo, sp, br'],
            [u'sao carlos', u'Sanca', u'Samca', u'Sao\s*Carlos', u'SC', 'sao carlos, sp, br']
        ]

        for p in example_posts:
            post = CaronaPost(p['post'])
            ## settings cities
            post.city1_list = cities[0]
            post.city1 = cities[0][0]
            post.city1_state = 'SP'
            post.city2_state = 'SP'
            post.city2 = cities[1][0]
            post.city2_list = cities[1]
            ## datetime
            print post.content_clean
            self.assertTrue(post.retrieve_date_tags(), 'retrieve date tags')
            print post.tag_date
            self.assertTrue(post.retrieve_time_tags(), 'retrieve time tags ' + str(post.tag_time))
            print 'time', post.tag_time, p['tag_time']
            print 'time_to', post.tag_time_to, p['tag_time_to']
            self.assertEquals(post.tag_time, p['tag_time'], 'retrieve date tags')
            self.assertEquals(post.tag_time_to, p['tag_time_to'], 'retrieve date tags')
            ## vagas
            if 'vagas' in p:
                self.assertTrue(post.retrieve_vagas(), 'retrieve vagas')
                print post.tag_num_vagas
                self.assertEquals(post.tag_num_vagas, p['vagas'], 'retrieve date tags')
                ## ofereco / procuro
            self.assertTrue(post.retrieve_ofereco_procuro_tag(), 'ofereco/procuro')
            print post.tag_ofereco_procuro
            self.assertEquals(post.tag_ofereco_procuro, p['ofereco_procuro'], 'retrieve ofereco/procuro tags')
            ## origin / destiny
            self.assertTrue(post.retrieve_origin_destiny(), 'origin/destiny tags')
            print post.tag_origin, '-->', post.tag_destiny
            print post.tag_origin, p['origin']
            print post.tag_destiny, p['destiny']
            self.assertEquals(post.tag_origin, p['origin'], 'origin tags')
            self.assertEquals(post.tag_destiny, p['destiny'], 'destiny tags')

        return

    def test_intervals(self):
        datetime_today = datetime.datetime.now()
        example_posts = [
            [
                {'message': u'''terça (01/10) a qualquer hora.'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 59))
            ],
            [
                {'message': u'''terça (01/10) a qualquer horario.'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 59))
            ],
            [
                {'message': u'''saindo até 12hrs.'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(12, 0))
            ],
            [
                {'message': u'''Procuro São Carlos - São Paulo para amanhã (01/10) depois das 16!.'''},
                datetime.datetime.combine(datetime_today, datetime.time(16, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 59))
            ],
            [
                {'message': u''''sao paulo - sao carlos na terca-feira 15/10 a partir das 18h.'''},
                datetime.datetime.combine(datetime_today, datetime.time(18, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 59))
            ],
            [
                {'message': u''''14h/15h'''},
                datetime.datetime.combine(datetime_today, datetime.time(14, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(15, 0))
            ],
            [
                {
                'message': u''''dia 26 de outubro eu queria ... pode me dar uma carona --> qualquer hora'''},
                datetime.datetime.combine(datetime_today, datetime.time(6, 0)),
                datetime.datetime.combine(datetime_today, datetime.time(23, 59))
            ],
        ]

        for p in example_posts:
            post = CaronaPost(p[0])
            ## just for testing
            post.tag_date = datetime_today
            # pprint(post.content_clean)
            ## datetime
            post.retrieve_time_tags()
            self.assertTrue(post.retrieve_time_tags(), 'not found interval tag time')
            print(post.tag_time, 'vs', p[1])
            self.assertEqual(post.tag_time, p[1], 'not correct time from ' + p[0]['message'])
            self.assertEqual(post.tag_time_to, p[2], 'not correct time to')
        return