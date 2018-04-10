"""massage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^services/$', views.services),
    url(r'^services/(\w+)', views.service),

    url(r'^history/$', views.history),
    url(r'^contacts/$', views.history),
    url(r'^promo/$', views.promo),

    url(r'^not_found\/?$', views.not_found),

    url(r'^service\/?', include('service.urls')),



    # url(r'^service/(\w+)$', views.service),
  
]

urlpatterns.append(url(r'^.*$', views.page404))
