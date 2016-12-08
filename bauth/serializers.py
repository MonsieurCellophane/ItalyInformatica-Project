from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username_field, PasswordField
from compat import Serializer,get_username_field, PasswordField, verify_handler, encode_handler,verify_handler


class TokenSerializer(Serializer):
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

                return {
                    'token': encode_handler(credentials['username']),
                    'user': user
                }
            else:
                msg = 'Unable to login with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

class VerificationSerializer(Serializer):
    """
    Serializer used for verifying tokens.
    """
    token = serializers.CharField()
    #TODO: check token freshness
    def validate(self, attrs):
        token = attrs['token']
        self._check_payload(token=token)
        if self.payload is None: return False
        user = self._check_user(payload=payload)

        return {
            'token': token,
            'user': user
        }

    def _check_payload(self,token):
        self.payload=verify_handler(token)
        

    def _check_user(self):
        try:
            username=self.payload('username')
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
    
