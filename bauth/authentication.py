from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from utils import verify_handler

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_X_TOKEN')
        if not token:
            return None

        pl=verify_handler(token)
        
        if not pl:
            return None

        #import pdb; pdb.set_trace()
        
        try:
            user = User.objects.get(username=pl.get('username'))
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
