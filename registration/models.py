from __future__ import unicode_literals

from django.db import models

from rest_framework.reverse  import reverse


def password_default(N=8):
    """
    Random string for registration passwords
    """
    return (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits+string.lowercase) for _ in range(N)))

class Registration(models.Model):
    """
    Records a registration request
    """
    created  = models.DateTimeField(auto_now_add=True)
    verified = models.DateTimeField(null=True)
    owner=models.ForeignKey('auth.User', related_name='registration', on_delete=models.CASCADE)
    token = models.TextField()
    password = models.TextField(default='password_default')
    
    def is_verified(self): return self.verified is not None

    def get_absolute_url(self):
        return reverse( 'register_request', args=[str(self.token)])
    
    def save(self, *args, **kwargs):
        # maybe do something clever
        super(Snippet, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('created',)
