from flask import Blueprint, request, Response, jsonify
from src.models.User import User
from src.utils.Utils import generate_salt, generate_hash, generate_jwt_token
from flask_apispec import use_kwargs, marshal_with, doc
from src.models.extensions import ErrorSchema, docs, LoginSchema
from webargs import fields
from datetime import datetime, timedelta
login_authentication = Blueprint("login_authentication", __name__)

@login_authentication.route("/login", methods=["POST"], provide_automatic_options=False)
@marshal_with(LoginSchema, code = 200)
@marshal_with(ErrorSchema, code = 401)
@marshal_with(None, code = 400, apply=False)
@doc(tags=['User Actions'])
@use_kwargs({'user_name': fields.Str(),  
            "password":fields.Str()})
def login_auth(**kwargs):
    user_name = kwargs.get("user_name")
    #http request, request content , json key value pairs, user_name is key, will the get value
    # admin = request.json["phone"]
    password = kwargs.get("password")
    if (len(user_name) != 0 and len(password) != 0) :
        record= User.query.filter(User.user_name == user_name).first()
        if (record):
            password_hash = generate_hash(password, record.password_salt)
            if (password_hash == record.password_hash):
                user_id = record.id
                jwt_token = generate_jwt_token({
                    "id": user_id,
                    'exp' : datetime.utcnow() + timedelta(minutes = 30) 
                })
                return {"jwt_token": jwt_token}, 200
            else:
                return  {"error_msg": "Password incorrect"}, 401
        else:
            return  {"error_msg": "Users not found"}, 401
    else:
        return None, 400

docs.register(login_auth, blueprint=login_authentication.name)