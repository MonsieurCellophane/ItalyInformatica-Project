from rest_framework import serializers
from models import Registration
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='get_username')
    email    = serializers.EmailField(source='get_email')
    #must become verify_url etc.
    url      = serializers.URLField(read_only=True,source='get_absolute_url')
        
    class Meta:
        model = Registration
        fields = ('url', 'id', 'username','email')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    registration = serializers.PrimaryKeyRelatedField(many=True, queryset=Registration.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'registration')        
