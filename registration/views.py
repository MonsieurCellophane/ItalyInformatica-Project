from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.exceptions import APIException, NotAcceptable

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 

from rest_framework.decorators import api_view

import time
import datetime

import logging

from .serializers import RegistrationSerializer,UserSerializer, ChangePasswordSerializer
from .models      import Registration


#
logger= logging.getLogger('IIR')
logger.debug("Logging is active")

@api_view(['GET'])
def registration_api_root(request, format=None):
    '''
    API entry point
    '''
    #import ipdb; ipdb.set_trace() 
    return Response({
        'registration-changepassword':  reverse('registration-changepassword', request=request, format=format),
        'registration-list':  reverse('registration-list', request=request, format=format),
        'registration-create': reverse('registration-create', request=request, format=format),
        'regusers'         : reverse('regusers', request=request, format=format),
        # cannot add a root for detail - the pk argument will always be missing
        #'registration-detail' : reverse('registration-detail', request=request, format=format),
    })

class RegistrationDetail(APIView):
    """
    Retrieve, update? or delete??? a registration instance
    """
    
    def get_object(self, pk, request):
        try:
            obj=Registration.objects.get(pk=pk)
            obj.inject_request(request)
            return obj
        except Registration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        registration = self.get_object(pk,request)
        serializer = RegistrationSerializer(registration,context={'request':request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # TODO user creation, ownership
        registration = self.get_object(pk,request)
        serializer = RegistrationSerializer(registration,  context={'request':request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # TODO we may not want this
        registration = self.get_object(pk,request)
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# the mixin allows creation
class RegistrationCreate(generics.CreateAPIView):
    """
    Create a registration.
    """
    serializer_class=RegistrationSerializer
    permission_classes=[]
    
# the mixin allows creation
class RegistrationList(generics.ListAPIView):
    """
    List all registrations.
    """
    serializer_class=RegistrationSerializer
    #queryset = Registration.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all registrations (for the superuser)
        or the registrations belonging to the currently authenticated user.
        """
        #import ipdb; ipdb.set_trace()
        user = self.request.user
        if user.is_anonymous(): return []
        if user.is_superuser: return Registration.objects.all()
        return Registration.objects.filter(owner=user)
    
    def list(self, request,format=None):
        queryset = self.get_queryset()
        for r in queryset: r.inject_request(request)
        serializer = RegistrationSerializer(queryset, context={'request':request}, many=True)
        return Response(serializer.data)

class RegistrationVerify(APIView):
    """
    Verify a registration
    """
    def get(self, request, pk=None, token=None, format=None):
        # TODO verification, user update
        #import ipdb; ipdb.set_trace() ;
        
        registrations = Registration.objects.filter(pk=pk,token=token)
        if len(registrations) != 1:
            raise NotAcceptable("Got wrong # of registrations (%d, should be 1)"%len(registrations))

        r0=registrations[0]
        if r0.is_verified():
            raise APIException("Do not verify registratios twice, plz")
        
        timestamp=r0.timestamp()
       
        try:
            grace_period=settings.ITINF_SETTINGS['registration_expires']
        except AttributeError:
            grace_period=604800

        if time.time()-timestamp > grace_period:
            logger.error("Stale registration! Please do something")
        else:
            r0.verified=datetime.datetime.now()
            r0._verifying=True
            
            r0.save()
        
        serializer = RegistrationSerializer(r0, context={'request':request} )
        return Response(serializer.data)



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# for reference
    #def perform_create(self, serializer):
        #import ipdb; ipdb.set_trace()
        #self.owner.save()
        #username=serializer.validated_data.get('get_username',None)
        #if serializer.validated_data.has_key('get_username'): del serializer.validated_data['get_username']
        #email=serializer.validated_data.get('get_email',None)
        #if serializer.validated_data.has_key('get_email'): del serializer.validated_data['get_email']
        #u=User(username=username,email=email,password='catafratto')
        #u.save()
        #instance=serializer.save(email=email, owner=u)
        #instance=serializer.save()

    #def post(self, request, format=None):
    #    # TODO user creation, ownership
    #    serializer = RegistrationSerializer(context={'request':request},data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#registrations = RegistrationList.as_view()
