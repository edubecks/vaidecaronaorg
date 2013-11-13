# coding: utf-8
__author__ = 'edubecks'
from djangoapp.apps.caronasbrasil.main_controller import MainController
from optparse import make_option
from django.core.management.base import BaseCommand, NoArgsCommand


class Command(NoArgsCommand):
    help = 'crawler of FB posts'

    def handle(self, *args, **options):
        ## execute robot
        MainController().clean_deleted_posts()
        return

