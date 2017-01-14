from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^weddingparty/$', views.wp, name='wp'),
    url(r'^travel/$', views.travel, name='travel'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^rsvp/$', views.rsvp_page, name='rsvp'),
    url(r'^info/', views.info, name='info'),
]
