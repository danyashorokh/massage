from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from service.models import Service

from django.contrib import auth
from django.contrib.auth import logout
from django.template import loader, RequestContext

import hashlib

# Create your views here.

def index(request):

	services_db = Service.objects.all().order_by('-id')
	services = [s for s in services_db]

	return render_to_response('services.html', {'title': 'Services', 'services1': services}, RequestContext(request))

# http://itman.in/django-404/
def page404(request):

	return render_to_response('404.html', {'title': 'Ошибка'}, RequestContext(request))

def not_found(request):

	return render_to_response('not_found.html', {'title': 'Ошибка'}, RequestContext(request))


def services(request):
	services_db = Service.objects.all().order_by('-id')
	services = [s for s in services_db]

	return render_to_response('services.html', {'title': 'Services', 'services': services, 'active':'services'}, RequestContext(request))

    # return HttpResponse("Hello, world. You're at the polls index.")


def service(request, id):

	service = Service.objects.get(id=id)

	return render_to_response('service.html', {'title': service.name, 'service': service}, RequestContext(request))


def history(request):
    return render_to_response('history.html', {'title': 'History', 'active':'history'}, RequestContext(request))


def contacts(request):
    return render_to_response('contacts.html', {'title': 'History', 'active':'contacts'}, RequestContext(request))


def promo(request):
    return render_to_response('promo.html', {'title': 'History', 'active':'promo'}, RequestContext(request))






