"""StigullWeb URL Configuration

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
from django.conf.urls import include, url #bætti include til að herma eftir tutoriali
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon/favicon.ico', permanent=True)

#from myapp import views as v
from home import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete 
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^events/', include('events.urls')),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout),
    url(r'^changepwd/$', auth_views.password_change),

    url(r'^favicon\.ico$', favicon_view),
    #url(r'^boots/$', v.index),

    # Email url til að resetta password
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
]

#urlpatterns += staticfiles_urlpatterns()
