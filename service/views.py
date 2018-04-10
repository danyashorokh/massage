from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from service.models import Service

from django.contrib import auth
from django.contrib.auth import logout
from django.template import loader, RequestContext

import hashlib
from massage.views import *

# Create your views here.


def find(request):
    if request.GET and 'find' in request.GET and request.GET['find'] != '':

        try:
            if int(request.GET['find']):
                try:
                    id = Service.objects.filter(id=int(request.GET['find']))[0].id
                except:
                    return redirect('/not_found/')
                return redirect('/services/' + str(id))
        
        except:

            service = 0

            for i in Service.objects.all().order_by('name'):

                if i.name.lower().find(request.GET['find'].lower()) != -1 or i.description.lower().find(request.GET['find'].lower()) != -1:
                    service = i
                    break

            if service:
            	return redirect('/services/' + str(service.id))
            else:
            	return redirect('/not_found/')


    else:
        return page404(request)







