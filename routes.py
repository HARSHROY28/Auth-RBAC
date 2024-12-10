from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .auth import authenticate
from .models import User, Role
from . import db, bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password_hash=hashed_pw, role_id=data.get('role_id', 2))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return authenticate(data['username'], data['password'])

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return jsonify({'message': f'Welcome, {user["username"]}!'})