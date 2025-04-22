import jwt
import os
import datetime
from functools import wraps
from flask import request, jsonify


JWT_SECRET = os.getenv("JWT_SECRET")
JWT_EXPIRY_SECONDS = int(os.getenv("JWT_EXPIRY_SECONDS", 3600))

def generate_token(username,user_id):
    payload = {
        'username': username,
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRY_SECONDS)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token expired'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        if token.startswith('Bearer '):
            token = token[7:]
        decoded = decode_token(token)
        if 'error' in decoded:
            return jsonify(decoded), 401
        request.username = decoded['username']
        request.user_id = decoded['user_id']
        return f(*args, **kwargs)
    return decorated

