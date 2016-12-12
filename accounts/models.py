from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# This needs to be added to settings.py as:
# AUTH_PROFILE_MODULE = 'accounts.Profile'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_confirmed=models.BooleanField(null=False, blank=False, default=False)

#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html    
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
