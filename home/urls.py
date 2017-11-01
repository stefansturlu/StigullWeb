from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^laws/$', views.laws, name='contact'),
]
