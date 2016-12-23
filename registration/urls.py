from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import registrations,register,verify, registration_api_root

urlpatterns = [
    url(r'^$', registration_api_root,name='registration-api-root'),
    url(r'^(?P<pk>[0-9]+)$'                                 , register     , name='register'     ),
    url(r'^register/$'                                      , register     , name='register'     ),
    url(r'^registrations/$'                                 , registrations, name='registrations'),
    url(r'^verify(/(?P<token>[a-fA_F0-9]+,[a-fA_F0-9]+))?/$', verify       , name='verify'       ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
