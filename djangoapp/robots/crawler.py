# coding: utf-8
from pprint import pprint
from model.caronasbrasil.carona_post import CaronaPost
from model.fb_groups.fb_groups_controller import FBGroupsController
from caronasbrasil.persistence_controller import PersistenceController

__author__ = 'edubecks'

class Crawler(object):

    def __init__(self):

        return

    def retrieve_posts(self, fb_group_id):

        ## persistence
        persistence = PersistenceController()
        city1_list, city2_list = persistence.get_city1_city2_for_fb_group_id(fb_group_id)

        ## getting feed
        fb_manager = FBGroupsController(fb_group_id)
        feed = fb_manager.get_posts()

        for fb_post in feed:

            ## check if exists
            if not persistence.exists_post(fb_post['id']):


                pprint(fb_post)
                ## create new carona post
                carona_post  = CaronaPost(fb_post)
                pprint(carona_post.content_clean)

                ## setting origin and destiny
                carona_post.city1_list = city1_list
                carona_post.city2_list = city2_list

                 ## date / time
                has_date_tag = carona_post.retrieve_date_tags()
                has_time_tag = carona_post.retrieve_time_tags()

                ## origin_destiny
                has_origin_destiny =  carona_post.retrieve_origin_destiny()

                ## oferecer/ procurar
                has_ofereco_procuro = carona_post.retrieve_ofereco_procuro_tag()

                ## [OPTIONAL] numero de vagas
                has_vagas = carona_post.retrieve_vagas()

                ## check the tag requirements
                if has_date_tag and has_time_tag and has_origin_destiny and has_ofereco_procuro:
                    ## saving in the db
                    pprint('---------------------')

                    pprint(str(carona_post))
                    persistence.add_carona(carona_post)
                else:
                    print('*************** wrong')
                    pprint(carona_post.content_clean)
                    pprint(str(carona_post))
                    print('*******************************************')


        return
