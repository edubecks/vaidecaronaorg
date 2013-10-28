# coding: utf-8
__author__ = 'edubecks'

class FBAPIManager(object):

    def __init__(self):

        return

    def read_group_feed(self, group_id):

        feed = {u'data': [
            {u'actions': [{u'link': u'https://www.facebook.com/641749869191341/posts/643047515728243',
                           u'name': u'Comment'},
                          {u'link': u'https://www.facebook.com/641749869191341/posts/643047515728243',
                           u'name': u'Like'}],
            u'comments': {u'data': [{u'can_remove': True,
                                  u'created_time': u'2013-09-19T13:36:52+0000',
                                  u'from': {u'id': u'677153213',
                                            u'name': u'Eduardo Espinoza'},
                                  u'id': u'643052102394451',
                                  u'like_count': 0,
                                  u'message': u'comentario 1.1',
                                  u'user_likes': False},
                                 {u'can_remove': True,
                                  u'created_time': u'2013-09-19T13:36:59+0000',
                                  u'from': {u'id': u'677153213',
                                            u'name': u'Eduardo Espinoza'},
                                  u'id': u'643052115727783',
                                  u'like_count': 0,
                                  u'message': u'comentario 1.2',
                                  u'user_likes': False}],
                       u'paging': {u'cursors': {u'after': u'NjQzMDUyMTE1NzI3Nzgz',
                                                u'before': u'NjQzMDUyMTAyMzk0NDUx'}}},
            u'created_time': u'2013-09-19T13:24:00+0000',
            u'from': {u'id': u'677153213', u'name': u'Eduardo Espinoza'},
            u'id': u'641749869191341_643047515728243',
            u'message': u'test post 1',
            u'privacy': {u'value': u''},
            u'to': {u'data': [{u'id': u'641749869191341',
                            u'name': u'test-fbgroups'}]},
            u'type': u'status',
            u'updated_time': u'2013-09-19T13:36:59+0000'},
            {u'actions': [{u'link': u'https://www.facebook.com/641749869191341/posts/641767875856207',
                       u'name': u'Comment'},
                      {u'link': u'https://www.facebook.com/641749869191341/posts/641767875856207',
                       u'name': u'Like'}],
            u'comments': {u'data': [{u'can_remove': True,
                                  u'created_time': u'2013-09-19T13:36:40+0000',
                                  u'from': {u'id': u'677153213',
                                            u'name': u'Eduardo Espinoza'},
                                  u'id': u'643052029061125',
                                  u'like_count': 0,
                                  u'message': u'comentario 1',
                                  u'user_likes': False}],
                       u'paging': {u'cursors': {u'after': u'NjQzMDUyMDI5MDYxMTI1',
                                                u'before': u'NjQzMDUyMDI5MDYxMTI1'}}},
            u'created_time': u'2013-09-16T14:42:00+0000',
            u'from': {u'id': u'677153213', u'name': u'Eduardo Espinoza'},
            u'id': u'641749869191341_641767875856207',
            u'message': u'hello world',
            u'privacy': {u'value': u''},
            u'to': {u'data': [{u'id': u'641749869191341',
                            u'name': u'test-fbgroups'}]},
            u'type': u'status',
            u'updated_time': u'2013-09-19T13:36:40+0000'},
            {u'actions': [{u'link': u'https://www.facebook.com/641749869191341/posts/643047619061566',
                       u'name': u'Comment'},
                      {u'link': u'https://www.facebook.com/641749869191341/posts/643047619061566',
                       u'name': u'Like'}],
            u'created_time': u'2013-09-19T13:24:09+0000',
            u'from': {u'id': u'677153213', u'name': u'Eduardo Espinoza'},
            u'id': u'641749869191341_643047619061566',
            u'message': u'test post 2',
            u'privacy': {u'value': u''},
            u'to': {u'data': [{u'id': u'641749869191341',
                            u'name': u'test-fbgroups'}]},
            u'type': u'status',
            u'updated_time': u'2013-09-19T13:24:09+0000'}],
            u'paging': {
                u'next': u'https://graph.facebook.com/641749869191341/feed?access_token=CAAHhR9ZA3zSwBAA3VEbmEK0qUoxIrYbybUD9aEKp2AS74TaEHxekYr6L3TfVHClFzFp9GfKvOUDZCsZBMQBRWAryH2XlfLyaWdWtrbnE6CC1z9fGLEbbpIo9JeV3QhdVph5rBqb6P8iRVXoGroV4PkaqZCIPy02ENOMeAzbHe7oii23qZCzFktfSNXzjxOcMZD&limit=25&until=1379597049&__paging_token=641749869191341_643047619061566',
                u'previous': u'https://graph.facebook.com/641749869191341/feed?access_token=CAAHhR9ZA3zSwBAA3VEbmEK0qUoxIrYbybUD9aEKp2AS74TaEHxekYr6L3TfVHClFzFp9GfKvOUDZCsZBMQBRWAryH2XlfLyaWdWtrbnE6CC1z9fGLEbbpIo9JeV3QhdVph5rBqb6P8iRVXoGroV4PkaqZCIPy02ENOMeAzbHe7oii23qZCzFktfSNXzjxOcMZD&limit=25&since=1379597819&__paging_token=641749869191341_643047515728243&__previous=1'}}

        return feed