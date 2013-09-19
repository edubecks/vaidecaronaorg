# coding: utf-8
__author__ = 'edubecks'

from facepy.utils import get_extended_access_token
from facepy import GraphAPI

import settings

long_lived_access_token, expires_at = get_extended_access_token(settings.OAUTH_TOKEN,
                                                                settings.DEV_FB_APP_ID,
                                                                settings.DEV_FB_APP_SECRET)
print long_lived_access_token

graph = GraphAPI(long_lived_access_token)
print(graph.get('/me'))
