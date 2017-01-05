from rest_framework import status
from rest_framework.authentication import SessionAuthentication

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.reverse import reverse
from rest_framework.views import APIView

from serializers import TokenSerializer, VerifyTokenSerializer
from authentication import TokenAuthentication
from utils import verify_handler

#
@api_view(['GET'])
def api_root(request, format=None):
    '''
    API entry point
    '''
    #import ipdb; ipdb.set_trace() 
    return Response({
        'obtain-token'   : reverse('obtain-token'   , request=request, format=format),
        'verify-token'   : reverse('verify-token'   , request=request, format=format),
    })

class TokenAPIView(APIView):
    """
    Base API View
    """
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'view': self,
        }

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__)
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get(self, request, *args, **kwargs):return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, *args, **kwargs):
        """
        Handles post requests, passing incoming data to own serializer.
        The serializer checks incomng data and (if valid) will return the 
        needed payload, based on the token.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            # TODO: yes, this is silly
            response_data = serializer.response_payload_handler(token, user, request)

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainToken(TokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a Token that can be used for authenticated requests.
    """
    serializer_class = TokenSerializer



class VerifyToken(TokenAPIView):
    """
    API View that checks the veracity of a token, returning the token if it
    is valid.
    """
    serializer_class = VerifyTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = serializer.response_payload_handler(token, user, request)

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

obtain_token = ObtainToken.as_view()
verify_token = VerifyToken.as_view()

