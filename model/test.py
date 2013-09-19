# coding: utf-8
import os

__author__ = 'edubecks'

from pprint import pprint

# # oauth_access_token = facebook.get_app_access_token(config.DEV_FB_APP_ID, config.DEV_FB_APP_SECRET)
# oauth_access_token = config.OAUTH_TOKEN
# graph = facebook.GraphAPI(oauth_access_token)
# profile = graph.get_object('me')
# group = graph.get_object('641749869191341')
# pprint(group)


import facebook
import urllib
import urlparse
import subprocess
import warnings

# Keep Facebook settings like APP_ID
import settings
import os



# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id=settings.DEV_FB_APP_ID,
                  client_secret=settings.DEV_FB_APP_SECRET,
                  grant_type='client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()

# facebook_graph = facebook.GraphAPI(oauth_access_token)
facebook_graph = facebook.GraphAPI(settings.LONG_LIVED_OAUTH_TOKEN)

# Try to post something on the wall.
try:
    # friends = facebook_graph.get_connections('me', 'friends')
    # pprint(friends)
    group_feed = facebook_graph.get_connections('641749869191341', 'feed')
    pprint(group_feed)

except facebook.GraphAPIError as e:
    print 'Something went wrong:', e.type, e.message