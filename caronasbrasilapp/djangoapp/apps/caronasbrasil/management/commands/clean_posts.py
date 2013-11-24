# coding: utf-8
from djangoapp.apps.caronasbrasil.persistence_controller import PersistenceController

__author__ = 'edubecks'
from djangoapp.apps.caronasbrasil.main_controller import MainController
from optparse import make_option
from django.core.management.base import BaseCommand, NoArgsCommand


class Command(NoArgsCommand):
    help = 'crawler of FB posts'

    def handle(self, *args, **options):
        ## execute robot
        ## clean deleted posts from facebook
        MainController().clean_deleted_posts()

        ## clean old posts
        PersistenceController().clean_old_posts()
        return

