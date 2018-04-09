from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from service.models import Service

from django.contrib import auth
from django.contrib.auth import logout
from django.template import loader, RequestContext

from django.contrib.auth.models import User
import hashlib

# Create your views here.

def index(request):

	services_db = Service.objects.all().order_by('-id')
	services = [s for s in services_db]

	return render_to_response('services.html', {'services': services, 'title': 'Services'}, RequestContext(request))


def services(request):
	services_db = Service.objects.all().order_by('-id')
	services = [s for s in services_db]

	return render_to_response('services.html', {'services': services, 'title': 'Services'}, RequestContext(request))

    # return HttpResponse("Hello, world. You're at the polls index.")


def service(request, id):

	service = Service.objects.get(id=id)

	return render_to_response('service.html', {'service': service, 'title': service.name}, RequestContext(request))






