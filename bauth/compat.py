from django.contrib.auth import get_user_model

from rest_framework import serializers

import hashlib
import hmac
import base64
import string
import random
import simplejson as json

import time

from django.conf import settings

class Serializer(serializers.Serializer):
    @property
    def object(self):
        return self.validated_data


class PasswordField(serializers.CharField):

    def __init__(self, *args, **kwargs):
        if 'style' not in kwargs:
            kwargs['style'] = {'input_type': 'password'}
        else:
            kwargs['style']['input_type'] = 'password'
        super(PasswordField, self).__init__(*args, **kwargs)


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


def session_key(N=16):
    """Return a string"""
    return (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits+string.lowercase) for _ in range(N)))

def encode_secret():
    """Return a systemwide fixed secret"""
    #TODO: Read from settings
    return "Trullallero lero la"

def encoded_payload(username):
    """Return encoded payload"""
    pl={'username':username,'time':str(time.time()),'sessionkey':session_key()}
    # or use base64
    return (simplejson.dumps(pl)).encode('hex')

def decoded_payload(pl):
    """Return decoded payload"""
    # or use base64
    try:
        return (simplejson.loads(pl.decode('hex')))
    except ValueError:
        return None
    except TypeError:
        return None
    

def encode_hmac(pl):
    return hmac.new(encode_secret(),pl,hashlib.sha256).hexdigest()
    
def encode_handler(username):
    """Returns an encoded token"""
    pl=encoded_payload(username)
    return "%s,%s"%(encode_hmac(pl),pl)

def verify_handler(token):
    try:
        (mac,pl)=token.split(',')
    except ValueError:
        return None
    
    if mac != encode_hmac(pl): return None
    return decoded_payload(pl)

