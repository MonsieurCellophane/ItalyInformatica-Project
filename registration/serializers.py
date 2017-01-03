from rest_framework import serializers
from models import Registration
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    email    = serializers.EmailField()
    password = serializers.CharField(read_only=True)
    token    = serializers.CharField(read_only=True)
    #must become verify_url etc.
    url      = serializers.URLField(read_only=True,source='get_absolute_url')

    def create(self, validated_data):
        #import ipdb; ipdb.set_trace();
        r=Registration()
        r.email=validated_data['email']
        r.save()
        return r
    
    class Meta:
        model = Registration
        fields = ('url', 'id', 'email','password','token')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    registration = serializers.PrimaryKeyRelatedField(many=True, queryset=Registration.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'registration')
