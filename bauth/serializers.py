from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from rest_framework import serializers
from compat import  encode_handler,verify_handler


#Get django user model
# -- too cute for now.
####User=get_user_model()



def get_username_field():
    try:
        username_field = get_user_model().USERNAME_FIELD
    except:
        username_field = 'username'

    return username_field


def get_username(user):
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return username

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # The following:
        #fields = ('url', 'username', 'email')
        # gives:
        #AssertionError: `HyperlinkedIdentityField` requires the request in the serializer context.
        # Add `context={'request': request}` when instantiating the serializer.
        # So need to figure out how to add request to context, as in:
        # 
        #serializer_context = {
        #    'request': Request(request),
        # }
        # p = Person.objects.first()
        # s = PersonSerializer(instance=p, context=serializer_context)
        # If context is given as above, it then tries to establish some form of relationshiop giving:
        #     Could not resolve URL for hyperlinked relationship using view name "user-detail".
        #     You may have failed to include the related model in your API, or incorrectly configured the
        #     `lookup_field` attribute on this field.
        # For now, omit url
        fields = ('username', 'email')
        
class PasswordField(serializers.CharField):

    def __init__(self, *args, **kwargs):
        if 'style' not in kwargs:
            kwargs['style'] = {'input_type': 'password'}
        else:
            kwargs['style']['input_type'] = 'password'
        super(PasswordField, self).__init__(*args, **kwargs)

class BaseSerializer(serializers.Serializer):
    @property
    def object(self):
        return self.validated_data
    
    def response_payload_handler(self,token,user=None,request=None):
        """
        Returns the response data for the login view (and maybe some others).
        May be extended to return serialized user, profile..
        """
        return {
            'token': token,
        }



class TokenSerializer(BaseSerializer):
    """
    Serializer class used to validate a username and password.
    Returns a Token that can be used to authenticate later calls.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Add username, password to self.fields.
        """
        super(TokenSerializer, self).__init__(*args, **kwargs)

        self.fields['username'] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password'),
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)
                # convenience attrs.
                self.user=user
                self.token=encode_handler(credentials['username'])
                return {
                    'token': self.token,
                    'user': self.user
                }
            else:
                msg = 'Unable to login with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

class VerifyTokenSerializer(BaseSerializer):
    """
    Serializer used for verifying tokens.
    """
    token = serializers.CharField()
    #TODO: check token freshness
    def validate(self, attrs):
        #convenience
        self.token = attrs['token']
        self._check_payload(token=self.token)
        if self.payload is None: return None
        #convenience
        self.user = self._check_user(payload=self.payload)

        return {
            'token': self.token,
            'user' : self.user
        }

    def _check_payload(self,token):
        self.payload=verify_handler(token)
        

    def _check_user(self,payload):
        try:
            username=payload['username']
        except KeyError:
            msg="Invalid payload"
            raise serializers.ValidationError(msg)

        # Make sure user exists
        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _("User doesn't exist.")
            raise serializers.ValidationError(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise serializers.ValidationError(msg)

        return user
    
    def response_payload_handler(self,token,user=None,request=None):
        """
        Returns the response data for the login view (and maybe some others).
        May be extended to return serialized user, profile..
        """
        retval={
            'token': token,
        }
        pl=verify_handler(token)
        retval['timestamp']=pl.get('timestamp')
            
        if user is not None: retval['user']=UserSerializer(instance=user, context=self.context).data
        return retval 
    
