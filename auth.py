from flask import jsonify
from flask_jwt_extended import create_access_token
from .models import User
from . import bcrypt, db

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        token = create_access_token(identity={'username': user.username, 'role': user.role_id})
        return jsonify({'access_token': token})
    return jsonify({'message': 'Invalid credentials'}), 401