#! /usr/bin/env python

import prolog
import os
# don't need this
#s=__import__( os.environ["DJANGO_SETTINGS_MODULE"])
#s=s.settings
from django.conf import settings
from django.apps import apps


#[ app for app in settings.INSTALLED_APPS if not "django" in app ]
#for app in settings.INSTALLED_APPS:  print(app)
for a in apps.all_models.keys():  print(a)


