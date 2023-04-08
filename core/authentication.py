from telnetlib import STATUS
import jwt , datetime
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed,NotAuthenticated
from rest_framework.authentication import get_authorization_header
from rest_framework import status

from .models import User

class JwtAuthenticationOrReadOnly(BaseAuthentication):
    def authenticate(self, request):
        if request.method == 'GET':
            return

        auth = get_authorization_header(request).split()
        
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')

            id = decode_access_token(token)
            user = User.objects.get(id=id)
            return (user, AuthenticationFailed)

        raise AuthenticationFailed('Unauthenticated')

    def authenticate_header(self, request):
        return 'Bearer realm="api"'

class JwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        print(get_authorization_header(request))
        
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')

            id = decode_access_token(token)
            user = User.objects.get(id=id)
            return (user, AuthenticationFailed)

        raise AuthenticationFailed('Unauthenticated')

    def authenticate_header(self, request):
        return 'Bearer realm="api"'

def create_access_token(id):
    return jwt.encode({
        'user_id':id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
        'iat': datetime.datetime.utcnow()
    },'access_secret',algorithm='HS256') 

def decode_access_token(token):
    try:
        payload = jwt.decode(
            token,
            'access_secret',
            algorithms='HS256') 

        return payload['user_id']
    except:
        raise AuthenticationFailed('unauthenticated')

def create_refresh_token(id):
    return jwt.encode({
        'user_id':id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    },'refresh_secret',algorithm='HS256')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(
            token,
            'refresh_secret',
            algorithms='HS256') 
        return payload['user_id']

    except Exception as e:
        raise AuthenticationFailed('unauthenticated')