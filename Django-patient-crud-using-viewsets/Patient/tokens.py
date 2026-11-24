import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings


def generate_access_token(user):

    payload = {
        'user_id': user.id,
        'token_type': 'access',
        'exp': datetime.now(timezone.utc) + timedelta(minutes=5),
        'iat': datetime.now(timezone.utc)
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm='HS256'
    )

    return token

def generate_refresh_token(user):
     payload = {
            'user_id': user.id,
            'token_type': 'refresh',
            'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
            'iat': datetime.now(timezone.utc)
        }
    
     token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm='HS256'
        )
    
     return token

def decode_token(token):

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None

def validate_refresh_token(token):

    payload = decode_token(token)

    if payload is None:
        return None

    if payload.get('token_type') != 'refresh':
        return None

    return payload