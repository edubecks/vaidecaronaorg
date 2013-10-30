from django.conf.urls import patterns, include, url
from djangoapp.apps.caronasbrasil.views import index, done, search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^djangoapp/', include('djangoapp.foo.urls')),
    url(r'^$', index),

    ## facebook login
    url(r'^done/$', done),
    url('', include('social.apps.django_app.urls', namespace='social')),

    ## caronas brasil
    # procurar/[-\w]+/[-\w]+/[-\d]+/[-\d:]+/[-\d:]+
    url(r'^(?P<op>procurar)/(?P<from_city>[-\w]+)/(?P<to_city>[-\w]+)/(?P<date>[-\d]+)/(?P<from_time>[-\d:]+)/(?P<to_time>[-\d:]+)/$', search),
    url(r'^(?P<op>oferecer)/(?P<from_city>[-\w]+)/(?P<to_city>[-\w]+)/(?P<date>[-\d]+)/(?P<from_time>[-\d:]+)/(?P<to_time>[-\d:]+)/$', search),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

