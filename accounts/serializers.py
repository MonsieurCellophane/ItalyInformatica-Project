from django.contrib.auth.models import User, Group

from rest_framework import serializers

from accounts.models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #username=serializers.ReadOnlyField()
    #profile=serializers.ReadOnlyField()
    #groups=serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'profile', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for user profiles
    """
    owner        = serializers.ReadOnlyField(source='owner.username')
    is_confirmed = serializers.ReadOnlyField()
    is_deleted   = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields='__all__'
        #exclude=['is_confirmed']
        #fields = ('url', 'id', 'owner',
        #          'location', 'bio', 'birth_date', 'is_confirmed')

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

