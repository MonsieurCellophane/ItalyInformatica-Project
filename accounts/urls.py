from django.conf.urls import url, include
from rest_framework import routers

from accounts.views import ProfileViewSet,UserViewSet,GroupViewSet



router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users'   , UserViewSet)
router.register(r'groups'  , GroupViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]
