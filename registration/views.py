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

from rest_framework.decorators import api_view

import time
import datetime

import logging

from serializers import RegistrationSerializer,UserSerializer
from models      import Registration


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
        'registration-list': reverse('registration-list', request=request, format=format),
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
        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # TODO user creation, ownership
        registration = self.get_object(pk,request)
        serializer = RegistrationSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # TODO we may not want this
        registration = self.get_object(pk,request)
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# register      = RegistrationDetail.as_view()

class RegistrationList(generics.ListCreateAPIView):
    """
    List all registrations, or create a new registration.
    """
    serializer_class=RegistrationSerializer
    queryset = Registration.objects.all()
    
    def list(self, request,format=None):
        queryset = self.get_queryset()
        for r in queryset: r.inject_request(request)
        serializer = RegistrationSerializer(queryset, context={'request':request}, many=True)
        return Response(serializer.data)

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
        
        serializer = RegistrationSerializer(r0)
        return Response(serializer.data)

# verify        = RegistrationVerify.as_view()




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
