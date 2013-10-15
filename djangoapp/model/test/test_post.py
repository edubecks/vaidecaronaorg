# coding: utf-8
from post import Post

__author__ = 'edubecks'

from pprint import pprint
from unittest import TestCase


class PostTestCase(TestCase):
    def setUp(self):
        self.posts_dict = [
            {'message': u'''Ofereço carona São Carlos - SP
Saio sexta feira, dia 20/09, as 19 horas. Deixo no Metro Ana Rosa e cobro 30 reais. Interessados favor entrar em contato INBOX.'''},
            {'message': u'''Ofereco carona Sao Carlos => Sao Paulo

Quinta-feira, 20/09, saida as 19h

Deixo no metro Faria Lima.

R$30,00

Interessados, contato por inbox'''},
            {'message': u'''Ofereco carona Sao Carlos => Sao Paulo

Quinta-feira, 20/09, saida as 19:30h

Deixo no metro Faria Lima.

R$30,00

Interessados, contato por inbox'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 12hrs Saindo do metro consolação.'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 12:05pm Saindo do metro consolação.'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 15:10 hrs Saindo do metro consolação.'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 am Saindo do metro consolação.'''},
            {'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 pm Saindo do metro consolação.'''},
        ]

        return


    def test_post(self):
        for p in self.posts_dict:
            post = Post(p)
            print(post.content)
        return




