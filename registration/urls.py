from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from views import registration_api_root# , registrations #,register,verify, 
import views

#ALF: ACHTUNG! look in models.py, since the get_absolute_url method must match this.
urlpatterns = [
    url(r'^$', views.registration_api_root,name='registration-api-root'),
    url(r'^registrarations/chpass/',views.ChangePasswordView.as_view(), name='registration-changepassword'),
    url(r'^registrations/$',views.RegistrationList.as_view(), name='registration-list'),
    url(r'^registrations/create/$',views.RegistrationCreate.as_view(), name='registration-create'),
    url('^registrations/(?P<pk>[0-9]+)/$',views.RegistrationDetail.as_view(), name='registration-detail'),
    url('^registrations/(?P<pk>[0-9]+)/(?P<token>[a-zA-Z0-9,=]+)/verify/$',views.RegistrationVerify.as_view(), name='registration-verify'),
    url(r'^regusers/$', views.UserList.as_view(),name="regusers"),
    url(r'^regusers/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='reguser-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
