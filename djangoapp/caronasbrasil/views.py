from django.shortcuts import render_to_response, render
from django.http import *
from django.core.context_processors import csrf
from django.template import RequestContext
from unidecode import unidecode
from django.conf import settings

def index(request):

    data = RequestContext(request, {
        'title': 'Caronas brasil',
    })
    return render_to_response('base.html', data)