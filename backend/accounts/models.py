from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# This needs to be added to settings.py as:
# AUTH_PROFILE_MODULE = 'accounts.Profile'
class Profile(models.Model):
    """
    Holds user details, preferences etc.
    """
    # See https://docs.djangoproject.com/en/1.10/ref/models/fields/
    # for other on_delete possible values.
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_confirmed=models.BooleanField(null=False, blank=False, default=False)
    is_deleted=models.BooleanField(null=False, blank=False, default=False)
    #
    def __iter__(self):
        """
        this iterator allows the idiom:

        for field, val in obj:
            do_something

        credits http://stackoverflow.com/questions/3106295/django-get-list-of-model-fields
        """
        for field in Profile._meta.get_fields():
            value = getattr(self, field.name, None)
            yield (field.name, value)
    
    def __str__(self):
        return "PROF_%s"%repr(self.id)
