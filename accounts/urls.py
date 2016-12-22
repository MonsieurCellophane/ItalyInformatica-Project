from django.conf.urls import url, include
from rest_framework import routers

from accounts.views import ProfileViewSet,UserViewSet,GroupViewSet
from accounts.views import schema_view, openapi_view, swagger_view



router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users'   , UserViewSet)
router.register(r'groups'  , GroupViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url('^schema/$', schema_view),
    url('^swagger/$', openapi_view),
    url('^swagger_view/$', swagger_view),
    url(r'^', include(router.urls)),
]
