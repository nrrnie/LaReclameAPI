from sqlalchemy.exc import IntegrityError
from passlib.hash import sha256_crypt
from flask import request

from api.models import Users
from api.auth import auth
from api import db


@auth.route('/add/user', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    if None in [username, password, email]:
        return {
            'status': 'error',
            'error': 'Not all data was given.'
        }

    hashed_password = sha256_crypt.hash(password)

    user = Users(username=username, password=hashed_password, email=email)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError as e:
        error_text = e.args[0]
        if error_text.find('users.username') != -1:
            return {
                'status': 'error',
                'error': 'User with such username already exists.'
            }
        elif error_text.find('users.email') != -1:
            return {
                'status': 'error',
                'error': 'User with such email already exists.'
            }

    return {
        'status': 'ok'
    }


@auth.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if None in [username, password]:
        return {
            'status': 'error',
            'error': 'Not all data was given.'
        }

    user = Users.query.filter_by(username=username).first()

    if user is None or not sha256_crypt.verify(password, user.password):
        return {
            'status': 'error',
            'error': 'Username or password is incorrect.'
        }

    return {
        'status': 'ok'
    }
