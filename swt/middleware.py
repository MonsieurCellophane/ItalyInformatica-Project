from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import ImproperlyConfigured
from django.contrib import auth

from rest_framework import exceptions

from .authentication import TokenAuthentication

class SWTAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware for utilizing SimpleWebToken authentication.

    If request.user is not authenticated, then this middleware attempts to
    authenticate the username passed with the token in the appropriate header
    If authentication is successful, the user is automatically logged in to
    persist the user in the session.
    """

    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Django simple web token auth middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the SimpleWebTokenMiddleware class.")

        #Already authenticated
        if request.user.is_authenticated:
            if request.user.get_username() == self.clean_username(username, request):
                return

        # Attempt authentication
        (user,backend) = (None,None)
        tokenauth=TokenAuthentication()
        try:
            authcred=tokenauth.authenticate(request)
            if authcred is None: return 
        except exceptions.AuthenticationFailed:
            return 

        (user,backend) = authcred
        if user:
            # User is valid.  Set request.user and persist user in the session
            # by logging the user in.
            request.user = user
            auth.login(request, user, backend=backend)
