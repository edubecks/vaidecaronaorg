# coding: utf-8
from djangoapp.apps.caronasbrasil.model.datetime_post import DateTimePost

__author__ = 'edubecks'

from unittest import TestCase


class DateTimePostTestCase(TestCase):
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
            {
                'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 12hrs Saindo do metro consolação.'''},
            {
                'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 12:05pm Saindo do metro consolação.'''},
            {
                'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 15:10 hrs Saindo do metro consolação.'''},
            {
                'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 am Saindo do metro consolação.'''},
            {
                'message': u'''Ofereço São Paulo -> São Carlos Sexta feira - 20/09 Por volta do 7 pm Saindo do metro consolação.'''},
        ]
        return

    def test_time_parser(self):
        for p in self.posts_dict:
            post = DateTimePost(p)
            post.retrieve_time_tags()
        return
