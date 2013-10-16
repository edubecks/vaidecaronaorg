# coding: utf-8
import re
import datetime
from post import Post

__author__ = 'edubecks'

class DateTimePost(Post):

    def __init__(self, info):
        super(DateTimePost, self).__init__(info)
        self.tag_time = None
        self.tag_date = None
        self.post_date = None

        ## creation_date
        if 'created_time' in info:
            self.creation_date = datetime.datetime.strptime(info['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            print self.creation_date
        return

    def retrieve_time_tags(self):

        """
        Ex:
        Saio sexta feira, dia 20/09, as 19 horas    --> (19,0)
        Quinta-feira, 20/09, saida as 19h           --> (19,0)
        Sexta feira - 20/09\nPor volta do 19hrs     --> (19,0)
        19:30                                       --> (19,30)
        7pm

        """

        ## am pm
        regex_am_pm_time = [
            r'(\d{1,2})([h|:]\d{2})?\s*?(am|pm|a\.m|p\.m)',
        ]
        for regex_expression in regex_am_pm_time:
            regex = re.compile(regex_expression)
            match = regex.search(self.content_clean)
            if match:
                ## am/pm tag
                # print match.groups(), match.lastindex
                ampm = match.group(3) if match.lastindex == 3 else match.group(2)
                hour = int(match.group(1)) if (ampm == 'am' or ampm == 'a.m') else int(match.group(1)) + 12
                minutes = int(match.group(2)[1:]) if match.group(2) else 0
                # print ampm, hour, minutes
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.time(hour, minutes)
                return True

        ## 24h
        regex_24h_time = [
            r'(\d{1,2})(:\d{2})?\s*?(?:hrs|horas|h |hs)',
            # r'(\d{2})h\s',
            # r'(\d{2})\s*horas',
            # r'(\d{2})\s*hrs',
            r'(\d{1,2})(h\d{2})',
            r'(\d{2})(:\d{2})',
        ]
        for regex_expression in regex_24h_time:
            regex = re.compile(regex_expression)
            match = regex.search(self.content_clean)
            if match:
                hour = int(match.group(1))
                minutes = int(match.group(2)[1:]) if match.lastindex == 2 else 0
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.time(hour, minutes)
                return True


        ## not found
        return False

    def retrieve_date_tags(self):
        """
        Ex:
        Saio sexta feira, dia 20/09, as 19 horas    --> (20, 09)
        Quinta-feira, 20/09, saida as 19h           --> (20, 09)
        Sexta feira - 20/09\nPor volta do 19hrs     --> (20, 09)
        """
        regex_date = [
            r'(\d{1,2})\/(\d{1,2})',
        ]
        for regex_expression in regex_date:
            regex = re.compile(regex_expression)
            match = regex.search(self.content_clean)
            if match:
                day = int(match.group(1))
                month = int(match.group(2))
                # print(regex_expression, day, month)
                self.tag_date = datetime.date(2013, month, day)
                return True



        return False