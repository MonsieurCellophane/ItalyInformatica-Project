from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import authentication
from rest_framework import exceptions
from utils import verify_handler


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        #import ipdb; ipdb.set_trace()
        try:
            header=settings.ITINF_SETTINGS['token_header']
        except AttributeError:
            header='HTTP_X_TOKEN'

        token = request.META.get(header)
        if not token:
            return None

        pl=verify_handler(token)
        
        if not pl:
            return None

        
        try:
            user = User.objects.get(username=pl.get('username'))
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, pl['auth'])

    def get_user(self, user_id):
        #import ipdb; ipdb.set_trace()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
    

    
