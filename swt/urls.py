from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import obtain_token, verify_token, api_root

urlpatterns = [
    url(r'^$', api_root,name='api-root'),
    url(r'^token/$', obtain_token,name='obtain-token'),
    url(r'^verify(/(?P<token>[a-fA_F0-9]+,[a-fA_F0-9]+))?/$', verify_token,name='verify-token'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
