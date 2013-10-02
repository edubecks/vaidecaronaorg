# coding: utf-8
from pprint import pprint
import re
import datetime
from datetime_post import DateTimePost

__author__ = 'edubecks'


class CaronaPost(DateTimePost):
    def __init__(self, info):
        super(CaronaPost, self).__init__(info)
        self.tag_ofereco_procuro = ''
        self.tag_time = ''
        self.tag_origin = ''
        self.tag_destiny = ''
        self.tag_date = ''
        self.city1_list = []
        self.city2_list = []
        return

    def retrieve_origin_destiny(self):

        ## creating regex
        regex_cities_pattern = [
            r'\s*-{0,3}>\s*',
            r'\s*-{1,3}\s*',
            r'\s*para\s*',
            r'\s*\={0,3}>\s*',
            r'\s*\>{0,3}\s*',
            u'\s*》\s*',
        ]
        regex_city1_city2 = []
        regex_city2_city1 = []
        for city1 in self.city1_list:
            for city2 in self.city2_list:
                for regex in regex_cities_pattern:
                    # print self.city1_list, city1, city2, regex
                    ## using raw strings to use backslash in regex
                    regex_city1_city2.append(r'('+city1+r')'+regex+ r'(' + city2 + r')')
                    regex_city2_city1.append(r'('+city2+r')'+regex+ r'(' + city1 + r')')

        ## searching for regex
        city1 = self.city1_list[0]
        city2 = self.city2_list[0]

        ## city1 -> city2
        for regex_expression in regex_city1_city2:
            regex = re.compile(regex_expression, re.IGNORECASE)
            match = regex.search(self.content_clean)
            # print regex_expression, self.content_clean
            if match:
                self.tag_origin = city1
                self.tag_destiny = city2
                print self.tag_origin, self.tag_destiny
                return True
                # print(self.content_clean, regex_expression )

        ## city2-> city1
        for regex_expression in regex_city1_city2:
            regex = re.compile(regex_expression, re.IGNORECASE)
            match = regex.search(self.content_clean)
            # print regex_expression, self.content_clean
            if match:
                self.tag_origin = city2
                self.tag_destiny = city1
                print self.tag_origin, self.tag_destiny
                return True
                # print(self.content_clean, regex_expression )

        return False

    def retrieve_time_tags(self):
        super(CaronaPost, self).retrieve_time_tags()

        ## if already found time
        if self.tag_time:
            return True

        regex_am_pm_time = [
            r'(\d{1,2})\s*?(da manha|da tarde|da noite)',
        ]
        for regex_expression in regex_am_pm_time:
            regex = re.compile(regex_expression)
            match = regex.search(self.content_clean)
            if match:
                hour = int(match.group(1)) if match.group(2) == 'da manha' else int(match.group(1)) + 12
                minutes = 0
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.time(hour, minutes)
                return True

        ## not found time
        return False


    def retrieve_ofereco_procuro_tag(self):

        ## procurar
        procurar_tags = ['procuro', 'busco']
        for t in procurar_tags:
            if t in self.content_clean:
                self.tag_ofereco_procuro = 'procurar'
                return True

        ## oferecer
        oferecer_tags = ['ofereco']
        for t in oferecer_tags:
            if t in self.content_clean:
                self.tag_ofereco_procuro = 'oferecer'
                return True
        return False


    def retrieve_vagas(self):

        regex_vagas = [
            r'(\d{1,2})\s*?(vaga|lugar|pessoa)',
        ]
        for regex_expression in regex_vagas:
            regex = re.compile(regex_expression)
            match = regex.search(self.content_clean)
            if match:
                self.tag_num_vagas = int(match.group(1))
                return True

        return False




