from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
from service.models import Service

from django.contrib import auth
from django.contrib.auth import logout
from django.template import loader, RequestContext

from django.contrib.auth.models import User
import hashlib

# Create your views here.







