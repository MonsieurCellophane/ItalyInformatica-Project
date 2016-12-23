from rest_framework import serializers
from models import Registration
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField()
    email    = serializers.EmailField()   
    url      = serializers.URLField(read_only=True,source='get_absolute_url')
    
    class Meta:
        model = Registration
        fields = ('url', 'id', 'username',)

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Registration.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'registration')        
