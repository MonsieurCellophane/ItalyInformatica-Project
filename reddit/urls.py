"""reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
import views


urlpatterns = [
    url(r'^test/', views.AuthenticatedView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)

# Use append - cannot be put above, format_suffix_patterns bombs if we do it.
urlpatterns.append(url(r'^', include('root.urls')))
# Admin site
urlpatterns.append(url(r'^admin/', admin.site.urls))
# API - auth
urlpatterns.append(url(r'^api/auth/', include('bauth.urls')))
# API - accounts
urlpatterns.append(url(r'^api/accounts/', include('accounts.urls')))
# API - schema
urlpatterns.append(url(r'^api/schema/', include('schema.urls')))


