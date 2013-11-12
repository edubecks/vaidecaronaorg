# coding: utf-8
import re
import datetime
import unidecode

__author__ = 'edubecks'


class Post(object):

    def _get_formatted_tag(self, tag):
        return '#' + tag

    def __init__(self, info):
        self._info = info
        self.tags = []

        ## post content
        self.content = self._info['message']
        self.content_clean = unidecode.unidecode(self._info['message']).lower().replace('\n', ' ')

        ## post creator
        self.fb_user_id = self._info['from']['id']

        ##post info
        if 'id' in self._info:
            self.fb_group_id, self.fb_post_id = self._info['id'][:self._info['id'].index('_')], self._info['id']
            print 'parsing:', self.fb_post_id

        ## post comments
        self.comments = []
        if 'comments' in self._info:
            for comment in self._info['comments']['data']:
                self.comments.append(comment['message'])
        return

    def set_admin_tags(self,tags):
        self.admin_tags =  tags
        self._retrieve_tags()
        return


    def _retrieve_tags(self):

        for tag_text, tag in self.admin_tags.iteritems():
            if tag_text in self.content_clean:
                self.tags.append(tag)
        return self.tags


    def has_tag(self,tag):
        return tag in self.tags

