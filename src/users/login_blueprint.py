from flask import Blueprint, request, Response, jsonify
from src.models.User import User
from src.utils.Utils import generate_salt, generate_hash
from flask_apispec import use_kwargs, marshal_with, doc
from src.models.extensions import ErrorSchema, docs, LoginSchema
from webargs import fields

login_authentication = Blueprint("login_authentication", __name__)

@login_authentication.route("/login", methods=["POST"])
@marshal_with(LoginSchema, code = 200)
@marshal_with(ErrorSchema, code = 401)
@marshal_with(None, code = 400)
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
                jwt_token = generate_jwt_token({"id": user_id})
                return {"jwt_token": jwt_token}
            else:
                return  {"error_msg": "Password incorrect"}
        else:
            return  {"error_msg": "Users not found"}
    else:
        return

docs.register(login_auth, blueprint=login_authentication.name)