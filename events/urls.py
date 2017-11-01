from django.conf.urls import url, include
from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail' ),
    url(r'^(?P<pk>\d+)/skraning/$', views.event_add_attendance, name='event_add_attendance' ),
    url(r'^(?P<pk>\d+)/afskraning/$', views.event_cancel_attendance, name='event_cancel_attendance' ),

]
