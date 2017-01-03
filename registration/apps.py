from __future__ import unicode_literals

from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'registration'

    def ready(self):
        #import ipdb; ipdb.set_trace();
        import receivers
        
