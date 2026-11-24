from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

from .tokens import decode_token


class CustomJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        token = auth_header.split(' ')[1]

        payload = decode_token(token)

        if payload is None:
            raise AuthenticationFailed("Invalid or expired token")

        if payload.get('token_type') != 'access':
            raise AuthenticationFailed("Access token required")

        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        return (user, None)