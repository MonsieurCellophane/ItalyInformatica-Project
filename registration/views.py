from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view

from bauth.utils import verify_handler
from serializers import RegistrationSerializer
from models      import Registration
#
@api_view(['GET'])
def registration_api_root(request, format=None):
    '''
    API entry point
    '''
    #import ipdb; ipdb.set_trace() 
    return Response({
        'register'      : reverse('register'     , request=request, format=format),
        'registrations' : reverse('registrations', request=request, format=format),
        'verify'        : reverse('verify'       , request=request, format=format),
    })

class RegistrationDetail(APIView):
    """
    Retrieve, update? or delete??? a registration instance
    """
    def get_object(self, pk):
        try:
            return Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        registration = self.get_object(pk)
        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # TODO user creation, ownership
        registration = self.get_object(pk)
        serializer = RegistrationSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # TODO we may not want this
        registration = self.get_object(pk)
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegistrationList(APIView):
    """
    List all registrations, or create a new registration.
    """
    def get(self, request, format=None,):
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO user creation, ownership
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationVerify(APIView):
    """
    Verify a registration
    """
    def get(self, request, format=None):
        # TODO verification, user update
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)



register      = RegistrationDetail.as_view()
registrations = RegistrationList.as_view()
verify        = RegistrationVerify.as_view()

# class RegistrationView(APIView):
#     pass

# class VerifyRegistrationView(APIView):
#     pass

# class TokenAPIView(APIView):
#     """
#     Base API View
#     """
#     permission_classes = ()
#     authentication_classes = ()

#     def get_serializer_context(self):
#         """
#         Extra context provided to the serializer class.
#         """
#         return {
#             'request': self.request,
#             'view': self,
#         }

#     def get_serializer_class(self):
#         """
#         Return the class to use for the serializer.
#         Defaults to using `self.serializer_class`.
#         You may want to override this if you need to provide different
#         serializations depending on the incoming request.
#         (Eg. admins get full serialization, others get basic serialization)
#         """
#         assert self.serializer_class is not None, (
#             "'%s' should either include a `serializer_class` attribute, "
#             "or override the `get_serializer_class()` method."
#             % self.__class__.__name__)
#         return self.serializer_class

#     def get_serializer(self, *args, **kwargs):
#         """
#         Return the serializer instance that should be used for validating and
#         deserializing input, and for serializing output.
#         """
#         serializer_class = self.get_serializer_class()
#         kwargs['context'] = self.get_serializer_context()
#         return serializer_class(*args, **kwargs)

#     def get(self, request, *args, **kwargs):return Response(None, status=status.HTTP_204_NO_CONTENT)
    
#     def post(self, request, *args, **kwargs):
#         """
#         Handles post requests, passing incoming data to own serializer.
#         The serializer checks incomng data and (if valid) will return the 
#         needed payload, based on the token.
#         """
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.object.get('user') or request.user
#             token = serializer.object.get('token')
#             # TODO: yes, this is silly
#             response_data = serializer.response_payload_handler(token, user, request)

#             return Response(response_data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ObtainToken(TokenAPIView):
#     """
#     API View that receives a POST with a user's username and password.

#     Returns a Token that can be used for authenticated requests.
#     """
#     serializer_class = TokenSerializer



# class VerifyToken(TokenAPIView):
#     """
#     API View that checks the veracity of a token, returning the token if it
#     is valid.
#     """
#     serializer_class = VerifyTokenSerializer
    
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.object.get('user') or request.user
#             token = serializer.object.get('token')
#             response_data = serializer.response_payload_handler(token, user, request)

#             return Response(response_data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


