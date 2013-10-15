# coding: utf-8
import collections
from pprint import pprint
import re
import datetime
from model.datetime_post import DateTimePost

__author__ = 'edubecks'


class CaronaPost(DateTimePost):
    def __init__(self, info):
        super(CaronaPost, self).__init__(info)
        self.fb_id = None
        self.tag_ofereco_procuro = ''
        self.tag_time = None
        self.tag_origin = ''
        self.tag_destiny = ''
        self.tag_date = ''
        self.tag_num_vagas = 1
        self.city1_list = []
        self.city2_list = []
        return

    @property
    def tag_datetime(self):
        if self.tag_date and self.tag_time:
            return datetime.datetime.combine(self.tag_date, self.tag_time)
        return None

    def retrieve_origin_destiny(self):

        ## creating regex
        regex_cities_pattern = [
            r'\s*-{0,3}>\s*',
            r'\s*-{1,3}\s*',
            r'\s*para\s*',
            r'\s*\={0,3}>\s*',
            r'\s*\>{0,3}\s*',
            r'\s* x \s*',
            u'\s*\u300B\s*',
            u'\s*\u27EB\s*',
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
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print regex_expression, self.content_clean
            if match:
                self.tag_origin = city1
                self.tag_destiny = city2
                # print self.tag_origin, self.tag_destiny
                return True
                # print(self.content_clean, regex_expression )

        ## city2-> city1
        for regex_expression in regex_city2_city1:
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print regex_expression, self.content_clean
            if match:
                self.tag_origin = city2
                self.tag_destiny = city1
                # print self.tag_origin, self.tag_destiny
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
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
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
        procurar_tags = ['procur', 'busc']
        for t in procurar_tags:
            if t in self.content_clean:
                self.tag_ofereco_procuro = 'procurar'
                return True

        ## oferecer
        oferecer_tags = ['oferec']
        for t in oferecer_tags:
            if t in self.content_clean:
                self.tag_ofereco_procuro = 'oferecer'
                return True
        return False


    def retrieve_vagas(self):

        regex_vagas = [
            r'(\d{1,2}) *?(vaga|lugar|pessoa)',
            r'(?:vaga|lugar|pessoa)(?:es|s)?:? *(\d{1,2})',
            r'(uma) *?(vaga|lugar|pessoa)',
            r'(duas) *?(vaga|pessoa)',
            r'(dois) *?(lugar)',
            r'(tres) *?(vaga|lugar|pessoa)',
            r'(quatro) *?(vaga|lugar|pessoa)',
        ]

        numbers = {
            'uma': 1,
            'duas': 2,
            'dois': 2,
            'tres': 3,
            'quatro': 4,
        }
        for regex_expression in regex_vagas:
            regex = re.compile(regex_expression, re.IGNORECASE)
            match = regex.search(self.content_clean)
            if match:
                # print regex_expression, self.content_clean
                try:
                    self.tag_num_vagas = int(match.group(1))
                except ValueError:
                    self.tag_num_vagas = int(numbers[match.group(1)])
                return True

        return False

    def retrieve_date_tags(self):
        if super(CaronaPost, self).retrieve_date_tags():
           return True

        ## detect using month
        regex_date = [
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(jan)(?:eiro)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(fev)(?:ereiro)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(mar)(?:co)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(abr)(?:il)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(mai)(?:o)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(jun)(?:ho)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(jul)(?:ho)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(ago)(?:sto)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(set)(?:embro)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(out)(?:ubro)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(nov)(?:embro)?',
            r'(\d{1,2})\s*?(?:de|\/)?\s*?(dez)(?:embro)?',
        ]
        for i, regex_expression in enumerate(regex_date):
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print self.content_clean
            if match:
                # print match.groups()
                day = int(match.group(1))
                month = i+1
                # print(regex_expression, day, month)
                self.tag_date = datetime.date(2013, month, day)
                return True

        regex_named_dates = [
            r'(seg|2da|2a)(?:unda)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?',
            r'(ter|3ca|3a)(?:ca)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?'  ,
            r'(qua|4ta|4a)(?:rta)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?' ,
            r'(qui|5ta|5a)(?:nta)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?' ,
            r'(sex|6ta|6a)(?:ta)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?'  ,
            r'(sab)(?:ado)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?' ,
            r'(dom)(?:ingo)?\s*?(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?',
        ]

        for day, regex_expression in enumerate(regex_named_dates):
            # print day, regex_expression
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print self.content_clean
            # print regex_expression
            if match:
                # print match.groups(), match.lastindex
                d = self.creation_date
                max_days = 6
                while d.weekday() != day and max_days: ## day: number of day, monday=0
                    d += datetime.timedelta(1)
                    max_days-=1
                self.tag_date = d
                # print self.tag_date
                # day = int(match.group(1))
                # month = i + 1
                # print(regex_expression, day)
                # self.tag_date = datetime.date(2013, month, day)
                return True

        ## special cases: today, tomorrow, the day after tomorrow
        special_cases= collections.OrderedDict([('depois de amanha',2), ('amanha',1), ('hoje',0)])
        for c, delta_time in special_cases.iteritems():
            # print "*",c,"*", self.content_clean,"*"
            if c in self.content_clean:
                self.tag_date = self.creation_date + datetime.timedelta(delta_time)
                # print self.tag_date
                return True

        ## nothing found
        return False

    def __str__(self):
        return str({
            'ofereco/procuro': self.tag_ofereco_procuro,
            'from': self.tag_origin,
            'to': self.tag_destiny,
            'datetime': self.tag_datetime,
            'date': self.tag_date,
            'time': self.tag_time,
            'num_vagas': self.tag_num_vagas
        })


