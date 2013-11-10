# coding: utf-8
from pprint import pprint
from djangoapp.apps.caronasbrasil.model.caronasbrasil.carona_post import CaronaPost
from djangoapp.apps.caronasbrasil.model.fb_groups.fb_groups_controller import FBGroupsController
from djangoapp.apps.caronasbrasil.persistence_controller import PersistenceController

__author__ = 'edubecks'

class Crawler(object):

    ## default time_interval 1 week = 60min * 24h *7d
    def __init__(self, time_interval=10080):
        self.time_interval = time_interval
        return

    def log_not_parsed_post(self,carona_post):
        PersistenceController().add_parser_error(carona_post.fb_group_id,
                                                 carona_post.fb_post_id, carona_post.content_clean)
        return

    def retrieve_posts(self, fb_group_id):

        ## persistence
        persistence = PersistenceController()
        city1, city1_state, city1_list, city2, city2_state, city2_list = \
            persistence.get_cities_by_fb_group_id(fb_group_id)

        ## getting feed
        fb_manager = FBGroupsController(fb_group_id)
        feed = fb_manager.get_posts(last_time_checked=self.time_interval)

        for fb_post in feed:

            pprint(feed)

            ## check if the post is not commented
            if (fb_post['message'][:2]!= '//'
            ## check if it is already parsed
                and not persistence.exists_post(fb_post['id'])):

                # pprint(fb_post)
                ## create new carona post
                carona_post  = CaronaPost(fb_post)
                pprint(carona_post.content_clean)

                ## setting origin and destiny
                carona_post.city1 = city1
                carona_post.city1_state = city1_state
                carona_post.city2 = city2
                carona_post.city2_state = city2_state
                
                carona_post.city1_list = city1_list
                carona_post.city2_list = city2_list

                 ## date / time
                has_date_tag = carona_post.retrieve_date_tags()
                carona_post.retrieve_time_tags()
                # has_time_interval = carona_post.retrieve_time_interval()
                has_time_tag = True if carona_post.tag_time else False

                ## origin_destiny
                has_origin_destiny =  carona_post.retrieve_origin_destiny()

                ## oferecer/ procurar
                has_ofereco_procuro = carona_post.retrieve_ofereco_procuro_tag()

                ## [OPTIONAL] numero de vagas
                has_vagas = carona_post.retrieve_vagas()

                ## check the tag requirements
                print(has_date_tag, has_time_tag, has_origin_destiny, has_ofereco_procuro)
                if has_date_tag and has_time_tag and has_origin_destiny and has_ofereco_procuro:
                    ## saving in the db
                    pprint(str(carona_post))
                    pprint('---------------------')
                    persistence.add_carona(carona_post)
                else:
                    print('*************** wrong')
                    pprint(carona_post.content_clean)
                    pprint(str(carona_post))
                    print('*******************************************')
                    self.log_not_parsed_post(carona_post)
            else:
                print('post already parsed', fb_post['id'])


        return
