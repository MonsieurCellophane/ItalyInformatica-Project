from __future__ import unicode_literals

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name="Accounts for the /r/italyinformatica project"
    def ready(self):
        #import ipdb; ipdb.set_trace();
        import receivers
