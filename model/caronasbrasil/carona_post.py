# coding: utf-8
import re
import datetime
from datetime_post import DateTimePost

__author__ = 'edubecks'


class CaronaPost(DateTimePost):
    def __init__(self, info):
        super(CaronaPost, self).__init__(info)
        return

    def retrieve_time_tags(self):
        super(CaronaPost, self).retrieve_time_tags()

        ## no tag time found using others
        if not self.tag_time:
        ## am pm
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
                    return




