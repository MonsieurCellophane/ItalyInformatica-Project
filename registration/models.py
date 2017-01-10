from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User

from rest_framework.reverse  import reverse, reverse_lazy
from rest_framework.exceptions import APIException, NotAcceptable
import random
import string

from .utils import password_default, encode_handler, verify_handler


model_urlpattern_name='registration-detail'

@python_2_unicode_compatible
class Registration(models.Model):
    """
    Records a registration request
    """
    created  = models.DateTimeField(auto_now_add=True)
    verified = models.DateTimeField(null=True)
    owner=models.ForeignKey('auth.User', related_name='registration', on_delete=models.CASCADE)
    token = models.TextField(default=None)
    password = models.TextField(default=password_default)
    _email=None
    _verifying=False # will be set to True during verification. See views
    
    def is_verified(self): return self.verified is not None

    def is_valid(self):
        pl=verify_handler(self.token)
        return pl is not None

    def timestamp(self):
        pl=verify_handler(self.token)
        if pl is None:
            raise APIException("Invalid token")
        
        return float(pl['timestamp'])

    def payload(self): return verify_handler(self.token)
    
    #http://stackoverflow.com/questions/17898994/how-to-use-request-get-in-django-models
    def inject_request(self,request):
        self.request=request

    @property
    def email(self):
        if self.owner_id:
            return self.owner.email
        else:
            return self._email


    @email.setter
    def email(self,value):
        #import ipdb; ipdb.set_trace()
        #if self._verifying: return     # disregard attempt
        if self.pk:
            raise NotAcceptable("cannot update email on saved registrations")
        
        if self.owner_id:
            raise NotAcceptable("Registration owner already set")

        else:
            try:
                u=User.objects.get(username=value)
                raise NotAcceptable("Address already registered")
            except User.DoesNotExist:
                self._email=value

    #todo transform it in verify url
    def get_absolute_url(self):
       
        #import ipdb; ipdb.set_trace()
        #must return a valid URL - right now it does not
        #or x = getattr(self, 'attr', sentinel)
        try:
            r=self.request
        except AttributeError:
            r=None
            
        #return reverse( model_urlpattern_name, request=r, args=[str(self.token)])
        return reverse_lazy( model_urlpattern_name, request=r, args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        #if verifying, just do it
        if self._verifying:
            super(Registration, self).save(*args, **kwargs)
            return
            
        if self.pk:
            raise NotAcceptable("cannot update saved registrations")
        try:
            u=User.objects.get(username=self._email)
            raise NotAcceptable("Address already registered")
        except User.DoesNotExist:
                u=User(username=self._email,email=self._email,password=self.password)
                u.save()
                self.owner=u
                self.owner_id=self.owner.id
                
        # maybe do something clever
        self.token=encode_handler(self._email)
        #further actions in receivers
        super(Registration, self).save(*args, **kwargs)

    def __str__(self):
        o=self._email
        if o is None: o=self.email
        return repr(o)
        
    class Meta:
        ordering = ('created',)
