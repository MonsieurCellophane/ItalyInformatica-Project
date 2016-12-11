from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^token/$', views.obtain_token),
    url(r'^verify(/(?P<token>[a-fA_F0-9]+,[a-fA_F0-9]+))?/$', views.verify_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
