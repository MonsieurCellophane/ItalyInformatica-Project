from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


# Ensure users have profile.
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

@receiver(pre_delete, sender=User)
def stash_user_profile(sender, instance, **kwargs):
    # consider creating a stashed user+profile object here
    # also see the on_delete value specified on Profile.
    pass

