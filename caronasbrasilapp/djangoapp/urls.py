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
    url(r'^(?P<from_city>[-\w]+)/(?P<to_city>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', search),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

