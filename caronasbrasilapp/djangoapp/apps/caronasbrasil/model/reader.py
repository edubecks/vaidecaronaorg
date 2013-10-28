# coding: utf-8
from djangoapp.apps.caronasbrasil.model.post import Post

__author__ = 'edubecks'


class Reader(object):

    def __init__(self, feed):
        self.feed = feed

        self.posts = []

        return

    def read_posts(self):

        for each_post in self.feed['data']:
            post = Post(each_post)
            self.posts.append(post)
            print(post.content)

        return

    def search_by_tag(self,tag):
        posts = []
        for post in self.posts:
            if post.has_tag(tag):
                posts.append(post)

        return posts