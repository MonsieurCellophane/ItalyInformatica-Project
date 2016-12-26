from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from rest_framework.reverse  import reverse, reverse_lazy




def password_default(N=8):
    """
    Random string for registration passwords
    """
    return (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits+string.lowercase) for _ in range(N)))

model_urlpattern_name='registration-detail'

@python_2_unicode_compatible
class Registration(models.Model):
    """
    Records a registration request
    """
    created  = models.DateTimeField(auto_now_add=True)
    verified = models.DateTimeField(null=True)
    owner=models.ForeignKey('auth.User', related_name='registration', on_delete=models.CASCADE)
    token = models.TextField()
    password = models.TextField(default='password_default')
    email = models.EmailField(null=True)
    
    def is_verified(self): return self.verified is not None

    #http://stackoverflow.com/questions/17898994/how-to-use-request-get-in-django-models
    def inject_request(self,request):
        self.request=request
        
    def get_username(self):
        if self.owner:
            return self.owner.username
        return None

    def get_email(self):
        if self.owner:
            return self.owner.email
        return self.email

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
        # maybe do something clever
        super(Registration, self).save(*args, **kwargs)

    def __str__(self):
        o="NULL"
        if self.owner: o=self.owner.username
        return o
        
    class Meta:
        ordering = ('created',)
