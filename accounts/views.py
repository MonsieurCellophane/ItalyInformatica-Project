from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions  import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from .serializers import ProfileSerializer, UserSerializer, GroupSerializer, ChangePasswordSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .models      import Profile


#
@api_view(['GET'])
def api_root(request, format=None):
    '''
    API entry point
    '''
    #user-list etc. are authomatic names that routers give to views
    return Response({
        'users'    : reverse('user-list'   , request=request, format=format),
        'groups'   : reverse('group-list'  , request=request, format=format),
        'profiles' : reverse('profile-list', request=request, format=format),
        'chpass'   : reverse('ac-chpass'   , request=request, format=format),
    })

class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Provides `retrieve`,`create`,`list`,`update` for profiles.
    Profiles cannot be deleted for extant users (see the admin interface 
    for special needs). Nor can they be created (see the create* receivers)
    Access is readonly except for owner.
    """
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)

#as view
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


class ChangePasswordViewSet(viewsets.ViewSet):
    """
    An endpoint for changing password.
    """
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def create(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data,context={'request':request,})

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs): return self.create(request, *args, **kwargs)
