# coding: utf-8
from reader import Reader

__author__ = 'edubecks'

from pprint import pprint
from unittest import TestCase

class ReaderTestCase(TestCase):
    def setUp(self):
        return

    def test_reader(self):
        reader = Reader(None)
        reader.read_posts()
        return