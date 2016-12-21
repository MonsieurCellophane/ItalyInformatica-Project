from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions as rfp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from accounts.serializers import ProfileSerializer, UserSerializer, GroupSerializer
from accounts.permissions import IsOwnerOrReadOnly
from accounts.permissions import IsAdminOrReadOnly
from accounts.models      import Profile


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
        'ptofiles' : reverse('profile-list', request=request, format=format),
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
    permission_classes = (rfp.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (rfp.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (rfp.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)
