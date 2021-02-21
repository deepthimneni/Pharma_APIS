import os
import jwt
from hashlib import pbkdf2_hmac
from functools import wraps 
from src.models.User import User
from flask import request, jsonify
import sys

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# password salt technique
def generate_salt():
    salt = os.urandom(16)
    return salt.hex()

# password hash technique
def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY)
    # print('user id is:', content)
    # print('encoded content is :', str(encoded_content))
    # token = str(encoded_content).split("'")[1]
    return encoded_content

def token_required(f): 
    @wraps(f) 
    def decorated(*args, **kwargs): 
        token = None
        # jwt is passed in the request header 
        if 'x-access-token' in request.headers: 
            token = request.headers['x-access-token'] 
        # return 401 if token is not passed 
        if not token: 
            return {'error_msg' : 'Token is missing !!!'}, 401
   
        try: 
            # decoding the payload to fetch the stored details 
            data = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            current_user = User.query.filter_by(id = data['id']).first() 
        except: 
            return { 
                'error_msg' : sys.exc_info()
            }, 401
        # returns the current logged in users contex to the routes 
        return  f(current_user, *args, **kwargs) 
   
    return decorated 