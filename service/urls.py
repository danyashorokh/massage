from django.conf.urls import url, include

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views

urlpatterns = [
#   url(r'^', views.index),
#   url(r'^services/(\w+)', views.service),
	url(r'find\/?$', views.find),
]