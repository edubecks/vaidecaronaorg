# coding: utf-8
from caronasbrasil.models import CaronaModel, CaronaGroupModel, ParserErrorsModel

__author__ = 'edubecks'


class PersistenceController(object):
    def __init__(self):
        return

    def add_carona(self, carona_post):
        new_carona = CaronaModel(
            fb_post_id=carona_post.fb_post_id,
            origin=carona_post.tag_origin,
            destiny=carona_post.tag_destiny,
            date=carona_post.tag_datetime,
            ofereco_procuro=carona_post.tag_ofereco_procuro[0], ## o: ofereco, p: procuro
            num_vagas=carona_post.tag_num_vagas
        ).save()
        return new_carona

    def exists_post(self, fb_post_id):
        return CaronaModel.objects.filter(fb_post_id=fb_post_id).count() > 0


    def search(self, origin, destiny, begin_datetime, end_datetime):
        return CaronaModel.objects.filter(
            origin=origin, destiny=destiny, date__range=[begin_datetime, end_datetime])

    def get_city1_city2_for_fb_group_id(self, fb_group_id):
        carona_group = CaronaGroupModel.objects.get(fb_group_id=fb_group_id)
        city1_list = carona_group.city1.split(',')
        city2_list = carona_group.city2.split(',')
        return city1_list, city2_list

    def add_parser_error(self,fb_group_id, fb_post_id, message_content):
        return ParserErrorsModel(
            fb_group_id=fb_group_id,
            fb_post_id=fb_post_id,
            content = message_content
        ).save()




