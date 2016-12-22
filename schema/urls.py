from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import schema_view, openapi_view, swagger_view

urlpatterns = [
    url('^$', schema_view),
    url('^swagger/$', openapi_view),
    url('^swagger_view/$', swagger_view),
]

