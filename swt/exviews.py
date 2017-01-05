from django.utils.decorators import classonlymethod

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .authentication import TokenAuthentication


class AuthenticatedView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    # do not put this in the schema
    exclude_from_schema = True

    # def __init__(self,*args,**kwargs):
    #     import ipdb; ipdb.set_trace()
    #     return super(APIView,self).__init__(*args,**kwargs)
    
    def get(self, request, format=None):
        #import ipdb; ipdb.set_trace()
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

    # @classonlymethod
    # def as_view(cls,**initkwargs):
    #     import ipdb; ipdb.set_trace()
    #     return super(APIView,cls).as_view(**initkwargs)
