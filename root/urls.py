from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^private/$', views.private, name='private'),
    url(r'^accounts/login/$', auth_views.login),
]


