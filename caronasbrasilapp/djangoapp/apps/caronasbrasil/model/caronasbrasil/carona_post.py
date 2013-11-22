# coding: utf-8
import collections
import re
import datetime
from djangoapp.apps.caronasbrasil.model.datetime_post import DateTimePost

__author__ = 'edubecks'


class CaronaPost(DateTimePost):
    def __init__(self, info):
        super(CaronaPost, self).__init__(info)
        self.fb_id = None
        self.tag_ofereco_procuro = ''
        self.tag_time = None
        self.tag_time_to = None
        self.tag_origin = ''
        self.tag_destiny = ''
        self.tag_date = ''
        self.tag_num_vagas = 1
        self.city1 = ''
        self.city1_state = ''
        self.city2 = ''
        self.city2_state = ''
        self.city1_list = []
        self.city2_list = []
        return

    @property
    def tag_datetime(self):
        return self.tag_time

    def retrieve_origin_destiny(self):

        ## creating regex
        regex_cities_pattern = [
            r'\s*-{0,10}\s*>{1,10}\s*',
            r'\s*~{0,10}\s*>{1,10}\s*',
            r'\s*-{1,10}\s*',
            r'\s*para\s*',
            r'\s*pra\s*',
            r'\s*\={0,10}\s*>{1,10}\s*',
            r'\s*>{1,10}\s*',
            r'\s*/{1,10}\s*',
            r'\s* x \s*',
            r'\s* a \s*',
            r'\s* ate \s*',
            r'\s* ate: \s*',
            u'\s*\u300B\s*',
            u'\s*\u27EB\s*',
        ]

        ## TODO-optimizar
        ## criar combinacoes na hora e nao antes
        regex_city1_city2 = []
        regex_city2_city1 = []
        for city1 in self.city1_list:
            for city2 in self.city2_list:
                for regex in regex_cities_pattern:
                    # print self.city1_list, city1, city2, regex
                    ## using raw strings to use backslash in regex
                    regex_city1_city2.append(r'('+city1+r')'+regex+ r'(' + city2 + r')')
                    regex_city2_city1.append(r'('+city2+r')'+regex+ r'(' + city1 + r')')

        ## cities
        city1 = self.city1+'/'+self.city1_state
        city2 = self.city2+'/'+self.city2_state

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

        regex_to_city_pattern = [
            r'\s*para\s*({to_city})',
            r'\s*pra\s*({to_city})',
            r'\s*p/\s*({to_city})',
        ]

        for regex_expression in regex_to_city_pattern:
            ## to city1
            for city in self.city1_list:
                regex = re.compile(regex_expression.format(to_city=city) , re.IGNORECASE | re.MULTILINE)
                match = regex.search(self.content_clean)
                if match:
                    self.tag_origin = city2
                    self.tag_destiny = city1
                    return True

            ## to city2
            for city in self.city2_list:
                regex = re.compile(regex_expression.format(to_city=city) , re.IGNORECASE | re.MULTILINE)
                match = regex.search(self.content_clean)
                if match:
                    self.tag_origin = city1
                    self.tag_destiny = city2
                    return True

        return False

    def retrieve_time_tags(self):

        CARONA_START_DATETIME = datetime.time(6, 0)
        CARONA_END_DATETIME = datetime.time(23, 59)

        ## after time
        regex_after_time = [
            r'(?:depois|a partir) das (\d{1,2})()(?:[h|:])(\d{2})', ## () for simplicity in group capturing
            r'(?:depois|a partir) das (\d{1,2})\s*(hrs|horas|h |hs)()',
            r'(?:depois|a partir) das (\d{1,2})\s*(am|pm|a\.m|p\.m)()',
            r'(?:depois|a partir) das (\d{1,2})()()', ## () for simplicity in group capturing
            r'(?:apos) as (\d{1,2})()(?:[h|:])(\d{2})', ## () for simplicity in group capturing
            r'(?:apos) as (\d{1,2})()()', ## () for simplicity in group capturing
        ]
        for regex_expression in regex_after_time:
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print(self.content_clean)
            if match:
                ampm = match.group(2)
                hour = int(match.group(1))
                hour = hour + 12 if ampm == 'pm' or ampm == 'p.m' else hour
                minutes = int(match.group(3)) if match.group(3) else 0
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.datetime.combine(self.tag_date, datetime.time(hour, minutes))
                ## default time interval
                self.tag_time_to = datetime.datetime.combine(self.tag_date, CARONA_END_DATETIME)
                return True

        ## until time
        regex_to_time = [
            r'(?:ate)\s*(?:as)?\s*(\d{1,2})\s*(hrs|horas|h |hs)',
            r'(?:ate)\s*(?:as)?\s*(\d{1,2})\s*(am|pm|a\.m|p\.m)',
            r'(?:ate)\s*(?:as)?\s*(\d{1,2})\s*(da manha|da tarde)',
        ]
        for regex_expression in regex_to_time:
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print(self.content_clean)
            if match:
                ampm = match.group(2)
                hour = int(match.group(1))
                hour = hour + 12 if ampm == 'pm' or ampm == 'p.m' or ampm == 'da tarde' else hour
                minutes = 0
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.datetime.combine(self.tag_date, CARONA_START_DATETIME)
                ## default time interval
                self.tag_time_to = datetime.datetime.combine(self.tag_date,
                                                             datetime.time(hour, minutes))
                # print self.tag_time, self.tag_time_to
                return True

        ## interval
        ## begin/end
        regex_interval_time = [
            r'(\d{1,2})\s*(?:hrs|horas|h|hs)/(\d{1,2})\s*(?:hrs|horas|h|hs)',
            r'entre (\d{1,2})\s*(?:hrs|horas|h|hs).*?e\s*(\d{1,2})\s*(?:hrs|horas|h|hs)'
        ]
        for regex_expression in regex_interval_time:
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print(self.content_clean)
            if match:
                hour_begin = int(match.group(1))
                hour_end = int(match.group(2))
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.datetime.combine(self.tag_date, datetime.time(hour_begin, 0))
                ## default time interval
                self.tag_time_to = datetime.datetime.combine(self.tag_date, datetime.time(hour_end, 0))
                return True

        ## any time
        interval_time_indentifiers = [
            'qualquer hora',
            'qualquer horario',
            'qq horario',
            'qqer horario',
        ]
        for t in interval_time_indentifiers:
            if t in self.content_clean:
                ## default time interval
                self.tag_time = datetime.datetime.combine(self.tag_date, CARONA_START_DATETIME)
                self.tag_time_to = datetime.datetime.combine(self.tag_date, CARONA_END_DATETIME)
                return True

        ## looking for time
        super(CaronaPost, self).retrieve_time_tags()

        ## if already found time
        DEFAULT_TIME_INTERVAL = 1
        if self.tag_time:
            self.tag_time_to = self.tag_time + datetime.timedelta(hours=DEFAULT_TIME_INTERVAL)
            return True

        regex_am_pm_time = [
            r'(\d{1,2})\s*?(da manha|da tarde|da noite)',
        ]
        for regex_expression in regex_am_pm_time:
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print(self.content_clean)
            if match:
                hour = int(match.group(1)) if match.group(2) == 'da manha' else int(match.group(1)) + 12
                minutes = 0
                # print(regex_expression, hour, minutes)
                self.tag_time = datetime.datetime.combine(self.tag_date,
                                                          datetime.time(hour, minutes))
                self.tag_time_to = self.tag_time + datetime.timedelta(hours=DEFAULT_TIME_INTERVAL)
                return True



        ## todo
        ## de manha, a noite, a tarde
        ## de manha
        manha_identifiers = ['de manha', 'da manha', 'pela manha']
        for t in manha_identifiers:
            if t in self.content_clean:
                self.tag_time = datetime.datetime.combine(self.tag_date, CARONA_START_DATETIME)
                self.tag_time_to = datetime.datetime.combine(self.tag_date, datetime.time(12, 0))
                return True

        ## a tarde
        tarde_identifiers = ['a tarde', 'depois do almoco']
        for t in tarde_identifiers:
            if t in self.content_clean:
                self.tag_time = datetime.datetime.combine(self.tag_date, datetime.time(12, 0))
                self.tag_time_to = datetime.datetime.combine(self.tag_date, datetime.time(18, 0))
                return True

        ## a noite
        tarde_identifiers = ['a noite']
        for t in tarde_identifiers:
            if t in self.content_clean:
                self.tag_time = datetime.datetime.combine(self.tag_date, datetime.time(18, 0))
                self.tag_time_to = datetime.datetime.combine(self.tag_date, CARONA_END_DATETIME)
                return True

        ## default: anytime
        if self.tag_date:
            self.tag_time = datetime.datetime.combine(self.tag_date, CARONA_START_DATETIME)
            self.tag_time_to = datetime.datetime.combine(self.tag_date, CARONA_END_DATETIME)
            return True


        ## look for interval
        return False


    def retrieve_ofereco_procuro_tag(self):

        ## procurar
        procurar_tags = ['procur', 'busc', 'pode me dar uma carona', 'da carona', 'alguem indo', 'preciso de carona']
        for t in procurar_tags:
            if t in self.content_clean:
                self.tag_ofereco_procuro = 'procurar'
                return True

        ## oferecer
        oferecer_tags = ['oferec','deixo', 'pego na']
        for t in oferecer_tags:
            if t in self.content_clean:
                self.tag_ofereco_procuro = 'oferecer'
                return True
        return False


    def retrieve_vagas(self):

        regex_vagas = [
            r'(?:vaga|lugar|pessoa)(?:es|s)?:? *(\d)\s',
            r'(\d) *?(vaga|lugar|pessoa)',
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
                self.tag_date = datetime.datetime(2013, month, day)
                return True

        regex_named_dates = [
            r'(seg|2da|2a)(?:unda)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?',
            r'(ter|3ca|3a)(?:ca)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?'  ,
            r'(qua|4ta|4a)(?:rta)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?' ,
            r'(qui|5ta|5a)(?:nta)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?' ,
            r'(sex|6ta|6a)(?:ta)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?'  ,
            r'(sab)(?:ado)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?' ,
            r'(dom)(?:ingo)?(?:\s+|-)(?:feira)?,?\s*?(?:dia)?\s*?(\d{1,2})?',
        ]

        for day, regex_expression in enumerate(regex_named_dates):
            # print day, regex_expression
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print self.content_clean
            # print regex_expression
            if match:
                # print match.groups(), match.lastindex, day
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

        regex_number_dates = [
            r'dia (\d{1,2})'
        ]
        for i, regex_expression in enumerate(regex_number_dates):
            regex = re.compile(regex_expression, re.IGNORECASE | re.MULTILINE)
            match = regex.search(self.content_clean)
            # print self.content_clean
            if match:
                # print match.groups()
                day = int(match.group(1))
                month = self.creation_date.month
                # print(regex_expression, day, month)
                self.tag_date = datetime.datetime(2013, month, day)
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
        self.tag_date = self.creation_date
        return True

    def __str__(self):
        return str({
            'o/p': self.tag_ofereco_procuro,
            'from': self.tag_origin,
            'to': self.tag_destiny,
            'time': str(self.tag_time),
            'time_to': str(self.tag_time_to),
            'vagas': self.tag_num_vagas
        })


