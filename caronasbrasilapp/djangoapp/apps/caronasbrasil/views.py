# coding=utf-8
from datetime import datetime
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render, redirect
from django.http import *
from django.core.context_processors import csrf
from django.template import RequestContext
# from social.backends.facebook import FacebookAppOAuth2
from unidecode import unidecode
from django.conf import settings
from djangoapp.apps.caronasbrasil.main_controller import MainController
from djangoapp.apps.caronasbrasil.model.fb_groups.fb_groups_controller import FBGroupsController
from djangoapp.apps.caronasbrasil.persistence_controller import PersistenceController


def my_render(request, template, data):
    ## default variables
    data.update({
        'title_site': 'Vai de Carona',
    })
    return render(request, template, data)

def index(request):
    return my_render(request, 'index.html',
        {
            'caronas': PersistenceController().get_carona_paths(),
            'from_city': 'sao carlos',
            'from_state': 'SP',
        }
    )


def last(request):
    return my_render(request, 'last.html',
        {
            'title': 'Ultimas caronas adicionadas ao sistema',
            'results': PersistenceController().get_last(),
        }
    )

def next_days(request):
    return my_render(request, 'next_days.html',
        {
            'title': 'Caronas nos proximos dias',
            'results_by_day': PersistenceController().get_next_days(),
        }
    )

def carona_info(request, carona_id):
    carona = PersistenceController().get_carona_info(carona_id)
    comments = FBGroupsController(carona.fb_group_id).get_comments(carona.fb_post_id)
    carona.comments =  comments
    return my_render(request,'carona_info.html',
        {
            'title': u'Informação sobre a carona',
            'result': carona,
        }
    )

def search(request, op, from_city, to_city, date, from_time, to_time):

    ##todo validar parametros
    from_city_index = from_city.rfind('-')
    from_city, from_city_state = from_city[:from_city_index], from_city[from_city_index+1:]
    to_city_index = to_city.rfind('-')
    to_city, to_city_state = to_city[:to_city_index], to_city[to_city_index+1:]

    ## TODO
    ## restrictions
    if len(to_city_state)!=2 or len(from_city_state) != 2:
        return
    ## to_time > from_time
    ## date > today



    ## preprocessing
    from_city = from_city.replace('-', ' ').lower()
    to_city = to_city.replace('-', ' ').lower()
    from_city_state = from_city_state.upper()
    to_city_state = to_city_state.upper()
    ofereco_procuro = 'o' if op[0] == 'p' else 'p'
    ## Ex: '2013-10-15 18:00'
    from_datetime = datetime.strptime(date+from_time, "%Y-%m-%d%H:%M")
    to_datetime = datetime.strptime(date+to_time, "%Y-%m-%d%H:%M")


    results  = PersistenceController().search_carona(**{
        'ofereco_procuro': ofereco_procuro,
        'from_city' : from_city,
        'from_city_state' : from_city_state,
        'to_city' : to_city,
        'to_city_state' : to_city_state,
        'from_datetime': from_datetime,
        'to_datetime': to_datetime,
    })

    return my_render(request, 'results.html',
        {
            'title': 'Buscar procurar oferecer - Caronas brasil',
            'results': results,
        }
    )

#
# @login_required
# def done(request):
#     """Login complete view, displays user data"""
#     scope = ' '.join(FacebookAppOAuth2.DEFAULT_SCOPE)
#     print scope
#     return render_to_response('index.html', {
#         'user': request.user,
#         'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
#         'plus_scope': scope
#     }, RequestContext(request))
#
#
# def signup_email(request):
#     return render_to_response('email_signup.html', {}, RequestContext(request))
#
#
# def validation_sent(request):
#     return render_to_response('validation_sent.html', {
#         'email': request.session.get('email_validation_address')
#     }, RequestContext(request))
#
#
# def require_email(request):
#     if request.method == 'POST':
#         request.session['saved_email'] = request.POST.get('email')
#         backend = request.session['partial_pipeline']['backend']
#         return redirect('social:complete', backend=backend)
#     return render_to_response('email.html', RequestContext(request))