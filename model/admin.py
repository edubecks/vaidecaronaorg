# coding: utf-8
__author__ = 'edubecks'


class Admin(object):

    FG_PREFIX = 'FG'
    FG_CONFIG = 'FACEBOOKGROUPS'
    FG_CLOSED = 'FG_CLOSED'


    def __init__(self, group_id):
        self.group_id = group_id

        tags = {
            u'São Carlos --> São Paulo': 'sc2sp',
            u'São Carlos -> São Paulo': 'sc2sp',
            u'São Carlos - São Paulo': 'sc2sp',
            u'SC --> SP': 'sc2sp',
            u'SC -> SP': 'sc2sp',
            u'SC - SP': 'sc2sp',
            u'São Carlos - SP': 'sc2sp',
            u'ofereço': 'ofereco',
            u'procuro': 'procuro',
        }

        self.tags = {}
        for tag_text, tag in tags.iteritems():
            self.tags[tag_text.lower()] = tag
        return

    def add_tag(self, tag_text, tag):
        self.tags[tag_text] = tag
        return


    def add_tag_to_post(self, post):
        ## todo implement
        return