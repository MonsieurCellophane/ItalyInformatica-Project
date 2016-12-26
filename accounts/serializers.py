from django.contrib.auth.models import User, Group

from rest_framework import serializers

from accounts.models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
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
    is_confirmed = serializers.ReadOnlyField() # (source='is_confirmed') gives a 'redundant' exception

    class Meta:
        model = Profile
        fields = ('url', 'id', 'owner',
                  'location', 'bio', 'birth_date', 'is_confirmed')
