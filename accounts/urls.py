from django.conf.urls import url, include

from rest_framework import routers

from .views import ProfileViewSet,UserViewSet,GroupViewSet, ChangePasswordViewSet



router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users'   , UserViewSet, base_name='user')
router.register(r'groups'  , GroupViewSet)
router.register(r'chpass'  , ChangePasswordViewSet, base_name='chpass')

# Wire up our API using automatic URL routing.
# NB: DO NOT use format_suffix_patterns here: routers do that, already
urlpatterns = [
    url(r'^', include(router.urls)),
]

