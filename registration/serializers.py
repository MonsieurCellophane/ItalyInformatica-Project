from rest_framework import serializers
from models import Registration
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    email    = serializers.EmailField()
    #password = serializers.CharField(read_only=True)
    password = serializers.SerializerMethodField(read_only=True)
    #token    = serializers.CharField(read_only=True)
    token    = serializers.SerializerMethodField(read_only=True)
    verified = serializers.DateTimeField(read_only=True)
    
    #must become verify_url etc.
    url      = serializers.URLField(read_only=True,source='get_absolute_url')

    def get_password(self, obj):
        #import ipdb; ipdb.set_trace();
        # obj.owner is the foreign key to the user model
        # if the registration has just been created
        if self.context['request'].method == 'POST' : return obj.password
        # if the user is GOD
        if self.context['request'].user.is_superuser: return obj.password
        # if the user is the owner
        if obj.owner == self.context['request'].user : return obj.password
        # else
        return ""



    def get_token(self, obj):
        #import ipdb; ipdb.set_trace();
        # obj.owner is the foreign key to the user model
        if self.context['request'].method == 'POST': return obj.token
        
        if self.context['request'].user.is_superuser or (obj.owner != self.context['request'].user) :
            return ""
        else:
            return obj.token

    def create(self, validated_data):
        #import ipdb; ipdb.set_trace();
        r=Registration()
        r.email=validated_data['email']
        r.inject_request(self.context['request'])
        r.save()
        return r
    
    class Meta:
        model = Registration
        fields = ('url', 'id', 'email','password','token','verified')


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    registration = serializers.PrimaryKeyRelatedField(many=True, queryset=Registration.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'registration')
