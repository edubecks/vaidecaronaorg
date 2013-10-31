# coding: utf-8
from pprint import pprint
from djangoapp.apps.caronasbrasil.models import CaronaModel, CaronaGroupModel, ParserErrorsModel
from django.db.models import Q

__author__ = 'edubecks'


class PersistenceController(object):
    def __init__(self):
        return

    def add_carona(self, carona_post):
        new_carona = CaronaModel(
            fb_post_id=carona_post.fb_post_id,
            fb_group_id=carona_post.fb_group_id,
            fb_user_id=carona_post.fb_user_id,
            fb_content = carona_post.content,
            origin=carona_post.tag_origin,
            destiny=carona_post.tag_destiny,
            from_datetime=carona_post.tag_time,
            to_datetime=carona_post.tag_time_to,
            ofereco_procuro=carona_post.tag_ofereco_procuro[0], ## o: ofereco, p: procuro
            num_vagas=carona_post.tag_num_vagas
        ).save()
        return new_carona

    def exists_post(self, fb_post_id):
        return CaronaModel.objects.filter(fb_post_id=fb_post_id).count() > 0


    def get_cities_by_fb_group_id(self, fb_group_id):
        carona_group = CaronaGroupModel.objects.get(fb_group_id=fb_group_id)
        city1_list = carona_group.city1_list.split(',')
        city2_list = carona_group.city2_list.split(',')
        return (
            carona_group.city1, carona_group.city1_state, city1_list,
            carona_group.city2, carona_group.city2_state, city2_list
        )

    def add_parser_error(self, fb_group_id, fb_post_id, message_content):
        return ParserErrorsModel(
            fb_group_id=fb_group_id,
            fb_post_id=fb_post_id,
            content=message_content
        ).save()


    def get_carona_paths(self):
        paths = {}
        for p in CaronaGroupModel.objects.all():

            if not p.city1_state in paths:
                paths[p.city1_state] = []
            paths[p.city1_state].append({
                'id': p.fb_group_id,
                'from': p.city1,
                'to': p.city2,
                'to_state': p.city2_state,
            })

            if not p.city2_state in paths:
                paths[p.city2_state] = []
            paths[p.city2_state].append({
                'id': p.fb_group_id,
                'from': p.city2,
                'to': p.city1,
                'to_state': p.city1_state,
            })

        return paths

    def search_carona(self, ofereco_procuro, from_city, from_city_state, to_city, to_city_state,
                      from_datetime, to_datetime):
        return CaronaModel.objects.filter(
            origin=from_city+'/'+from_city_state,
            destiny =to_city + '/' + to_city_state,
            ofereco_procuro = ofereco_procuro,
            num_vagas = 1
        ).filter(
            ## Example: in DB 10-12
            ## case: 10-12 vs 9-13 searching superset
            Q(from_datetime__gte=from_datetime, to_datetime__lte=to_datetime) |
            ## case: 10-12 vs 11-13
            Q(to_datetime__gte=from_datetime, to_datetime__lte=to_datetime) |
            ## case: 10-12 vs 9-11
            Q(from_datetime__gte=from_datetime, from_datetime__lte=to_datetime) |
            ## case: 10-12 vs 10:30-11 searching subset
            Q(from_datetime__lte=from_datetime, to_datetime__gte=to_datetime)
        )