from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import create_user, get_user_by_username
from app.utils.jwt_handler import generate_token, token_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    hashed_password = generate_password_hash(password)
    success = create_user(username, hashed_password)

    if not success:
        return jsonify({'error': 'Username already exists'}), 409

    return jsonify({'message': 'Signup successful'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400

    user = get_user_by_username(username)
    if user and check_password_hash(user['password'], password):
        token = generate_token(username, user['id'])
        return jsonify({'username':username, 'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    
@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': f'Hello, {request.username} with id {request.user_id}! This is a protected route.'})
