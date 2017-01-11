from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import registration_api_root# , registrations #,register,verify, 
import views

#ALF: ACHTUNG! look in models.py, since the get_absolute_url method must match this.
urlpatterns = [
    url(r'^$', views.registration_api_root,name='registration-api-root'),
    url(r'^list/$',views.RegistrationList.as_view(), name='registration-list'),
    url(r'^create/$',views.RegistrationCreate.as_view(), name='registration-create'),
    url('^view/(?P<pk>[0-9]+)/$',views.RegistrationDetail.as_view(), name='registration-detail'),
    url('^verify/(?P<pk>[0-9]+)/(?P<token>[a-zA-Z0-9,=]+)$',views.RegistrationVerify.as_view(), name='registration-verify'),
#    url(r'^users/$', views.UserList.as_view(),name="regusers"),
#    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='reguser-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
