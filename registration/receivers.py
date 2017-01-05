from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from rest_framework.exceptions import APIException

from models import Registration
from django.core.mail import send_mail



@receiver(post_save, sender=Registration)
def send_registration_handle(sender, instance, **kwargs):
    """
    Sends user a validation link
    """
    #import ipdb; ipdb.set_trace()
    url=instance.get_absolute_url()
    url.rstrip('/')
    try:
        send_mail(
            'Registration to ItalyInformaticaProject',
            "Please click on the link to validate your registration:%s/%s"%(url.rstrip('/'),instance.token),
            'noreply@glass.org',
            [instance.owner.email],
            fail_silently=False,
            )
    except Exception as e:
        instance.owner.delete()
        raise APIException("Cannot send email notification:%s"%repr(e))

            

