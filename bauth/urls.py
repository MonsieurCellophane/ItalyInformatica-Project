from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import obtain_token, verify_token
from views import schema_view, openapi_view, swagger_view

urlpatterns = [
    url('^schema/$', schema_view),
    url('^swagger/$', openapi_view),
    url('^swagger_view/$', swagger_view),
    url(r'^token/$', obtain_token),
    url(r'^verify(/(?P<token>[a-fA_F0-9]+,[a-fA_F0-9]+))?/$', verify_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
